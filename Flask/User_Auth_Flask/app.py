import pyrebase 

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

email = input('Please Enter your Email\n')
password = input('Please enter your password\n')

user = auth.create_user_with_email_and_password(email, password)
#user = auth.sign_in_with_email_and_password(email, password)

auth.get_account_info(user['idToken'])