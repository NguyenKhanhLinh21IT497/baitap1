import tkinter
from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
import mysql.connector
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import ttk
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\stu.jpg")
        img=img.resize((1366,270),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=270)

        # backgorund image 
        bg1=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\bg-img.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=270,width=1360,height=768)


        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM PAGE",font=("verdana",30,"bold"),bg="white",fg="black")
        title_lb1.place(x=0,y=0,width=1360,height=60)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\detect-face.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\f_det.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\attendance.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        att_b1_1.place(x=710,y=280,width=180,height=45)


        tra_img_btn=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\train-data.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=940,y=100,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        tra_b1_1.place(x=940,y=280,width=180,height=45)

       

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")

#============= Exit button=============        



# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
   

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
