from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category):
        if not name or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        if not category or len(category) == 0:
            raise ValueError("Category cannot be empty.")
        
        self.name = name
        self.category = category
        
        # Insert into the database and fetch the auto-generated id
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        
        self.id = cursor.lastrowid  # Get the id of the inserted magazine
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

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if hasattr(self, '_category'):
            raise ValueError("Category cannot be modified after initialization.")
        self._category = value
