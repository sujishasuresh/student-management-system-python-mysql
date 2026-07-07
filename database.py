import pymysql

conn=pymysql.connect(host="localhost",user="root",password="YOUR_PASSWORD",database="student_management",cursorclass=pymysql.cursors.DictCursor)
curr=conn.cursor()
