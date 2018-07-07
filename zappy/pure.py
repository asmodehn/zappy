import contextlib
import functools

# We grab modules early to minimize interferences from other part of the code.
import sys
_sys = sys
import os
_os = os


from .stacker import Stacker

class ZAPImpurityDetected(Exception):
    pass


def maybe_list(l):
    return l if isinstance(l, list) else [l]


# we keep a global dict of overridden procedures
# We need to be quite monadic to support reentrant updates...
backup_dict = Stacker()


# we want to have only one reference to the raising procedure
def forbidden_procedure(*args, **kwargs):
    raise ZAPImpurityDetected()


# Special context manager to replace builtins in globals
@contextlib.contextmanager
def override_builtin(impure):

    impures = (imp for imp in maybe_list(impure))

    # we backup in '__zappy_builtins_backup__' what needs to be
    # CAREFUL : we need to be reentrant to support multiple identical overrides (be monadic !)
    backup_dict.update((i for i in globals()['__builtins__'].items() if i[1] in impures))
    # we replace in '__builtins__' what needs to be
    globals()['__builtins__'].update({imp.__name__: forbidden_procedure for imp in impures})
    yield
    # we restore what was backed up previously
    # Our Stacker will pop retrieved procedures
    globals()['__builtins__'].update({imp.__name__: backup_dict.get(imp.__name__) for imp in impures})


def pure(pure_function):

    # Here we redefine any impure python construct.
    # Python being extremely customizable, it is likely not possible to cover all cases here.
    # So this will be done on a best effort basis.
    # If you find another python method that should be overridden, or a better way to do it, please submit a PR.

    @functools.wraps(pure_function)
    def pure_wrapper(*args, **kwargs):
        # replacing forbidden procedures to have them raise instead.
        with (override_builtin(print)):

            return pure_function(*args, **kwargs)

    return pure_wrapper
