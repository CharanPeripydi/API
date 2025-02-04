from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'  
    app.config['MYSQL_PASSWORD'] = 'July1@2000' 
    app.config['MYSQL_DB'] = 'employee_manage'  
    mysql.init_app(app)