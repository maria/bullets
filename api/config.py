HOST = '0.0.0.0'
MONGODB_SETTINGS = {
    'db': 'bullets',
    'host': 'localhost'
}

try:
    from config_local.py import *
except Exception:
    print 'No local config file'
