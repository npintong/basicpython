import pymysql.cursors
from utils import*

connection = utils.connectdb.getConnection()

try:
    cursor = connection.cursor()
    

except pymysql.Error as e:
    print("Error %s" %e.args[1])
finally:
    # ปิดการเชื่อมต่อฐานข้อมูล
    connection.close()
