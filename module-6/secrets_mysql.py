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
"raise_on_warnings" : secrets["RAISE_ON_WARNINGS"]

}

try:
    db = mysql.connector.connect(**config)
    print("\n Data base user{} connected to MYSQL on host {} with database{}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno ==  errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)
    
finally:
        db.close()
