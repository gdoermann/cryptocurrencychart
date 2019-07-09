"""
The config file is placed in ~/.cryptocurrencychart and should be in the following format:

[default]
KEY = API KEY
SECRET = API SECRET
"""
import os
from configparser import ConfigParser

CONFIG_FILE = os.getenv('CONFIG_FILE', os.path.join(os.environ.get("HOME"), '.cryptocurrencychart'))

parser = ConfigParser()
parser.read([CONFIG_FILE, ])
