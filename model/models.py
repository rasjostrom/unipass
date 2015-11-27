from uuid import uuid1 
import inspect 
import sys
import sqlite3 as lite
import hashlib

from db import Model
from descriptors import Descriptor, GetDescriptor


"""
models.py

This file is used to define persistance objects.
The only this that you have to care abour here is to inherit from Model
if creating a new persistance object.

The descriptors is only used to talk to the "controller" layer and dont 
have anything to do with persistance.

the initdb() function will check in this file for classes and
creates the database depending on the objects in here.
there is no migration options here. 
if made changes, remove database and run the application again.

Example:
class User(Model):  // Inherits from Model

    uuid = GetDescriptor('_uuid')  // UUID = Universally unique identifier
                                   // This uuid is the value that we use in database
    
    def __init__(self, **kwargs):  // Constructor
        super(Model, self).__init__()  // Call parent
        self._uuid = (kwargs['_uuid'] if '_uuid' in kwargs else str(uuid1()))  // <- This one is required!
        self._name = (kwargs['_name'] if '_name' in kwargs else '')  // <- Optional
        self._password = (kwargs['_password'] if '_password' in kwargs else '')  // <- Optional

"""


class User(Model):
    """ User object
    """
    uuid = GetDescriptor('_uuid')
    
    def __init__(self, **kwargs):
        super(Model, self).__init__()
        self._uuid = (kwargs['_uuid'] if '_uuid' in kwargs else str(uuid1()))
        self._name = (kwargs['_name'] if '_name' in kwargs else '')
        self._password = (kwargs['_password'] if '_password' in kwargs else '')

        
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
    
        

    
