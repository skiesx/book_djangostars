from ._django import *
from ._apps import *
# from ._static import *
# from ._project import *
try:
    from .local import *
except ImportError:
    pass
