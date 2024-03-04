from flask import Flask
from mysql_connection import get_db_connection

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/health', methods=['GET'])
def health_check():
    return {"status": "UP"}, 200

@app.route('/metrics', methods=['GET'])
def monitoring():
    return {"status": "UP"}, 200

@app.route('/data')
def get_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM people")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return str(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)