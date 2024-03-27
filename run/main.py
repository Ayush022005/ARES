import cv2
from ultralytics import YOLO
import firebase_admin
import base64
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("connection.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://puhackthon-default-rtdb.firebaseio.com/'
})


# Load the YOLOv8 model
model = YOLO('best_injured.pt')

# Open the video file
video_path = "main.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame,conf=0.95)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        for r in results:
        
          boxes = r.boxes
          for box in boxes:
            
             c = box.cls
             if model.names[int(c)] =="injured":
                print("We are able to send img")

                cv2.imwrite('live_feed.png',annotated_frame)

                img = cv2.imread("live_feed.png")

                _, image_data = cv2.imencode(".jpg", img)  # Encode using preferred format (replace if needed)
                image_data_bytes = image_data.tobytes()

                base64_encoded_string = base64.b64encode(image_data_bytes).decode("utf-8")

                ref = db.reference('/')

                data = {
                    'start': base64_encoded_string
                 }


                ref.set(data)




       # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()