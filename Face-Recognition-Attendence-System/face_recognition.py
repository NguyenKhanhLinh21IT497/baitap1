from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
from tkinter import messagebox
from datetime import datetime
import threading

class Face_Recognition:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Page")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)

           # Khởi tạo stop_event
        self.stop_event = threading.Event()
        
        # self.root = root
        # self.root.geometry("1366x768+0+0")
        # self.root.title("Face Recognition Panel")

        # # Phần giao diện đồ họa
        # img = Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\bg-img.jpg")
        # img = img.resize((1366, 130), Image.LANCZOS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lb1 = Label(self.root, image=self.photoimg)
        # f_lb1.place(x=0, y=0, width=1366, height=130)

        # bg1 = Image.open(r"Images_GUI\bg2.jpg")
        # bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        # self.photobg1 = ImageTk.PhotoImage(bg1)

        # bg_img = Label(self.root, image=self.photobg1)
        # bg_img.place(x=0, y=0, width=1366, height=768)

        # title_lb1 = Label( text="Face Recognition Page", font=("verdana", 30, "bold"), bg="white", fg="black")
        # title_lb1.place(x=0, y=200, width=1366, height=60)

        # std_img_btn = Image.open(r"Images_GUI\train-top.jpg")
        # std_img_btn = std_img_btn.resize((1300, 350), Image.LANCZOS)
        # self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button( command=self.face_recog, image=self.std_img1, cursor="hand2")
        # std_b1.place(x=0, y=250, width=1300, height=360)

        # std_b1_1 = Button( command=self.face_recog, text="Face Detector", cursor="hand2", font=("tahoma", 15, "bold"), bg="blue", fg="white")
        # std_b1_1.place(x=0, y=600, width=1300, height=40)

  

    def mark_attendance(self, i, r, n, d):
        n = ''.join([c for c in n if ord(c) < 128])
        d = ''.join([c for c in d if ord(c) < 128])

        with open("attendance.csv", "r+", newline="\n", encoding="latin-1") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if (i not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Department from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarCascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        video_cap = cv2.VideoCapture(0)

        while not self.stop_event.is_set():
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1) == 12:  
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
