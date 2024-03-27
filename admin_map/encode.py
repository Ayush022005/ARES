import firebase_admin
import cv2
import base64
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("connection.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://puhackthon-default-rtdb.firebaseio.com/'
})

# Read image
image_path = "nigg.jpg"  # Replace with your image path
img = cv2.imread(image_path)
# encode 
_, image_data = cv2.imencode(".jpg", img)  # Encode using preferred format (replace if needed)
image_data_bytes = image_data.tobytes()

base64_encoded_string = base64.b64encode(image_data_bytes).decode("utf-8")


# Reference to your Firebase Realtime Database

ref = db.reference('/')

# Data to be sent
data = {
    'start': base64_encoded_string
}

# Push data to Firebase Realtime Database
ref.set(data)

print("Data sent successfully to Firebase Realtime Database.")


