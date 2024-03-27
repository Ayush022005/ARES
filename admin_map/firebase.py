import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("connection.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://puhackthon-default-rtdb.firebaseio.com/'
})

# Reference to your Firebase Realtime Database
ref = db.reference('/')

# Data to be sent
data = {
    'start': 'sd'
}

# Push data to Firebase Realtime Database
ref.set(data)

print("Data sent successfully to Firebase Realtime Database.")


