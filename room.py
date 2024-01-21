import requests
from ast import literal_eval
from os import stat
from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self,root, contact_id='00000000'):
        self.contact_id=contact_id
        self.root=root
        self.root.title("351Hotel Reservation System")
        self.root.geometry("1121x452+234+243")

        #variables
        self.var_contact = StringVar()
        self.var_check_in = StringVar()
        self.var_check_out = StringVar()
        self.var_room_available = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days= StringVar()
        self.var_paid_tax = StringVar()
        self.var_actual_total = StringVar()
        self.var_total = StringVar()


        #title
        lbl_title = Label(self.root,text="Room Booking Details",font=("times new roman",18,"bold"),bg="#36685f",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        #logo
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((100,35),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)

        #label frame
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOMBOOKING DETAILS",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=425,height=410)

        #Labels


        #customer
        lbl_cust_contact= Label(lblFrameLeft,text="CUSTOMER CONTACT :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact = ttk.Entry(lblFrameLeft,textvariable= self.var_contact,width=20,font=("arial",11,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        self.var_contact.set(contact_id)


        #check-in button
        lblcheck_in_date = Label(lblFrameLeft,text="CHECK IN DATE : (YYYY-MM-DD)",font=("arial",10,"bold"),padx=2,pady=6)
        lblcheck_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(lblFrameLeft,textvariable=self.var_check_in,width=29,font=("arial",11,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #check out button
        lblcheck_out_date = Label(lblFrameLeft,text="CHECK OUT DATE : (YYYY-MM-DD)",font=("arial",10,"bold"),padx=2,pady=6)
        lblcheck_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(lblFrameLeft,textvariable=self.var_check_out,width=29,font=("arial",11,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        
        #available 
        lblroom_available = Label(lblFrameLeft,text="AVAILABLE ROOMS:",font=("arial",10,"bold"),padx=2,pady=6)
        lblroom_available.grid(row=4,column=0,sticky=W)


        self.combo_room_no = ttk.Combobox(lblFrameLeft,textvariable=self.var_room_available,font=("arial",10,"bold"),width=31,stat="readonly")
        #self.combo_room_no["value"]=rows
        self.combo_room_no["value"]=(" ", " ")
        self.combo_room_no.current(0)
        self.combo_room_no.grid(row=4,column=1)

        #meal
        lblroom_meal = Label(lblFrameLeft,text="MEAL :",font=("arial",10,"bold"),padx=2,pady=6)
        lblroom_meal.grid(row=5,column=0,sticky=W)

        txtroom_meal=ttk.Entry(lblFrameLeft,textvariable=self.var_meal,width=29,font=("arial",11,"bold"))
        txtroom_meal.grid(row=5,column=1)

        combo_meal=ttk.Combobox(lblFrameLeft,textvariable=self.var_meal,font=("arial",10,"bold"),width=31,state="readonly")
        combo_meal["value"]=("Breakfast","Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)

        #number of days
        lblno_of_days = Label(lblFrameLeft,text="NO. OF DAYS :",font=("arial",10,"bold"),padx=2,pady=6)
        lblno_of_days.grid(row=6,column=0,sticky=W)

        txtno_of_days=ttk.Entry(lblFrameLeft,textvariable=self.var_no_of_days,width=29,font=("arial",11,"bold"),state="readonly")
        txtno_of_days.grid(row=6,column=1)

        
        
        
        

        #paid tax
        lblno_of_days = Label(lblFrameLeft,text="PAID TAX :",font=("arial",10,"bold"),padx=2,pady=6)
        lblno_of_days.grid(row=7,column=0,sticky=W)

        txtno_of_days=ttk.Entry(lblFrameLeft,textvariable=self.var_paid_tax,width=29,font=("arial",11,"bold"),state="readonly")
        txtno_of_days.grid(row=7,column=1)

        #sub total
        lblno_of_days = Label(lblFrameLeft,text="SUB TOTAL :",font=("arial",10,"bold"),padx=2,pady=6)
        lblno_of_days.grid(row=8,column=0,sticky=W)

        txtno_of_days=ttk.Entry(lblFrameLeft,textvariable=self.var_actual_total,width=29,font=("arial",11,"bold"),state="readonly")
        txtno_of_days.grid(row=8,column=1)

        #total cost
        lbLid_number = Label(lblFrameLeft,text="TOTAL COST :",font=("arial",10,"bold"),padx=2,pady=6)
        lbLid_number.grid(row=9,column=0,sticky=W)

        txtid_number = ttk.Entry(lblFrameLeft,textvariable=self.var_total,width=29,font=("arial",11,"bold"),state="readonly")
        txtid_number.grid(row=9,column=1)

        #bill button
        btn_bill_button = Button(lblFrameLeft,text="BILL",command=self.total,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_bill_button.grid(row=10,column=0,padx=5,sticky=W)

        #refresh button
        btn_refresh_button = Button(lblFrameLeft,text="REFRESH",command=self.refresh_btn,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_refresh_button.grid(row=10,column=1,padx=5,sticky=W)

        #button
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=32)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_add.grid(row=0,column=0,padx=3)

        #btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        #btn_update.grid(row=0,column=1,padx=3)

        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_delete.grid(row=0,column=2,padx=3)

        btn_reset = Button(btn_frame,text="RESET",command=self.reset,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_reset.grid(row=0,column=3,padx=3)

        #right side image
        img3 = Image.open("room1.jpg")
        img3 = img3.resize((365,211),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=750,y=38,width=365,height=211)
        
        
        #search frame    
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=248,width=680,height=201)

        #lblsearchby = Label(table_frame,text="SEARCH BY :",font=("arial",10,"bold"),bg="#36685f",fg="white")
        #lblsearchby.grid(row=0,column=0,sticky=W,padx=4)

        #self.search_var = StringVar()

        #combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=12,state="readonly")
        #combo_search["value"]=("CONTACT","ROOM")
        #combo_search.current(0)
        #combo_search.grid(row=0,column=1,padx=4)

        #self.txt_search = StringVar()
        #entry_search = ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("arial",11,"bold"))
        #entry_search.grid(row=0,column=2,padx=4)

        #btn_search = Button(table_frame,text="SEARCH",command=self.search_data,font=("arial",10,"bold"),bg="#36685f",fg="white",width=10)
        #btn_search.grid(row=0,column=3,padx=5)

        #btn_showall = Button(table_frame,text="SHOW ALL!!",command=self.fetch_data,font=("arial",10,"bold"),bg="#36685f",fg="white",width=10)
        #btn_showall.grid(row=0,column=4,padx=5)

        #show data frame
        details_table = Label(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=34,width=674,height=148)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("CONTACT","CHECK_IN","CHECK_OUT","ROOM_AVAILABLE","MEAL"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("CONTACT",text="CONTACT")
        self.room_table.heading("CHECK_IN",text="CHECK IN")
        self.room_table.heading("CHECK_OUT",text="CHECK OUT")
        self.room_table.heading("ROOM_AVAILABLE",text="ROOM AVAILABLE")
        self.room_table.heading("MEAL",text="MEAL")


        self.room_table["show"]="headings"

        self.room_table.column("CONTACT",width=100)
        self.room_table.column("CHECK_IN",width=100)
        self.room_table.column("CHECK_OUT",width=100)
        self.room_table.column("ROOM_AVAILABLE",width=100)
        self.room_table.column("MEAL",width=100)


        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()
        self.search_data(self.contact_id)



    def add_data(self):
        if self.var_contact.get()=="" or self.var_check_in.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED!!!",parent=self.root)
        else:
            try:
                data = {'Contact':self.var_contact.get(),'check_in':self.var_check_in.get(),'check_out':self.var_check_out.get(),'Room':self.var_room_available.get(),'meal':self.var_meal.get()}
                r = requests.post(url = "http://www.epharmac.store:8081/add_data_room", json = data)
                #self.fetch_data()
                self.search_data(self.contact_id)
                messagebox.showinfo("Success","Room booked!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        data = {'test':'test'}
        r = requests.post(url = "http://www.epharmac.store:8081/fetch_data_room", json = data)
        rows = literal_eval(r.text)
        if len(rows)!= 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
         

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        #self.var_contact.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_check_out.set(row[2]),
        self.var_room_available.set(row[3]),
        self.var_meal.set(row[4])
        
        

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            data = {'Contact':self.var_contact.get(),'check_in':self.var_check_in.get(),'check_out':self.var_check_out.get(),'Room':self.var_room_available.get(),'meal':self.var_meal.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/update_room", json = data)
            #self.fetch_data()
            self.search_data(self.contact_id)
            messagebox.showinfo("Update","Room details has been updated sucessfully",parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("351Hotel Reservation System,","Do you want to remove this customers room",parent=self.root)
        if dat_Delete>0:
            data = {'Contact':self.var_contact.get(),'check_in':self.var_check_in.get(),'check_out':self.var_check_out.get(),'Room':self.var_room_available.get(),'meal':self.var_meal.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/dat_delete_room", json = data)
            #self.fetch_data()
            self.search_data(self.contact_id)
        else:
            if not dat_Delete:
                return
        
        


    def reset(self):
        self.var_contact.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
        self.var_room_available.set(""),
        self.var_meal.set(""),
        self.var_no_of_days.set(""),
        self.var_paid_tax.set(""),
        self.var_actual_total.set(""),
        self.var_total.set("")

    

    
    #search
    def search_data(self, contact_id_='00000000'):
        if contact_id_!='00000000':
            data = {'search_var':'CONTACT','txt_search':contact_id_}
            r = requests.post(url = "http://www.epharmac.store:8081/search_data_room", json = data)
            rows_fetch = literal_eval(r.text)
            if len(rows_fetch)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows_fetch:
                    self.room_table.insert("",END,values=i)
        return
                


    def total(self):
        indate = self.var_check_in.get()
        outdate = self.var_check_out.get()
        indate=datetime.strptime(indate,"%Y-%m-%d")
        outdate=datetime.strptime(outdate,"%Y-%m-%d")
        self.var_no_of_days.set(abs(outdate-indate).days)
        room__type = ""
        av=self.var_room_available.get()
        if "LUXURY" in av: room__type = "LUXURY"
        elif "DUPLEX" in av: room__type = "DUPLEX"
        elif "SINGLE" in av: room__type = "SINGLE"
        elif "DOUBLE" in av: room__type = "DOUBLE"
        
        if (self.var_meal.get()=="BreakFast" and room__type=="LUXURY"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and room__type=="SINGLE"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and room__type=="DUPLEX"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and room__type=="LUXURY"):
            q1 = float(1000)
            q2 = float(1500)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and room__type=="LUXURY"):
            q1 = float(1100)
            q2 = float(1600)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and room__type=="SINGLE"):
            q1 = float(250)
            q2 = float(600)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and room__type=="SINGLE"):
            q1 = float(300)
            q2 = float(800)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and room__type=="DUPLEX"):
            q1 = float(550)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and room__type=="DUPLEX"):
            q1 = float(500)
            q2 = float(1100)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and room__type=="DOUBLE"):
            q1 = float(400)
            q2 = float(900)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and room__type=="DOUBLE"):
            q1 = float(500)
            q2 = float(900)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and room__type=="DOUBLE"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "USD "+str("%.2f"%((q5)*0.1))
            ST = "USD "+str("%.2f"%((q5)))
            TT = "USD "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)
            

    def refresh_btn(self):
        if self.var_check_in.get()=="" or self.var_check_out.get()=="":
            messagebox.showerror("Error","Please enter checkin and checkout dates",parent=self.root)
        else:
            data = {'check_in':self.var_check_in.get(),'check_out':self.var_check_out.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/refresh_btnn", json = data)
            # continue from here
            display_r = literal_eval(r.text)
            if len(display_r)!=0:
                self.combo_room_no["value"]=display_r
                self.combo_room_no.current(0)








if __name__ == "__main__":
    root=Tk()
    Obj=Roombooking(root)
    root.mainloop()