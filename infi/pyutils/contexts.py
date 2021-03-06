import sys
from .decorators import wraps

_PYTHON_VERSION = sys.version_info

if _PYTHON_VERSION >= (3,):
    from contextlib import _GeneratorContextManager
else:
    from contextlib import GeneratorContextManager as _GeneratorContextManager


if _PYTHON_VERSION >= (3,5):
    def contextmanager(func):
        @wraps(func)
        def helper(*args, **kwds):
            return _GeneratorContextManager(func, args, kwds)
        return helper

elif _PYTHON_VERSION >= (3,2,2):
    def contextmanager(func):
        @wraps(func)
        def helper(*args, **kwds):
            return _GeneratorContextManager(func, *args, **kwds)
        return helper
else:
    def contextmanager(func):
        @wraps(func)
        def helper(*args, **kwds):
            return _GeneratorContextManager(func(*args, **kwds))
        return helper
