import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd ="!@#abc12345",
    database="testdatabase"
    )

mycursor = db.cursor()
# mycursor.execute ("CREATE DATABASE testdatabase")
# mycursor.execute("CREATE TABLE User (username VARCHAR(25) NOT NULL, password VARCHAR(25) NOT NULL, personID int PRIMARY KEY AUTO_INCREMENT NOT NULL)")
# mycursor.execute("ALTER TABLE User ADD COLUMN name varchar(20) NOT NULL")

# mycursor.execute("DESCRIBE User")
# for x in mycursor:
#     print(x)

# q2 = "CREATE TABLE reviews(id int PRIMARY KEY AUTO_INCREMENT NOT NULL, user_id int NOT NULL, FOREIGN KEY (user_id) REFERENCES user(personID), content varchar(200), rating smallint DEFAULT 0 NOT NULL )"
# mycursor.execute(q2)


# mycursor.execute("ALTER TABLE User DROP COLUMN ")
# mycursor.execute("ALTER TABLE User CHANGE old_name new_name newtype ")

# inserting column
# mycursor.execute("INSERT INTO User (username, password) VALUES (%s,%s)", ("root", "root"))
# db.commit() when inserting data into column