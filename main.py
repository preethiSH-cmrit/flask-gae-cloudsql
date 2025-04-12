from flask import Flask, render_template
import mysql.connector
import os
app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]
# Replace with your actual cloud MySQL credentials for testing locally
# db_config = {
#     'host': '34.135.184.228',        # e.g., '34.168.xxx.xxx' or Cloud SQL private IP for connecting locally
#     'user': 'root',
#     'password': 'your-password',
#     'database': 'guestdb',
# }

db_config = {
    'user': os.environ["DB_USER"],
    'password': os.environ["DB_PASSWORD"],
    'database': os.environ["DB_NAME"],
    'unix_socket': os.environ["DB_SOCKET_PATH"]
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tblguest")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', rows=rows)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
