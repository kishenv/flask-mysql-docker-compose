'''Python Web-app to fetch and display details from a database'''
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_PORT'] =  3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        user = details['fname']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM vms WHERE USER = %s", [user])
        result = cur.fetchall()
        print(type(result))
        mysql.connection.commit()
        cur.close()
        if not result:
            return 'No such user'
        else:
            return render_template("result.html", data=result)
    return render_template("mysql.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 
