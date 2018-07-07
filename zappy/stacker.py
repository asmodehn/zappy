import collections
import queue


class Stacker(collections.MutableMapping):
    """
    A dictionary of stacks, that can also be seen as a stack of dictionaries
    Implemented with queue.LifoQueue to provide proper locking semantics when needed
    TODO : A way (meta class?) to provide different stack implementations
    """

    def __init__(self, seq=None, **kwargs):
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, stack(value)) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        # (copied from class doc)
        """
        self.store = dict()
        # iterating on seq(and putting identical names in one stack in order)
        if seq is not None:
            for k, v in seq:
                self.store.setdefault(k, queue.LifoQueue())
                self.store[k].put(v)
        # filling up our dict store
        for k, v in kwargs.items():
            self.store.setdefault(k, queue.LifoQueue())
            self.store[k].put(v)

    def __getitem__(self, key):
        try:
            # we want to get what is there now, if there is nothing, this is an error.
            # It has the same semantics as accessing a key in a dict
            v = self.store[key].get_nowait()
            # but if it is the last, we want to erase the key completely from our dict.
            # Empty stack has no meaning.
            if self.store[key].empty():
                del self.store[key]
            return v
        except queue.Empty:
            raise KeyError('e')

    def __setitem__(self, key, value):
        # Here we want to wait to potentially serialize addition on the stack
        # It has the same semantics as setting a key in a dict, plus ensure linearization of writes
        self.store[key].put(value)
        # TODO : potentially limit the stack to avoid taking in all the memory?

    def __delitem__(self, key):
        try:
            # Here we want to consume one element from the stack ( should be the last one )
            # and ignoring its value. Therefore an empty stack error can be handled in here and not raised up.
            self.store[key].get_nowait()
        except queue.Empty:
            del self.store[key]

    def __iter__(self):
        # We iterate on the first level of all stacks, effectively providing a simple dictionary
        return iter({k: self.__getitem__(k) for k in self.store})

    def __len__(self):
        return len(self.store)
