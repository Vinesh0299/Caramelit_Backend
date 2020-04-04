from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def contact_us():
    return render_template('contactform.html')

@app.route('/data', methods=['POST'])
def data():
    return jsonify(data=[
        request.form['name'],
        request.form['email'],
        request.form['phone'],
        request.form['pincode'],
        request.form['budget'],
        request.form['service'],
        request.form['country']
    ])

if __name__ == '__main__':
    app.run(debug=True)