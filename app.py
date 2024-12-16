# /app.py

from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Use a context manager to ensure the database connection is properly closed
    with get_db_connection() as conn:
        cursor = conn.cursor()

        '''
            The following is just for testing purposes, 
            you can modify it to meet the requirements of your implementation.
        '''

        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid  # Use this to fetch the id of the newly created author

        # Create a magazine
        magazine = Magazine(magazine_name, magazine_category)
        magazine_id = magazine.id  # Automatically assigned by the Magazine constructor

        # Create an article
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (article_title, article_content, author_id, magazine_id))

        conn.commit()

        # Query the database for inserted records. 
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()

        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(f"ID: {magazine['id']}, Name: {magazine['name']}, Category: {magazine['category']}")

    print("\nAuthors:")
    for author in authors:
        print(f"ID: {author['id']}, Name: {author['name']}")

    print("\nArticles:")
    for article in articles:
        print(f"ID: {article['id']}, Title: {article['title']}, Content: {article['content']}, Author ID: {article['author_id']}, Magazine ID: {article['magazine_id']}")

if __name__ == "__main__":
    main()
