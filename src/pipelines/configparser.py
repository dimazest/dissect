import os.path
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

import pipelines


all = 'configparser'


configparser = SafeConfigParser(
    {'_package_dir': os.path.abspath(os.path.dirname(pipelines.__file__))}
)
