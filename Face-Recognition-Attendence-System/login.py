import tkinter
from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
from train import Train
import mysql.connector
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import ttk
import os

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\Face-Recognition-Attendence-System\Images_GUI\bg3.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="white")
        frame1.place(x=500,y=100,width=340,height=450)

        img1=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\log1.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="white")
        lb1img1.place(x=550,y=125, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=170,y=55)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",13,"bold"))
        self.txtuser.place(x=33,y=190,width=270,height=30)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",13,"bold"),fg="black",bg="white")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270,height=30)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",13,"bold"),bd=0,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=40)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.register_window,text="Register",font=("times new roman",13,"bold"),bd=0,relief=RIDGE,fg="white",bg="red",activeforeground="orange",activebackground="black")
        loginbtn.place(x=33,y=370,width=270,height=40)


    #  THis function is for open register window
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()

    def register(self):
        messagebox.showinfo("Register", "Register window is under construction")


#=================== Register===================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\Face-Recognition-Attendence-System\Images_GUI\bg3.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=200,y=40,width=900,height=580)

        get_str = Label(frame,text="Register Page ",font=("times new roman",30,"bold"),fg="black",bg="#F2F2F2")
        get_str.place(x=350,y=70)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        fname.place(x=100,y=180)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=205,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        lname.place(x=100,y=250)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=275,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        cnum.place(x=530,y=180)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=205,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        email.place(x=530,y=250)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=275,width=270)

        
        
        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        pwd.place(x=100,y=330)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=355,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        cpwd.place(x=530,y=330)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=355,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="black",bg="#F2F2F2")
        checkbtn.place(x=100,y=410,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.register,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="blue",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=470,width=310,height=40)

        # Creating Button Login
        loginbtn=Button(frame,command=self.return_login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="red",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=500,y=470,width=310,height=40)




    def register(self):
        if self.var_fname.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                my_cursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    my_cursor.execute("insert into regteach values(%s,%s,%s,%s,%s)",(
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_cnum.get(),
                            self.var_email.get(),
                            self.var_pwd.get()
                        ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def return_login(self):
        self.root.destroy()


# =====================main program Face deteion system====================

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
        title_lb1 = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM PAGE",font=("verdana",30,"bold"),bg="white",fg="BLACK")
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
    app=Login(root)
    root.mainloop()