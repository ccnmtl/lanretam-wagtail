# flake8: noqa
from lanretam.settings_shared import *

try:
    from lanretam.local_settings import *
except ImportError:
    pass
