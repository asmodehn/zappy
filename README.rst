=====
Zappy
=====


.. image:: https://img.shields.io/pypi/v/zappy.svg
        :target: https://pypi.python.org/pypi/zappy

.. image:: https://img.shields.io/travis/asmodehn/zappy.svg
        :target: https://travis-ci.org/asmodehn/zappy

.. image:: https://readthedocs.org/projects/zappy/badge/?version=latest
        :target: https://zappy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/asmodehn/zappy/shield.svg
     :target: https://pyup.io/repos/github/asmodehn/zappy/
     :alt: Updates



Zero Assumption Programming Python


* Free software: MIT license
* Documentation: https://zappy.readthedocs.io.


Features
--------

Based on functools.py, the goals are to :

* research the one true way to do functional programming in python
* use function properties to improve stability of program execution, even in hte face of hardware failures
* use control theory to maximize the (optimization,determinism) tuple in unknown computing environments.

Roadmap :

* [ ] purity check (potentially using types) - foundation 1
* [ ] use purity check to actually isolate computation (SECCOMP, VM, etc.) when possible
* [ ] determinism/idempotency check (potentially using types) - foundation 2
* [ ] use determinism/idempotency check to detect HW/underlying computing system failures
* [ ] use determinism/idempotency check to recover from HW/underlying computing system failures
* [ ] use determinism/idempotency check to optimise when possible (similar to functools.lru_cache)
* [ ] implement a single @zap decorator that can provide extreme guarantees about the execution of the decorated function.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
