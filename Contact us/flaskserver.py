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

@app.route('/contact/form')
# returns the contact us page
def contact_us():
    return render_template('contactform.html')

@app.route('/sendcontactform', methods=['POST'])
# Sends the mail and redirects to contact us page
def data():
    global ticket
    try:
        msg = Message(
            subject="Ticket #" + str(ticket),
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["Madarauchiha3524@gmail.com", "krishnamurthy.pradhan@gmail.com", "krishnamurthy.p@caramelt.com", "madarauchiha3525@gmail.com"],
            body="Name: " + str(request.form['name']) + "\n Email: " + str(request.form['email']) + "\n Phone: " + str(request.form['phone']) + "\n pincode: " + str(request.form['pincode']) + "\n Budget: " + str(request.form['budget']) + "\n Service: " + str(request.form['service']) + "\n Country: " + str(request.form['country']) + "\n"
        )
        mail.send(msg)
        ticket += 1
    except Exception as e:
        print(e)
    return redirect('/contact/form')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)