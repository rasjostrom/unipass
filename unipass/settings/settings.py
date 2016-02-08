import os

DEGUB = True

if not DEGUB:
    HOME_DIR = os.path.expanduser('~')
    DATABASE_NAME = 'sqlite3.db'
    DATABASE_LOCATION = HOME_DIR + '/.unipass/'
    DB = DATABASE_LOCATION+DATABASE_NAME
else:
    HOME_DIR = os.path.expanduser('~')
    DATABASE_LOCATION = '.'
    DB = 'sqlite3.db'



