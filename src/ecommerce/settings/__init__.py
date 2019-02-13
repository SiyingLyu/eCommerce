# ordering is important.
from .base import *

from .production import *

# good for going live
try:
	from .local import *
except:
	pass