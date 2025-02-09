import mysql.connector
user="root"
password="" 

database = "project"
port=3306
def select(q):
	cnx = mysql.connector.connect(user="root", password=password,port=port, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	result = cur.fetchall()
	cur.close()
	cnx.close()
	return result
def update(q):
	cnx = mysql.connector.connect(port=port,user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount  
	cur.close()
	cnx.close()
	return result
def delete(q):
	cnx = mysql.connector.connect(port=port,user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount
	cur.close()
	cnx.close()
def insert(q):
	cnx = mysql.connector.connect(port=port,user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.lastrowid
	cur.close()
	cnx.close()
	return result


