from configparser import ParsingError
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Combobox
from tkinter.ttk import Entry
import mysql
import mysql.connector
import random
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk, Image


class Room:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x450+250+350")

        img1 = Image.open(r"C:\Users\User\Desktop\Hotel Management System\images\image2.jpg")
        img1.resize((1500,800), Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(img1)
        lblimg= Label(self.root, image=self.photoimage, bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=1100, height=450)


        self.id= StringVar()
        self.checkInDate= StringVar()
        self.checkOutDate= StringVar()
        self.roomType= StringVar()
          
        heading= Label(self.root,text="Book A Room!", font=("Bahnschrift light",18,BOLD),bg='#0790b9', fg="black", bd=4, relief=RIDGE)
        heading.place(x=0, y=30, width=1250, height=50)

        labelFrame= LabelFrame(self.root,text="Customer Details", font=("Bahnschrift light",15,BOLD),bg='#0790b9', fg="black", bd=4, relief=RIDGE)
        labelFrame.place(x=100, y=100, width=900, height=400)

        cid= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Customer ID", padx=2, pady=6)
        cid.grid(row=1, column=0, sticky=W)
        text=Entry(labelFrame ,textvariable= self.id, font=("century gothic", 13, BOLD),width= 29)
        text.grid(row=1, column=1, padx=15)

        checkIn= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Check In Date", padx=2, pady=6)
        checkIn.grid(row=2, column=0, sticky=W)
        text1=DateEntry(labelFrame ,textvariable= self.checkInDate, font=("century gothic", 13, BOLD),width= 27)
        text1.grid(row=2, column=1, padx=15)

        checkOut= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Check Out Date", padx=2, pady=6)
        checkOut.grid(row=3, column=0, sticky=W)
        text2=DateEntry(labelFrame , textvariable= self.checkOutDate, font=("century gothic", 13, BOLD),width= 27)
        text2.grid(row=3, column=1, padx=15)

        roomType= Label(labelFrame, font=("century gothic", 12, BOLD), bg='#0790b9', fg="black",text="Room Type:", padx=2, pady=6)
        roomType.grid(row=4, column=0, sticky=W)
        cBox= Combobox(labelFrame,textvariable= self.roomType, font=("century gothic", 13, BOLD),width= 27, state="readonly")
        cBox["value"]= ("Single", "Double")
        cBox.current(0)
        cBox.grid(row=4, column=1, padx=15)
    
        btnFrame= Frame(labelFrame, bd=4,bg='#0a8da4', relief=RIDGE)
        btnFrame.place(x=600, y=6, width=200, height=260)

        btnAdd =Button(btnFrame,command=self.bookRoom, text="Book",font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=0, column=0, padx=50, pady=15)
   
        btnAdd =Button(btnFrame,command= self.updateBookings, text="Update", font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=1, column=0, padx=50, pady=15)


        btnAdd =Button(btnFrame,command= self.deleteBokings, text="Delete",font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=3, column=0, padx=50, pady=15)

        btnAdd =Button(btnFrame,command=self.reset_details, text="Reset",font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=4, column=0, padx=50, pady=15)

    def bookRoom(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
        my_cursor= conn.cursor()
        my_cursor1= conn.cursor()
        my_cursor.execute("select * from customer where ID= %s", (self.id.get(),))
        self.row= my_cursor.fetchall()
        if len(self.row) ==0:
            messagebox.showerror("Error", "No Customer with this ID found! Please move to Customer section to add customer details")
        else:
            my_cursor1.execute("insert into room values(%s,%s,%s,%s)", (
                self.id.get(),
                self.checkInDate.get(),
                self.checkOutDate.get(),
                self.roomType.get() 
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess", "Your room has been done successfully !!", parent= self.root)
    
    def updateBookings(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
        my_cursor= conn.cursor()
        my_cursor.execute("update room set CustomerID= %s, CheckInDate= %s, CheckOutDate= %s, RoomType= %s" , (
                self.id.get(),
                self.checkInDate.get(),
                self.checkOutDate.get(),
                self.roomType.get() 
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Update", "Details have been updates successfully !!!", parent= self.root)
    
    def deleteBokings(self):
        delete= messagebox.askyesno("Hotel Management System", "Are you sure want to delete the details?", parent= self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
            my_cursor= conn.cursor()
            my_cursor.execute("delete from room where CustomerID= %s", (self.id.get(),))
        else:
            return
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Successfully deleted the data!!!")
    
    def reset_details(self):
        self.id.set(""),
        self.roomType.set(""),
        self.noOfDays.set(""),


if __name__ == "__main__":
    root= Tk()
    obj= Room(root)
    root.mainloop()