from flask import Flask, render_template, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.from_pyfile('configmail.cfg')
mail = Mail(app)

@app.route('/')
def contact_us():
    return render_template('contactform.html')

@app.route('/data', methods=['POST'])
def data():
    msg = Message(subject="TEst", sender=app.config.get("MAIL_USERNAME"), recipients=["Madarauchiha3524@gmail.com"], body="This is a test mail for" + request.form['name'])
    mail.send(msg)
    return render_template('contactform.html')

if __name__ == '__main__':
    app.run(debug=True)