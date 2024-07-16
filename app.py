from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
from flask_mail import Mail, Message

# MySQL setup
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pythoncourse'
app.config['MYSQL_DB'] = 'school'
mysql = MySQL(app)

# Email setup
app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ngoanhkhoi2004@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def email_send():
    if request.method == 'POST':
        email = request.form['email']
        msg = Message("Nhom nhom", sender='ngoanhkhoi2004@gmail.com', recipients='ngoanhkhoi2004@gmail.com')
        msg.body = f"New message from titiuoi. Check it asap!"
        mail.send(msg)
        
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)