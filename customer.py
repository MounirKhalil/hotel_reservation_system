import requests
from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
from tkinter import messagebox
from ast import literal_eval





class Cust_Win:
    def __init__(self,root, contact_id='00000000'):
        self.root=root
        self.root.title("351Hotel Reservation System")
        self.root.geometry("1121x452+234+243")


        #variables
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_cust_middle = StringVar()
        self.var_cust_gender = StringVar()
        self.var_cust_post = StringVar()
        self.var_cust_mobile = StringVar()
        self.var_cust_email = StringVar()
        self.var_cust_nationality = StringVar()
        self.var_cust_id_proff = StringVar()
        self.var_cust_id_number = StringVar()
        self.var_cust_address = StringVar()


        #Title
        lbl_title = Label(self.root,text="Add Customer Details",font=("times new roman",18,"bold"),bg="#36685f",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        #logo
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((100,35),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)


        #Frame
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=425,height=410)


        #labels
        #reference number
        lbl_cust_ref = Label(lblFrameLeft,text="Customer Reference :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)    
        entry_ref = ttk.Entry(lblFrameLeft,textvariable=self.var_ref,width=29,font=("arial",11,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #customer name
        lbl_cust_name = Label(lblFrameLeft,text="Customer Name :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        entry_name = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_name,width=29,font=("arial",11,"bold"))
        entry_name.grid(row=1,column=1)


        #middle name
        lbl_cust_mname = Label(lblFrameLeft,text="Middle Name :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)
        entry_mname = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_middle,width=29,font=("arial",11,"bold"))
        entry_mname.grid(row=2,column=1)


        #Gender
        lbl_gender = Label(lblFrameLeft,font=("arial",10,"bold"),text="Gender :",padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(lblFrameLeft,textvariable=self.var_cust_gender,font=("arial",10,"bold"),width=31,state="readonly")
        combo_gender["value"]=("MALE","FEMALE")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        ########### POST CODE ###############
        # lbl_cust_post = Label(lblFrameLeft,text="POST CODE :",font=("arial",10,"bold"),padx=2,pady=6)
        # lbl_cust_post.grid(row=4,column=0,sticky=W)
        
        # entry_post = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_post,width=29,font=("arial",11,"bold"))
        # entry_post.grid(row=4,column=1)

        #contact number
        lbl_cust_mob = Label(lblFrameLeft,text="Contact Number:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_mob.grid(row=5,column=0,sticky=W)
        entry_mob = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_mobile,width=29,font=("arial",11,"bold"))
        entry_mob.grid(row=5,column=1)
        self.var_cust_mobile.set(contact_id)

        #email
        lbl_cust_email = Label(lblFrameLeft,text="Email :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=6,column=0,sticky=W)
        entry_email = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_email,width=29,font=("arial",11,"bold"))
        entry_email.grid(row=6,column=1)

        #nationality
        lblNationality = Label(lblFrameLeft,font=("arial",10,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(lblFrameLeft,textvariable=self.var_cust_nationality,font=("arial",10,"bold"),width=31,state="readonly")
        combo_nationality["value"]=("Lebanese","American","Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        #id 
        lblIdproff = Label(lblFrameLeft,font=("arial",10,"bold"),text="ID Type :",padx=2,pady=6)
        lblIdproff.grid(row=8,column=0,sticky=W)
        combo_idproff=ttk.Combobox(lblFrameLeft,textvariable=self.var_cust_id_proff,font=("arial",10,"bold"),width=31,state="readonly")
        combo_idproff["value"]=("Personal Identification","Passport","Driving License")
        combo_idproff.current(0)
        combo_idproff.grid(row=8,column=1)

        #id number
        lbl_cust_idno = Label(lblFrameLeft,text="ID Number :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_idno.grid(row=9,column=0,sticky=W)
        entry_idno = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_id_number,width=29,font=("arial",11,"bold"))
        entry_idno.grid(row=9,column=1)

        #address
        lbl_cust_addr = Label(lblFrameLeft,text="Address :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_addr.grid(row=10,column=0,sticky=W)
        entry_addr = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_address,width=29,font=("arial",11,"bold"))
        entry_addr.grid(row=10,column=1)

        #buttons
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=352,width=412,height=32)

        #add
        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="white",fg="#36685f",width=10)
        btn_add.grid(row=0,column=0,padx=3)
        #update
        btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="white",fg="#36685f",width=10)
        btn_update.grid(row=0,column=1,padx=3)
        #delete
        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="white",fg="#36685f",width=10)
        btn_delete.grid(row=0,column=2,padx=3)
        #reset
        btn_reset = Button(btn_frame,text="RESET",command=self.data_reset,font=("arial",10,"bold"),bg="white",fg="#36685f",width=10)
        btn_reset.grid(row=0,column=3,padx=3)



        #search frame      
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Search and View Details",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=40,width=680,height=410)

        lblsearchby = Label(table_frame,text="Search By :",font=("arial",10,"bold"),bg="#36685f",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=4)

        self.search_var = StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=12,state="readonly")
        combo_search["value"]=("Mobile","Reference Number")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=4)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("arial",11,"bold"))
        entry_search.grid(row=0,column=2,padx=4)
        
        #Search
        btn_search = Button(table_frame,text="Search",command=self.search_data,font=("arial",10,"bold"),bg="black",fg="#36685f",width=10)
        btn_search.grid(row=0,column=3,padx=5)
        btn_showall = Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="#36685f",width=10)
        btn_showall.grid(row=0,column=4,padx=5)



        #Data table
        details_table = Label(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=34,width=674,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_table=ttk.Treeview(details_table,columns=("REF","NAME","MIDDLE","GENDER","POSTCODE","MOBILE","EMAIL","NATIONALITY","IDPROOF","IDNUMBER","ADDRESS"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_details_table.xview)
        Scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("REF",text="REF")
        self.Cust_details_table.heading("NAME",text="NAME")
        self.Cust_details_table.heading("MIDDLE",text="MIDDLE")
        self.Cust_details_table.heading("GENDER",text="GENDER")
        self.Cust_details_table.heading("POSTCODE",text="POSTCODE")
        self.Cust_details_table.heading("MOBILE",text="MOBILE")
        self.Cust_details_table.heading("EMAIL",text="EMAIL")
        self.Cust_details_table.heading("NATIONALITY",text="NATIONALITY")
        self.Cust_details_table.heading("IDPROOF",text="IDPROOF")
        self.Cust_details_table.heading("IDNUMBER",text="IDNUMBER")
        self.Cust_details_table.heading("ADDRESS",text="ADDRESS")

        self.Cust_details_table["show"]="headings"

        self.Cust_details_table.column("REF",width=100)
        self.Cust_details_table.column("NAME",width=100)
        self.Cust_details_table.column("MIDDLE",width=100)
        self.Cust_details_table.column("GENDER",width=100)
        self.Cust_details_table.column("POSTCODE",width=100)
        self.Cust_details_table.column("MOBILE",width=100)
        self.Cust_details_table.column("EMAIL",width=100)
        self.Cust_details_table.column("NATIONALITY",width=100)
        self.Cust_details_table.column("IDPROOF",width=100)
        self.Cust_details_table.column("IDNUMBER",width=100)
        self.Cust_details_table.column("ADDRESS",width=100)

        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()





    def add_data(self):
        if self.var_cust_mobile.get()=="" or self.var_cust_middle.get()=="":
            messagebox.showerror("Error","All Feilds are Required",parent=self.root)
        else:
            try:
                data = {'Ref':self.var_ref.get(),'Name':self.var_cust_name.get(),'Middle':self.var_cust_middle.get(),'Gender':self.var_cust_gender.get(),'PostCode':'-1','Mobile':self.var_cust_mobile.get(),'Email':self.var_cust_email.get(),'Nationality':self.var_cust_nationality.get(),'Idproof':self.var_cust_id_proff.get(),'Idnumber':self.var_cust_id_number.get(),'Address':self.var_cust_address.get()}
                r = requests.post(url = "http://www.epharmac.store:8081/add_data", json = data)
                
                ####self.fetch_data()####
                rows = literal_eval(r.text)
                if len(rows)!= 0:
                    self.Cust_details_table.delete(*self.Cust_details_table.get_children())
                    for i in rows:
                        self.Cust_details_table.insert("",END,values=i)
                ####self.fetch_data()####

                messagebox.showinfo("Success","Customer has been added",parent=self.root)
                

            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)



    def fetch_data(self):
        data = {'test':'test'}
        r = requests.post(url = "http://www.epharmac.store:8081/fetch_data", json = data)
        rows = literal_eval(r.text)
        if len(rows)!= 0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)




    def get_cursor(self,event=""):
        cursor_row = self.Cust_details_table.focus()
        content = self.Cust_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_middle.set(row[2]),
        self.var_cust_gender.set(row[3]),
        self.var_cust_post.set(row[4]),
        self.var_cust_mobile.set(row[5]),
        self.var_cust_email.set(row[6]),
        self.var_cust_nationality.set(row[7]),
        self.var_cust_id_proff.set(row[8]),
        self.var_cust_id_number.set(row[9]),
        self.var_cust_address.set(row[10])
        
    #update info button
    def update(self):
        if self.var_cust_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            data = {'Ref':self.var_ref.get(),'Name':self.var_cust_name.get(),'Middle':self.var_cust_middle.get(),'Gender':self.var_cust_gender.get(),'PostCode':'-1','Mobile':self.var_cust_mobile.get(),'Email':self.var_cust_email.get(),'Nationality':self.var_cust_nationality.get(),'Idproof':self.var_cust_id_proff.get(),'Idnumber':self.var_cust_id_number.get(),'Address':self.var_cust_address.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/update", json = data)
            
            ####self.fetch_data()####
            rows = literal_eval(r.text)
            if len(rows)!= 0:
                self.Cust_details_table.delete(*self.Cust_details_table.get_children())
                for i in rows:
                    self.Cust_details_table.insert("",END,values=i)
            ####self.fetch_data()####

            messagebox.showinfo("Update","Customer details has been updated sucessfully",parent=self.root)
            
    #delete button
    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("351Hotel Reservation System,","Do you want to delete this customer",parent=self.root)
        if dat_Delete>0:
            data = {'Ref':self.var_ref.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/dat_delete", json = data)
            messagebox.showinfo("Update","Customer details have been deleted sucessfully",parent=self.root)
        else:
            if not dat_Delete:
                return
    
        ####self.fetch_data()####
        rows = literal_eval(r.text)
        if len(rows)!= 0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
        ####self.fetch_data()####
        

    #reset button
    def data_reset(self):

        self.var_cust_name.set(""),
        self.var_cust_middle.set(""),
        self.var_cust_post.set(""),
        self.var_cust_mobile.set(""),
        self.var_cust_email.set(""),
        self.var_cust_id_number.set(""),
        self.var_cust_address.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

    #search
    def search_data(self):
        
        data = {'search_var':self.search_var.get(),'txt_search':self.txt_search.get()}
        r = requests.post(url = "http://www.epharmac.store:8081/search_data", json = data)
        messagebox.showinfo("Update","Customer details has been updated sucessfully",parent=self.root)

        rows_fetch = literal_eval(r.text)
        
        if len(rows_fetch)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows_fetch:
                self.Cust_details_table.insert("",END,values=i)
            
         
            

        

if __name__ == "__main__":
    root=Tk()
    Obj=Cust_Win(root)
    root.mainloop()