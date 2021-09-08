import pymysql

connection = pymysql.connect(host='ali-server.private', port=9006, password='passwd', db='health')
cursor = connection.cursor()

