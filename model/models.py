from uuid import uuid1 
import inspect 
import sys
import sqlite3 as lite

from model.db import Model
from model.descriptors import Descriptor, GetDescriptor, AdminDescriptor


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
    """
    User object
    """
    uuid = GetDescriptor('_uuid')
    name = Descriptor('_name')
    password = Descriptor('_password')
    admin = AdminDescriptor('_admin')
    
    def __init__(self, **kwargs):
        super(Model, self).__init__()
        self._uuid = (kwargs['_uuid'] if '_uuid' in kwargs else str(uuid1()))
        self._name = (kwargs['_name'] if '_name' in kwargs else '')
        self._password = (kwargs['_password'] if '_password' in kwargs else '')
        self._note = (kwargs['_note'] if '_note' in kwargs else '')
        self._admin = (kwargs['_admin'] if '_admin' in kwargs else False)

    def valid(self):
        if len(self._name) == 0:
            return False
        if len(self._password) == 0:
            return False
        if len(self._uuid) == 0:
            return False
        return True


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
        
    except IOError:
        con = lite.connect('sqlite3.db')
        cur = con.cursor()
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for cls in clsmembers:
            if isinstance(cls[0], str):
                cur.execute("CREATE TABLE {}(id INTEGER PRIMARY KEY, uuid TEXT, data BLOB)".format(cls[0]))
        con.close()
        return False


