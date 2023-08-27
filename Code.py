import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
from geopy.distance import geodesic
import pywhatkit as pwt
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector

class StyledButton(tk.Button):
    def __init__(self,*args,**kwargs):
        tk.Button.__init__(self,*args,**kwargs)
        self.config(
            relief = tk.FLAT,
            bg = "maroon",
            fg= "black",
            activebackground="maroon",
            activeforeground="black",
            padx=10,
            pady=10,
            font=("Helvetica",15),      
        )


# Function definitions for menu actions
def open_calendar():
    os.system("start outlookcal:")

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_file_explorer():
    os.system("start explorer")

def open_command_prompt():
    os.system("start cmd")

def open_control_panel():
    os.system("start control")

def open_task_manager():
    os.system("start taskmgr")

def open_settings():
    os.system("start ms-settings:")

def calculate_distance():
    print("Enter coordinates for Location 1")
    lat1=float(input("Enter Latitude for location 1"))
    lon1=float(input("Enter Longitude for location 1"))
    print("Enter coordinates for Location 2")
    lat2=float(input("Enter Latitude for location 2"))
    lon2=float(input("Enter Longitude for location 2"))
    
    coords1 = (lat1,lon1)
    coords2 = (lat2,lon2)

    distance=geodesic(coords1,coords2).kilometers
    print(f"Distance between locations is {distance:.2f} kilometers")

def send_whatsapp_message():
    print("Opening Whatsapp")
    os.system("start WhatsApp")
    pwt.sendwhatmsg_instantly("+919166732901","Hey, this message is sent using python")

def open_camera():
    print("opening camera")
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    status
    cv2.imwrite("photo.jpg",photo)
    cv2.imshow("photo",photo)
    cv2.waitKey()
    cv2.destroyAllWindows()

def make_video():
    print("opening your video")
    c = cv2.VideoCapture(0)
    s, p = c.read()
    s
    cv2.imshow("hii",p)
    while True:
        s, p = c.read()
        cv2.imshow("hii",p)
        if cv2.waitKey(50)==13:
            break
    cv2.destroyAllWindows()

def crop_video():
    print("opening your video")
    c = cv2.VideoCapture(0)
    s, p = c.read()
    s
    cv2.imshow("hii",p)
    while True:
        s, p = c.read()
        cv2.imshow("hii",p[100:300,200:400])
        if cv2.waitKey(50)==13:
            break
    cv2.destroyAllWindows()

def fingerprint_detection():
    print("fingerprint detector")
    model = HandDetector()
    ca = cv2.VideoCapture(0)
    st, ph = ca.read()
    hand = model.findHands(ph)
    handphoto = hand[1]
    cv2.imshow("hii",ph)
    cv2.waitKey()
    cv2.destroyAllWindows()

def face_detection():
    sap = cv2.VideoCapture(0)
    detector = FaceDetector()
    
    while True:
        success, img = sap.read()
        img, bboxs = detector.findFaces(img)
        cv2.imshow("Image",img)
        if cv2.waitKey(1)==13:
            break
    cv2.destroyAllWindows()


root = tk.Tk()
root.title("Functionality Menu")
root.configure(bg="black")  
root.attributes("-fullscreen", True)



buttons = [
    ("Open Calendar", open_calendar),
    ("Open Chrome", open_chrome),
    ("Open File Explorer", open_file_explorer),
    ("Open Command Prompt", open_command_prompt),
    ("Open Control Panel", open_control_panel),
    ("Open Task Manager", open_task_manager),
    ("Open Settings", open_settings),
    ("Distance Between Locations", calculate_distance),
    ("Send a Whatsapp Message", send_whatsapp_message),
    ("Open Camera", open_camera),
    ("Make a Video", make_video),
    ("Crop Your Video", crop_video),
    ("Fingerprint Detector", fingerprint_detection),
    ("Face Detector", face_detection)
]


for label, command in buttons:
    button = tk.Button(root, text=label, command=command, bg="maroon", fg="white")  
    button.pack(fill=tk.BOTH,padx=10,pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="maroon", fg="white") 
exit_button.pack()

    
root.mainloop()
