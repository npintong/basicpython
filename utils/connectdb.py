import pymysql.cursors

def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='pythontestdb',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    return connection

print(getConnection())
