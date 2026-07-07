import pymysql

conn=pymysql.connect(host="localhost",user="root",password="Sujisha03@",database="student_management",cursorclass=pymysql.cursors.DictCursor)
curr=conn.cursor()
# sql1="insert into student values(1,'Taylor','Female','2000-01-15','tayalor20@gmail.com')"
# curr.execute(sql1)
# conn.commit()
# conn.close()