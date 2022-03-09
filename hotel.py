from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from customer import Customer
from room import Room
from detail import Details

class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1900x1000")


        img1 = Image.open(r"C:\Users\User\Desktop\Hotel Management System\images\image2.jpg")
        img1.resize((1900,1000), Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(img1)
        lblimg= Label(self.root, image=self.photoimage, bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=1900, height=1000)


        heading= Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("Bahnschrift light",40,font.BOLD),bg= '#0790b9', fg="black", bd=7, relief=RIDGE)
        heading.pack(pady=80)

        my_frame= Frame(self.root,bd=4, bg= '#0790b9',relief=RIDGE)
        my_frame.pack(pady=20)

        button1= Button(my_frame,text="Customer Registration",command=self.custDetails, font=("century gothic", 14, font.BOLD), fg="white", bg= '#064698', bd=4, relief=RIDGE)
        button1.grid(row=0, column=0, padx=30)

        button1= Button(my_frame,text="Bookings", command = self.roomDetails, font=("century gothic", 14, font.BOLD), fg="white", bg= '#064698', bd=4, relief=RIDGE)
        button1.grid(row=0, column=1, padx=30)

        button1= Button(my_frame,text="Details", command=self.viewDetails, font=("century gothic", 14, font.BOLD), fg="white", bg= '#064698', bd=4, relief=RIDGE)
        button1.grid(row=0, column=2, padx=30)

 
    def custDetails(self):
        self.window1= Toplevel(self.root)
        self.app= Customer(self.window1)
   
    def roomDetails(self):
        self.window2= Toplevel(self.root)
        self.app= Room(self.window2)

    def viewDetails(self):
        self.window3= Toplevel(self.root)
        self.app= Details(self.window3)



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
    

