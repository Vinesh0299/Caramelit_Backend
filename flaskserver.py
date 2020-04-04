# Importing required modules
from flask import Flask, render_template, jsonify, request, redirect
from flask_mail import Mail, Message

# Contact ticket number
ticket = 1

# Initialize the flask app
app = Flask(__name__)

# Importing config
app.config.from_pyfile('configmail.cfg')
# Initialize the Mail class
mail = Mail(app)

@app.route('/')
# returns the contact us page
def contact_us():
    return render_template('contactform.html')

@app.route('/data', methods=['POST'])
# Sends the mail and redirects to contact us page
def data():
    global ticket
    msg = Message(
        subject="Ticket #" + str(ticket),
        sender=app.config.get("MAIL_USERNAME"),
        recipients=["Madarauchiha3524@gmail.com"],
        body="Name: " + str(request.form['name']) + "\n Email: " + str(request.form['email']) + "\n Phone: " + str(request.form['phone']) + "\n pincode: " + str(request.form['pincode']) + "\n Budget: " + str(request.form['budget']) + "\n Service: " + str(request.form['service']) + "\n Country: " + str(request.form['country']) + "\n"
    )
    mail.send(msg)
    ticket += 1
    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)