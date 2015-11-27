from uuid import uuid1 
import inspect 
import sys
import sqlite3 as lite
import hashlib

from db import Model
from descriptors import Descriptor, GetDescriptor


class Entry(Model):
    """Password object.
    Name
    Password
    """

    uuid = GetDescriptor('_uuid')    
    name = Descriptor('_name')    
    password = Descriptor('_password')
    
    def __init__(self, **kwargs):
        super(Model, self).__init__()
        self._uuid = (kwargs['_uuid'] if '_uuid' in kwargs else str(uuid1()))
        self._name = (kwargs['_name'] if '_name' in kwargs else '')
        self._password = (kwargs['_password'] if '_password' in kwargs else '')


def initdb():
    """
    This function test if database exists
    It not, database is created with existing classes
    There is a little overhead here, Model is also created in the database.
    """
    try:
        open('sqlite3.db')
        con = lite.connect('sqlite3.db')
        con.close()
        return True
        
    except:
        con = lite.connect('sqlite3.db')
        cur = con.cursor()
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for cls in clsmembers:
            if isinstance(cls[0], str):
                cur.execute("CREATE TABLE {}(id INTEGER PRIMARY KEY, uuid TEXT, data BLOB)".format(cls[0]))
        con.close()
        return False


# Testing
if __name__ == '__main__':
    initdb()
    # e = Entry()
    # e.name = 'john'
    # e.password = 'password'
    # e.create()
    print(Entry().getall()[0].name)
    
        

    
