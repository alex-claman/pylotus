# pylotus/__init__.py

import requests

session = requests.Session()

from .wf_api import *
from .response_classes import *
from .exceptions import *