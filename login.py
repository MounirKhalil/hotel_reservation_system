import requests
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from hotel import HotelReservationSystem



def main():
    root=Tk()
    app=Login_window(root)
    root.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1600x700+0+0")

        self.bg=ImageTk.PhotoImage(file="login_background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="#36685f")
        frame.place(x=550,y=180,width=340,height=450)

        img1=Image.open("logo.png")
        img1=img1.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=623,y=110,width=190,height=190)

        get_start=Label(frame,text="GET STARTED",font=("arial",14,"bold"),fg="white",bg="#36685f")
        get_start.place(x=108,y=120)

        #username label login frame
        username_lbl=Label(frame,text="USERNAME :",font=("arial",11,"bold"),fg="white",bg="#36685f")
        username_lbl.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("arial",11,"bold"))
        self.txtuser.place(x=40,y=190,width=210)

        #password label login frame
        password_lbl=Label(frame,text="PASSWORD :",font=("arial",11,"bold"),fg="white",bg="#36685f")
        password_lbl.place(x=40,y=235)

        self.txtpass=ttk.Entry(frame,font=("arial",11,"bold"),show = "*")
        self.txtpass.place(x=40,y=270,width=210)


        #user icon login page
        img2=Image.open("login_icon.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=560,y=330,width=25,height=25)

        #password icon login page
        img3=Image.open("password_icon.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="#36685f",borderwidth=0)
        lblimg3.place(x=560,y=420,width=25,height=25)

        #login button
        login_btn=Button(frame,text="LOGIN",command=self.login,font=("arial",11,"bold"),bd=3,relief=RIDGE,fg="black",bg="#36685f",activeforeground="#36685f",activebackground="#36685f")
        login_btn.place(x=110,y=320,width=120,height=35)
        #register button
        register_btn=Button(frame,text="REGISTER",command=self.register_window,font=("arial",11,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="#36685f",activeforeground="#36685f",activebackground="#36685f")
        register_btn.place(x=20,y=380,width=120,height=20)
        #forget password button
        forgot_password_btn=Button(frame,text="FORGOT PASSWORD",command=self.forgot_password_window,font=("arial",11,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="#36685f",activeforeground="#36685f",activebackground="#36685f")
        forgot_password_btn.place(x=20,y=415,width=160,height=20)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("ERROR","All Feilds Required")
        else:
            data = {'email':self.txtuser.get(), 'password':self.txtpass.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/login_attempt", json = data)
            server_response = r.text #a string
            if(server_response=='<h1>Invalid username or password</h1>'):
                messagebox.showerror("ERROR","Invalid username or password")
            elif('ok' in server_response):
                contact_id = server_response.split(' ')[1]
                open_main=messagebox.askyesno("ADMIN","Login successfull, start?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelReservationSystem(self.new_window,contact_id)
                else:
                    if not open_main:
                        return

            
    


            
            
    #reset password
    def reset_password_data(self):
        if self.combo_security_q.get()=="SELECT":
            messagebox.showerror("ERROR","SELECT THE SECURITY QUESTION",parent=self.root2)
        elif self.txt_security_a.get()=="":
            messagebox.showerror("ERROR","Please enter answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("ERROR","Please enter password",parent=self.root2)
        else:
            data = {'email':self.txtuser.get(), 'security_q':self.combo_security_q.get(),'security_a':self.txt_security_a.get(),'password':self.txt_new_password.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/passw_reset", json = data)
            server_response = r.text
            if(server_response=='<h1>Please enter the correct answer</h1>'):
                messagebox.showerror("ERROR","Please enter the correct answer",parent=self.root2)
            elif(server_response=='<h1>Your password was reset, please login using new password</h1>'):
                messagebox.showinfo("INFO","Your password was reset, please login using new password",parent=self.root2)
                self.root2.destroy()


            

    #forget password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("ERROR","Enter email to reset password")
        else:
            data = {'email':self.txtuser.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/forget_passw", json = data)
            server_response = r.text
            if(server_response=='<h1>invalid username</h1>'):
                messagebox.showerror("ERROR","invalid username")
            elif(server_response=='<h1>else_case</h1>'):

                self.root2=Toplevel()
                self.root2.title("FORGOT PASSWORD")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="FORGOT PASSWORD",font=("arial",12,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="SELECT SECURITY QUESTION:",font=("arial",15,"bold"),bg="white",fg="black")
                security_q.place(x=30,y=80)

                self.combo_security_q=ttk.Combobox(self.root2,font=("arial",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("SELECT","Your Birth Place","Your Pet Name")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)

                security_a=Label(self.root2,text="SECURITY ANSWER",font=("arial",15,"bold"),bg="white",fg="black")
                security_a.place(x=50,y=150)

                self.txt_security_a = ttk.Entry(self.root2,font=("arial",15,"bold"))
                self.txt_security_a.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="NEW PASSWORD",font=("arial",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password = ttk.Entry(self.root2,font=("arial",15,"bold"),show = "*")
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="RESET",command=self.reset_password_data,font=("arial",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTER")
        self.root.geometry("1600x700+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #background image
        self.bg=ImageTk.PhotoImage(file="register_background.jpg")

        bg_lbl=Label(self.root, bg="grey")
        bg_lbl.place(x=100,y=100,relheight=0,relwidth=0)

        #image to left of register page
        self.bg1=ImageTk.PhotoImage(file="register_left_background.jpg")

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,height=550,width=470)

        #register frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl =Label(frame,text="REGISTER HERE",font=("arial",15,"bold"),fg="#36685f",bg="white")
        register_lbl.place(x=20,y=20)

        #labels

        #row1
        
        #first name
        fname=Label(frame,text="FIRST NAME :",font=("arial",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        #last name
        fname=Label(frame,text="LAST NAME :",font=("arial",15,"bold"),bg="white")
        fname.place(x=370,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",15,"bold"))
        fname_entry.place(x=370,y=130,width=250)

        #row2

        #contact number
        contact = Label(frame,text="CONTACT NO.:",font=("arial",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("arial",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        #email
        email = Label(frame,text="EMAIL:",font=("arial",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("arial",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #row3

        #security question
        security_q=Label(frame,text="SELECT SECURITY QUESTION:",font=("arial",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_security_q,font=("arial",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("SELECT","YOUR BIRTH PLACE","YOUR PET NAME")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        #security answer
        security_a=Label(frame,text="SECURITY ANSWER",font=("arial",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security_a = ttk.Entry(frame,textvariable=self.var_security_a,font=("arial",15,"bold"))
        self.txt_security_a.place(x=370,y=270,width=250)


        #row4
        
        #password
        pswd=Label(frame,text="PASSWORD",font=("arial",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("arial",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        #confirm password
        confirm_pswd=Label(frame,text="CONFIRM PASSWORD",font=("arial",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("arial",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #check button
        
        #terms and conditions
        self.var_check_btn=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check_btn,text="I AGREE THE TEARMS AND CONDITIONS.",font=("arial",11,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)

        #buttons
        
        #register button
        img = Image.open("register_button.png")
        img = img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.rgister_data,borderwidth=0,cursor="hand2",fg="white",activeforeground="white",activebackground="white",bg="white",font=("arial",15,"bold"))
        b1.place(x=30,y=460)
        #login button
        img1 = Image.open("login_button.png")
        img1 = img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2 = Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",fg="white",activeforeground="white",activebackground="white",bg="white",font=("arial",15,"bold"))
        b2.place(x=330,y=460)



    #function
    def rgister_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="SELECT" or self.var_contact.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED", parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("ERROR","PASSWORD AND CONFIRM PASSWORD MUST BE SAME", parent=self.root)
        elif self.var_check_btn.get()==0:
            messagebox.showerror("ERROR","PLEASE AGREE THE TERMS AND CONDITION", parent=self.root)
        else:
            data = {'fname':self.var_fname.get(), 'lname':self.var_lname.get(),'contact':self.var_contact.get(),'email':self.var_email.get(),'security_q':self.var_security_q.get(),'security_a':self.var_security_a.get(),'passw':self.var_pass.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/new_registration", json = data)
            server_response = r.text #a string
            if(server_response=='<h1>Successfully Registered!</h1>'):
                messagebox.showinfo("SUCCESS","REGISER SUCCESSFULLY")
            elif(server_response=='<h1>USER ALREADY EXISTS</h1>'):
                messagebox.showerror("ERROR","USER ALREADY EXISTS, PLEASE TRY ANOTHER EMAIL")


    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()


