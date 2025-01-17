from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Student Pannel")

        #-----------Variables-------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"D:\Face-Recognition-Attendence-System\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Student Pannel",font=("verdana",30,"bold"),bg="white",fg="black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1250,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="black")
        left_frame.place(x=20,y=10,width=600,height=450)

        # Current Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="black")
        current_course_frame.place(x=10,y=5,width=580,height=130)

        #label Department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="black")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=13,font=("verdana",11,"bold"),state="readonly")
        dep_combo["values"]=("------","digital economy and e-commerce","Computer Science","BSENG","BSPHY","BSMATH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        # -----------------------------------------------------

        #label Course
        cou_label=Label(current_course_frame,text="Course",font=("verdana",12,"bold"),bg="white",fg="black")
        cou_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=13,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("------","SE","CE","EL","AD","DA")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        #-------------------------------------------------------------

        #label Year
        year_label=Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="black")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=13,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("-----","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #-----------------------------------------------------------------

        #label Semester 
        year_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="black")
        year_label.grid(row=1,column=2,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=13,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("------","Semester-1","Semester-2","Semester-Summer")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",12,"bold"),fg="black")
        class_Student_frame.place(x=10,y=140,width=580,height=230)

        #Student id
        studentId_label = Label(class_Student_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="black",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=12,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=12,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Class Didvision
        student_div_label = Label(class_Student_frame,text="Class Division:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=11,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("-----","Morning","Afternoon")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=12,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=11,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("-----","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=12,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=12,font=("verdana",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=12,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=12,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Tutor Name:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=12,font=("verdana",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #=============Button Frame=======
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=380,width=580,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=6,font=("verdana",12,"bold"),fg="white",bg="blue")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="blue")
        update_btn.grid(row=0,column=1)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="blue")
        del_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="blue")
        reset_btn.grid(row=0,column=3)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=9,font=("verdana",12,"bold"),fg="white",bg="blue")
        take_photo_btn.grid(row=0,column=4)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Photo",width=11,font=("verdana",12,"bold"),fg="white",bg="blue")
        update_photo_btn.grid(row=0,column=5)


        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="black")
        right_frame.place(x=630,y=10,width=600,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="black")
        search_frame.place(x=10,y=5,width=580,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="black",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=10,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="blue")
        search_btn.grid(row=0,column=3,padx=2)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="blue")
        showAll_btn.grid(row=0,column=4)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=580,height=350)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame, column=("Student_ID", "Name", "Department", "Cource", "Year", "Semester", "Division", "Gender", "DOB", "Mobile_No", "Address", "Roll_No", "Email", "Teacher_Name", "PhotoSample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Student_ID", text="Student_ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Cource", text="Cource")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Mobile_No", text="Mobile_No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Roll_No", text="Roll_No")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Teacher_Name", text="Teacher_Name")
        self.student_table.heading("PhotoSample", text="PhotoSample")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.column("Student_ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Department", width=100)
        self.student_table.column("Cource", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Mobile_No", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Roll_No", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Teacher_Name", width=100)
        self.student_table.column("PhotoSample", width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student (Student_ID, Name, Department, Cource, Year, Semester, Division, Gender, DOB, Mobile_No, Address, Roll_No, Email, Teacher_Name, PhotoSample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Name=%s,Department=%s,Cource=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",(
                            self.var_std_name.get(),
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_div.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_mob.get(),
                            self.var_address.get(),
                            self.var_roll.get(),
                            self.var_email.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()   
                            ))
                    messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    
    #==============================Delete Function=========================================
    def delete_data(self):  # Move this method into the class
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                    my_cursor = conn.cursor()
                    sql="DELETE from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("-----"),
        self.var_course.set("-----"),
        self.var_year.set("-----"),
        self.var_semester.set("-----"),
        self.var_div.set("-----"),
        self.var_gender.set("-----"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID, Name, Department, Cource, Year, Semester, Division, Gender, DOB, Mobile_No, Address, Roll_No, Email, Teacher_Name, PhotoSample FROM student where Roll_No='" + str(self.var_search.get()) + "'"
                my_cursor.execute(sql)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror("Error", "Data Not Found", parent=self.root)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="do-an")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Name=%s,Department=%s,Cource=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                # Xác định hàm face_cropped để cắt khuôn mặt từ hình ảnh
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    face_cropped = None
                    for(x, y, w, h) in faces:  
                        face_cropped = img[y:y+h, x:x+w] 
                    return face_cropped

                # Load pre-trained face detection model từ OpenCV
                

                # Mở camera để chụp ảnh
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data_img/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        org = (50, 50)  # Tọa độ org
                        cv2.putText(face, str(img_id), org, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)  # Thêm văn bản lên ảnh
                        cv2.imshow("Cropped Face", face)

                    # Đóng cửa sổ hiển thịhình ảnh sau khi nhấn phím Enter hoặc sau khi chụp đủ 100 ảnh
                    if cv2.waitKey(1) == 12 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result", "Generating dataset completed !!!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

  
# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
