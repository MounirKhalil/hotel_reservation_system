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

class Detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("351Hotel Reservation System")
        self.root.geometry("1121x452+234+243")

        #title
        lbl_title = Label(self.root,text="Roombooking Details",font=("times new roman",18,"bold"),bg="#36685f",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        #logo
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((100,35),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)

        #frame
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add New Room",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=460,height=350)

        #Floor
        lbl_floor= Label(lblFrameLeft,text="FLOOR ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_floor = ttk.Entry(lblFrameLeft,textvariable=self.var_floor,width=20,font=("arial",11,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)


        #room number
        lbl_room_no= Label(lblFrameLeft,text="ROOM NO. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_room_no.grid(row=1,column=0,sticky=W)
        
        self.var_room_no=StringVar()
        entry_room_no = ttk.Entry(lblFrameLeft,textvariable=self.var_room_no,width=20,font=("arial",11,"bold"))
        entry_room_no.grid(row=1,column=1,sticky=W)

        #room type
        lbl_room_TYPE= Label(lblFrameLeft,text="ROOM TYPE. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_room_TYPE.grid(row=2,column=0,sticky=W)
        
        self.var_room_type=StringVar()
        

        combo_gender=ttk.Combobox(lblFrameLeft,textvariable=self.var_room_type,font=("arial",10,"bold"),width=31,state="readonly")
        combo_gender["value"]=("LUXURY","DUPLEX","SINGLE","DOUBLE")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)
        
        

        #buttons
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=290,width=412,height=32)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_add.grid(row=0,column=0,padx=3)

        btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_update.grid(row=0,column=1,padx=3)

        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_delete.grid(row=0,column=2,padx=3)

        btn_reset = Button(btn_frame,text="RESET",command=self.reset,font=("arial",10,"bold"),bg="#36685f",fg="#36685f",width=10)
        btn_reset.grid(row=0,column=3,padx=3)

        #search frame       
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=500,y=40,width=600,height=350)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,columns=("FLOOR","ROOM_NO","ROOM_TYPE"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("FLOOR",text="FLOOR")
        self.room_table.heading("ROOM_NO",text="ROOM NO.")
        self.room_table.heading("ROOM_TYPE",text="ROOM TYPE")
        

        self.room_table["show"]="headings"

        self.room_table.column("FLOOR",width=80)
        self.room_table.column("ROOM_NO",width=80)
        self.room_table.column("ROOM_TYPE",width=80)
        

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    #add data func
    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="" or self.var_room_no.get()=="":
            messagebox.showerror("Error","All Feilds Are Required",parent=self.root)
        else:
            f_floor='Floor'+self.var_floor.get()
            data = {'Floor':f_floor,'RoomNo':self.var_room_no.get(),'RoomType':self.var_room_type.get(), 'avFrom':'2022-01-01', 'avTo':'3000-12-31'}
            r = requests.post(url = "http://www.epharmac.store:8081/add_data_det", json = data)
            self.fetch_data()
            messagebox.showinfo("Success","New Room added",parent=self.root)


    #fetch data from database func
    def fetch_data(self):
        data = {'test':'test'}
        r = requests.post(url = "http://www.epharmac.store:8081/fetch_data_det", json = data)
        rows = literal_eval(r.text)
        if len(rows)!= 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)


    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2])

    #update info func
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            data = {'Floor':self.var_floor.get(),'RoomType':self.var_room_type.get(),'RoomNo':self.var_room_no.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/update_det", json = data)
            self.fetch_data()
            messagebox.showinfo("Update","New Room details has been updated sucessfully",parent=self.root)
            
    #delete info func
    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("351Hotel Reservation System,","Do you want to remove this room detail",parent=self.root)
        if dat_Delete>0:
            data = {'RoomNo':self.var_room_no.get()}
            r = requests.post(url = "http://www.epharmac.store:8081/dat_delete_det", json = data)
        else:
            if not dat_Delete:
                return
        self.fetch_data()
        

    def reset(self):
        self.var_floor.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set("")





if __name__ == "__main__":
    root=Tk()
    Obj=Detailsroom(root)
    root.mainloop()
