import requests
import sqlite3
import logging
import time


def get_dog_breeds():
    """ Fetch the list of all dog breeds from the Dog API https://dog.ceo/dog-api/documentation/
        Aforementioned link suggest using - https://dog.ceo/api/breeds/list/all to get all breeds (alongwith sub-breeds)

    Returns:
        breeds: Hastable with breed as the key and sub-breed and value. 
    """
    try:
        response = requests.get('https://dog.ceo/api/breeds/list/all')
        breeds = response.json().get('message', {})
        return breeds
    except Exception as e:
        print(f'Failed to get Dog Breeds - {e}')

def create_databases():
    """Connect to SQLite database (or create it)

    Returns:
        connection: Connection variable holds the connection object to the SQLite database file.
        cursor: The cursor is used to execute SQL commands and queries on the database.
    """
    
    try:
        connection = sqlite3.connect('dogs.db')
        cursor = connection.cursor()

        # Create breeds table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS breeds (
            breed TEXT PRIMARY KEY
        )
        ''')

        # Create sub-breeds table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sub_breeds (
            breed_name TEXT,
            subBreedCount INTEGER
        )
        ''')
        return connection, cursor
    except Exception as e:
        print(f'Failed to Create Databases - {e}')
    
def insert_breeds(c, breeds):
    """ Insert breeds into the breeds table.
    
    Args:
      c: DB Connection
      breeds: DB Connection Cursor
    """
    
    try:
        for breed in breeds:
            c.execute('INSERT OR IGNORE INTO breeds (breed) VALUES (?)', (breed,))
        print(f"Done inseting data in breeds Table!")
    except Exception as e:
        print(f'Failed to insert data in Breeds DB - {e}')

def insert_sub_breeds(c, breeds):
    """ Insert data into sub-breeds table.

    Args:
      c: DB Connection
      breeds: DB Connection Cursor
    """
    
    try:
        for breed, sub_breeds in breeds.items():
            c.execute('INSERT INTO sub_breeds (breed_name, subBreedCount) VALUES (?, ?)', (breed, len(sub_breeds)))
        print(f"Done inseting data in sub-breeds Table!")
    except Exception as e:
        print(f'Failed to insert data in sub_breeds DB - {e}')
        
        
def main():
    logging.basicConfig(level=logging.ERROR)
    breeds = get_dog_breeds()
    conn, c = create_databases()
    insert_breeds(c, breeds)
    insert_sub_breeds(c, breeds)
    conn.commit()
    conn.close()
    
    # Keep the script running for 10 minutes to allow testing
    time.sleep(600)

if __name__ == "__main__":
    main()