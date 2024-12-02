#Mark White
#CSD310
#Assignment8.2


import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values(".env")

def show_films(cursor, title):
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for row in films:
        print("Film Name: {}\n Director: {}\n Genre Name ID: {}\n Studio Name: {}\n".format(row[0], row[1], row[2], row[3]))


def main(): 
    config = {
    "user" : secrets["USER"],
    "password" : secrets["PASSWORD"],
    "host" : secrets["HOST"],
    "database" : secrets["DATABASE"],
    "raise_on_warnings" : secrets["RAISE_ON_WARNINGS"],
    }
    
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    # Call the function
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE ")
    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()