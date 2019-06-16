import sqlite3
import os

class DB:
    def create_connection(self):
        try:
            conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)), 'sqlite.db')
            return conn
        except Exception  as e:
            print(e)
        finally:
            conn.close()