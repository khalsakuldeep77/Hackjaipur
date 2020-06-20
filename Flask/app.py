import pyrebase 
from flask import *
app = Flask(__name__)

config = {
    "apiKey": "AIzaSyD8KT7KJ54oTgURRg0FiZPE1t5lPnxP4l0",
    "authDomain": "test1-3741d.firebaseapp.com",
    "databaseURL": "https://test1-3741d.firebaseio.com",
    "projectId": "test1-3741d",
    "storageBucket": "test1-3741d.appspot.com",
    "messagingSenderId": "628133344506",
    "appId": "1:628133344506:web:519cabaafff645dd7e0543",
    "measurementId": "G-2TY6Q3D7ZT"
  }

firebase = pyrebase.initialize_app(config)


auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def basic():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('new.html', s=successful)
		except:
			return render_template('new.html', us=unsuccessful)

	return render_template('new.html')


if __name__ == '__main__':
	app.run()
