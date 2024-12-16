# /models/Article.py

from database.connection import get_db_connection

class Article:
    def __init__(self, author, magazine, title):
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        
        self.title = title
        self.author = author
        self.magazine = magazine
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                       (title, author.id, magazine.id))
        conn.commit()
        
        self.id = cursor.lastrowid  # Fetch the id of the newly inserted article
        conn.close()
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise ValueError("Title cannot be modified after initialization.")
        self._title = value
    
    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author.id,))
        author = cursor.fetchone()
        conn.close()
        
        return author

    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine.id,))
        magazine = cursor.fetchone()
        conn.close()
        
        return magazine
