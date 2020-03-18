import MySQLdb

host = "localhost"
user = "application"
password = "123456"
db = "escola"
port = 3306

connection = MySQLdb.connect(host, user, password, db, port)