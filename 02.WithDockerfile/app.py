# app.py

from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Read environment variables
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
table_name = os.environ.get('TABLE_NAME')

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
db_cursor = db_connection.cursor()

# Create a route to insert data into the table
@app.route('/insert')
def insert_data():
    query = "INSERT INTO {} (name, email) VALUES (%s, %s)".format(table_name)
    values = ('John Doe', 'john@example.com')
    db_cursor.execute(query, values)
    db_connection.commit()
    return 'Data inserted successfully!'

# Create a route to select data from the table
@app.route('/select')
def select_data():
    query = "SELECT * FROM {}".format(table_name)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
