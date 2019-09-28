# from flaskext.mysql import MySQL
# from flask import Flask

# mysql = MySQL()
# def connect(app):  # mysql connection
#     app.config['MYSQL_HOST'] = 'localhost'
#     app.config['MYSQL_USER'] = 'root'
#     app.config['MYSQL_PASSWORD'] = 'mirim2'
#     app.config['MYSQL_DB'] = 'seoul'
#     mysql.init_app(app)
#     global cur
#     conn = mysql.connect()
#     cur = conn.cursor()


# def login(id, pwd):  # 예외처리해야함.
#     cur.execute('SELECT id,pwd FROM member where id = ' + id)
#     rv = cur.fetchall()
#     return str(rv)


# if __name__ == '__main__':
#     app = Flask(__name__)
#     connect(app)
    
