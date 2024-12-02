#Mark White
#CSD310
#Assignment7.2

import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values(".env")

config = {
"user" : secrets["USER"],
"password" : secrets["PASSWORD"],
"host" : secrets["HOST"],
"database" : secrets["DATABASE"],
"raise_on_warnings" : True,

}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# First query: fields from studio table
cursor.execute("SELECT studio_id, studio_name FROM studio")
result_studio = cursor.fetchall()
print("--DISPLAYING studio RECORDS--")
for row in result_studio:
    print("Studio ID: {}\nStudio Name: {}\n".format(row[0], row[1]))

# Second query: fields of genre table
cursor.execute("SELECT genre_id, genre_name FROM genre")
result_genre = cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for row in result_genre:
    print("Genre ID: {}\nGenre Name: {}\n".format(row[0], row[1]))


# Third query: Select movie names with a run time of less than two hours
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120 ")
result_short_movies = cursor.fetchall()
print("--DISPLAYING Short Film RECORDS-- \n ")
for row in result_short_movies:
      print("Film Name: {}\nRuntime: {}\n".format(row[0], row[1]))

#Fourth query: Get a list of film names and directors grouped by director
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
result_director = cursor.fetchall()
print("--DISPLAYING director RECORDS--")
for row in result_director:
    print("Film Name: {}\n Director: {}\n".format(row[0], row[1]))