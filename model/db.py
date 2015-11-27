import sqlite3 as lite
import pickle 


class Model(object):
    """
    Database base class
    By extending this class you will get help with creating, updating and deleting database objects
    """
    def __init__(self):
        self._uuid = ''

        
    def create(self):
        """
        Save instance of model to db
        """
        con = lite.connect('sqlite3.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO {} (uuid, data) VALUES(?, ?)".format(self.__class__.__name__) , (self._uuid, pickle.dumps(self.__dict__)))
        con.close()
                                                                
        
    def update(self):
        """
        Update instance of model to db
        """
        con = lite.connect('sqlite3.db')
        with con:
            cur = con.cursor()
            cur.execute("UPDATE {} SET data=? WHERE uuid=?".format(self.__class__.__name__), (pickle.dumps(self.__dict__), self._uuid))
        con.commit()
        con.close()

        
    def delete(self):
        """
        Delete instance of model to db
        """
        con = lite.connect('sqlite3.db')
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM {} WHERE uuid=?".format(self.__class__.__name__), (self._uuid,))
        con.close()


    @classmethod
    def getbyuuid(self, uuid):
        """
        returns one object
        """
        con = lite.connect('sqlite3.db')
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM {} WHERE uuid=?".format(self.__name__), (uuid,)) 
        obj = cur.fetchone()
        try:
            return self(**pickle.loads(obj['data']))
        except TypeError:
            return None
        
        
    @classmethod
    def getall(self):
        """
        returns a list
        """
        con = lite.connect('sqlite3.db')
        con.row_factory = lite.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM {}".format(self.__name__))
        users = cur.fetchall()
        try:
            return [self(**pickle.loads(user['data'])) for user in users]
        except TypeError:
            print("Could not fetch users (db.py)")
            return []

    
    def __eq__(self, other):
        return self._uuid == other._uuid

