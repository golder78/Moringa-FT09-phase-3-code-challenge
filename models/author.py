# /models/Author.py

from database.connection import get_db_connection

class Author:
    def __init__(self, name):
        if not name or len(name) == 0:
            raise ValueError("Name cannot be empty.")
        
        self.name = name
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        
        self.id = cursor.lastrowid  # Fetch the id of the newly inserted author
        conn.close()
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise ValueError("Name cannot be modified after initialization.")
        self._name = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT a.title 
        FROM articles a
        JOIN authors au ON a.author_id = au.id
        WHERE au.id = ?
        ''', (self.id,))
        
        articles = cursor.fetchall()
        conn.close()
        
        return [article[0] for article in articles]

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT m.name
        FROM magazines m
        JOIN author_magazine am ON m.id = am.magazine_id
        WHERE am.author_id = ?
        ''', (self.id,))
        
        magazines = cursor.fetchall()
        conn.close()
        
        return [magazine[0] for magazine in magazines]
