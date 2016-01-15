import MySQLdb as mysql

db = None
DBUNAME = 'test'
DBPASS = 'test'
DBNAME = 'open_records'


def init_db():
	db = mysql.connect("localhost", DBUNAME, DBPASS, DBNAME)


if __name__ == "__main__":

