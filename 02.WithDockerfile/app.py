# app.py

from flask import Flask, jsonify,request, render_template
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
@app.route('/')
def index():
    return 'Flask MySQL App Perform <a href=./insert>Insert</a> and <a href="./select">Select</a> Operations'

# Create a route to insert data into the table
@app.route('/insert', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        query = f"INSERT INTO {table_name} (name, email) VALUES (%s, %s)"
        values = (name, email)
        db_cursor.execute(query, values)
        db_connection.commit()
        return 'Data inserted successfully!'
    else:
        return render_template('insert_form.html')

# Create a route to select data from the table
@app.route('/select')
def select_data():
    query = "SELECT * FROM {}".format(table_name)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
