# Caramelit_Backend
Code for the Caramel IT Academy's Website


## Contact Us Section
html file for the contact us form is under templates directory and css and JS files can be found under the static folder along with the images for webpage

validinput.js file takes the content of inputs name, email, phone and pincode and applies a simple check on them. Only when all checks are passed will the user be able to submit the form

flaskserver.py file takes the input from after the form is submitted and sends a mail through the flask_mail library which uses smtp server for sending mail.
All required details for mailing are stored in configmail.cfg file like sender mail username, password etc.

There is a ticket number variable that increases everytime a mail is successfully sent. The content of the mail as of now is simple it just list all the details in 'key: value' format