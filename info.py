from os import stat
from tkinter import*
from PIL import Image, ImageTk 


class Info_details:
    def __init__(self,root):
        self.root=root
        self.root.title("351Hotel Reservation System")
        self.root.geometry("1121x452+234+243")

        #Title
        lbl_title = Label(self.root,text="Staff Information",font=("times new roman",18,"bold"),bg="#36685f",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        #logo
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((100,35),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)

        #info
        img3 = Image.open("REPORTS.PNG")
        img3 = img3.resize((800,517),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=35,width=1120,height=418)






if __name__ == "__main__":
    root=Tk()
    Obj=Info_details(root)
    root.mainloop()