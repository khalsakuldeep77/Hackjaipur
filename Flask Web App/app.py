import pyrebase 
from flask import *
import os
from werkzeug.utils import secure_filename
import requests
import json, requests, datetime
from flask_cors import CORS

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'many random bytes'

cors = CORS(app)

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
			return redirect("http://127.0.0.1:5000/upload")
		except:
			return render_template('new.html', us=unsuccessful)

	return render_template('new.html')

@app.route('/upload', methods=['GET'])

def basic2():
        return render_template('upload.html')

@app.route('/upload', methods=['POST'])

def basic3():
        file = request.files['upload']
        url2 = request.form.get('url')
        filename = secure_filename(file.filename)
        new_path = os.path.abspath(filename)
        print(new_path)

        url = 'http://127.0.0.1:3000/'
        # date_time = datetime.datetime.strptime('1/10/2018 21:45:00', '%d/%m/%Y %H:%M:%S').timestamp()
        j_data = json.dumps({"url":url2})
        r = requests.post(url, data=j_data)

        print(r, r.text)

        result = "Your detection is {}".format(r.text)

        print(r.text.rstrip(), "\"Tlevel0\"")

        print(r.text.rstrip() == "\"Tlevel0\"")

        if str(r.text).rstrip() == "\"Tlevel0\"":
                print('abc')
                flash("No Non-proliferative diabetic retinopathy")
        elif str(r.text).rstrip() == "\"Tlevel1\"":
                print('avcd')
                flash("Mild Non-proliferative diabetic retinopathy")
        elif str(r.text).rstrip() == "\"Tlevel2\"":
                print('123')
                flash("Moderate Non-proliferative diabetic retinopathy")
        elif str(r.text).rstrip() == "\"Tlevel3\"":
                print('1231')
                flash("High Non-proliferative diabetic retinopathy")
        else:
                flash("Severe Non-proliferative diabetic retinopathy")
        
        #flash("Hello")
        
        return render_template('upload.html', prediction=r.text)

if __name__ == '__main__':
	app.run()
