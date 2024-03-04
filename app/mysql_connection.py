import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql-service.db.svc.cluster.local',
        user='Lim',
        password='password123',
        database='mydatabase'
    )
    return connection
