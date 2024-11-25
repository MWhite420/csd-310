import mysql.connector
from mysql.connector import errorcode


config ={
"user" : "root",
"password" : "Education.2025",
"host" : "127.0.0.1",
"database" : "movies",
"raise_on_warnings" :True

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
