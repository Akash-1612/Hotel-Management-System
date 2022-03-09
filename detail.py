from configparser import ParsingError
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkinter.ttk import Entry
import mysql
import mysql.connector
import random
from tkinter import messagebox
from PIL import ImageTk, Image

class Details:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x450+250+350")

        img1 = Image.open(r"C:\Users\User\Desktop\Hotel Management System\images\image2.jpg")
        img1.resize((1500,800), Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(img1)
        lblimg= Label(self.root, image=self.photoimage, bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=1100, height=450)

        self.search= StringVar()

        heading= Label(self.root,text="View Details", font=("Bahnschrift light",18,BOLD),bg='#0790b9', fg="black", bd=4, relief=RIDGE)
        heading.place(x=0, y=30, width=1250, height=50)

        labelFrame= LabelFrame(self.root,text="Customer & Bookings Details", font=("Bahnschrift light",15,BOLD),bg='#0790b9', fg="black", bd=4, relief=RIDGE)
        labelFrame.place(x=100, y=100, width=900, height=400)

        search= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Enter Customer ID", padx=2, pady=6)
        search.grid(row=1, column=0, sticky=W)
        text=Entry(labelFrame,textvariable=self.search,font=("century gothic", 13, BOLD),width= 29)
        text.grid(row=1, column=1, padx=15)

        searchButton =Button(labelFrame,text="Search", command= self.searchDetails, font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        searchButton.grid(row=1, column=2, padx= 15)

        viewAll =Button(labelFrame, text="View All", command=self.searchAll, font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        viewAll.grid(row=1, column=3, padx= 15)

        tableFrame=Frame(labelFrame, bd=4, relief=RIDGE)
        tableFrame.place(x=10,y=50, width=900, height=250)

        scroll=ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scroll.pack(side=BOTTOM, fill=X)
    
        self.details= Treeview(tableFrame, xscrollcommand=scroll.set,  columns=("ID","Name","Gender","Contact", "Nationality","IdProof","IdProofNo","BookingID", "CheckInDate","CheckOutDate","RoomType"))

        scroll.config(command=self.details.xview)

        self.details.heading("ID",text="ID")
        self.details.heading("Name",text="Name")
        self.details.heading("Gender",text="Gender")
        self.details.heading("Contact",text="Contact")
        self.details.heading("Nationality",text="Nationality")
        self.details.heading("IdProof",text="IdProof")
        self.details.heading("IdProofNo",text="IdProofNo")
        self.details.heading("BookingID",text="BookingID")
        self.details.heading("CheckInDate",text="CheckInDate")
        self.details.heading("CheckOutDate",text="CheckOutDate")
        self.details.heading("RoomType",text="RoomType")

        self.details["show"]="headings"
        self.details.pack(fill=BOTH, expand=1)

    def searchDetails(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
        my_cursor= conn.cursor()
        my_cursor.execute("select distinct * from customer inner join room on customer.ID = room.CustomerID where customer.ID = %s", (self.search.get(),))
        rows= my_cursor.fetchall()
        if len(rows) != 0:
            for i in rows:
                self.details.insert("", END, values=i)
        conn.commit()
        conn.close()

    def searchAll(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
        my_cursor= conn.cursor()
        my_cursor.execute("select distinct * from customer inner join room on customer.ID = room.CustomerID")
        rows= my_cursor.fetchall()
        if len(rows) != 0:
            for i in rows:
                self.details.insert("", END, values=i)
        conn.commit()
        conn.close()

        


if __name__ == "__main__":
    root= Tk()
    obj= Details(root)
    root.mainloop()