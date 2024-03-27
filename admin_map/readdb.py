import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pyautogui


# Initialize Firebase Admin SDK
cred = credentials.Certificate("connection.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://puhackthon-default-rtdb.firebaseio.com/'
})

# Reference to your Firebase Realtime Database\
ref = db.reference('start/')
read = ref.get()

if read == 'start':
    pyautogui.press("space",presses=1)  
    print("Pressed") 
 
if read == 'stop':
    pyautogui.press("space")

