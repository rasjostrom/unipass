import os

#DATABASE_LOCATION = '~/.unipass/sqlite3.db'
HOME_DIR = os.path.expanduser('~')
DATABASE_NAME = 'sqlite3.db'
DATABASE_LOCATION = HOME_DIR + '/.unipass/'
DB = DATABASE_LOCATION+DATABASE_NAME


