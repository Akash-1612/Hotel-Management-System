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
from PIL import ImageTk, Image

class Customer:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x450+250+350")

        img1 = Image.open(r"C:\Users\User\Desktop\Hotel Management System\images\image2.jpg")
        img1.resize((1100,450), Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(img1)
        lblimg= Label(self.root, image=self.photoimage, bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=1100, height=450)

        self.id= StringVar()
        x= random.randint(100,1000)
        self.id.set(str(x))

        self.cust_name= StringVar()
        self.cust_gender= StringVar()
        self.cust_contact= StringVar()
        self.cust_nationality= StringVar()
        self.cust_id_type= StringVar()
        self.cust_idno= StringVar()




        heading= Label(self.root,text="Add Customer", font=("Bahnschrift light",18,BOLD),bg='#0790b9', fg="black", bd=4, relief=RIDGE)
        heading.place(x=0, y=30, width=1250, height=50)

        labelFrame= LabelFrame(self.root,text="Customer Details", font=("Bahnschrift light",15,BOLD),bg='#0790b9', fg="black", bd=4, relief=RIDGE)
        labelFrame.place(x=100, y=100, width=900, height=400)

        cid= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Customer ID", padx=2, pady=6)
        cid.grid(row=1, column=0, sticky=W)
        text=Entry(labelFrame,textvariable=self.id ,font=("century gothic", 13, BOLD),width= 29)
        text.grid(row=1, column=1, padx=15)

        cname= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Customer Name:", padx=2, pady=6)
        cname.grid(row=2, column=0, sticky=W)
        text1=Entry(labelFrame, textvariable= self.cust_name, font=("century gothic", 13, BOLD),width= 29)
        text1.grid(row=2, column=1, padx=15)


        gender= Label(labelFrame, font=("century gothic", 12, BOLD), bg='#0790b9', fg="black",text="Gender:", padx=2, pady=6)
        gender.grid(row=3, column=0, sticky=W)
        cBox= Combobox(labelFrame,textvariable = self.cust_gender, font=("century gothic", 13, BOLD),width= 27, state="readonly")
        cBox["value"]= ("Male", "Female", "Other")
        cBox.current(0)
        cBox.grid(row=3, column=1, padx=15)

        contact= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Contact Number:", padx=2, pady=6)
        contact.grid(row=4, column=0, sticky=W)
        text3=Entry(labelFrame, textvariable= self.cust_contact, font=("century gothic", 13, BOLD),width= 29)
        text3.grid(row=4, column=1, padx=15)

        nationality= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="Nationality:", padx=2, pady=6)
        nationality.grid(row=5, column=0, sticky=W)
        text4=Entry(labelFrame, textvariable= self.cust_nationality, font=("century gothic", 13, BOLD),width= 29)
        text4.grid(row=5, column=1, padx=15)

        id= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="ID Proof type:", padx=2, pady=6)
        id.grid(row=6, column=0, sticky=W)
        cBox1= Combobox(labelFrame, textvariable= self.cust_id_type, font=("century gothic", 13, BOLD),width= 27, state="readonly")
        cBox1["value"]= ("Aadhar Card", "PAN Card", "Passport")
        cBox1.current(0)
        cBox1.grid(row=6, column=1, padx=15)

        idNo= Label(labelFrame, font=("century gothic", 12, BOLD),bg='#0790b9', fg="black", text="ID Number:", padx=2, pady=6)
        idNo.grid(row=7, column=0, sticky=W)
        text5=Entry(labelFrame, textvariable= self.cust_idno, font=("century gothic", 13, BOLD),width= 29)
        text5.grid(row=7, column=1, padx=15)


        btnFrame= Frame(labelFrame, bd=4, bg='#0a8da4', relief=RIDGE)
        btnFrame.place(x=600, y=6, width=200, height=260)

        btnAdd =Button(btnFrame, text="Add",command= self.add_details ,font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=0, column=0, padx=50, pady=15)


        btnAdd =Button(btnFrame, text="Update",command= self.update_details, font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=1, column=0, padx=50, pady=15)


        btnAdd =Button(btnFrame, text="Delete",command = self.delete_details, font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=3, column=0, padx=50, pady=15)

        btnAdd =Button(btnFrame, text="Reset",command = self.reset_details, font=("century gothic", 11, BOLD),fg="white", bg="brown",width=8)
        btnAdd.grid(row=4, column=0, padx=50, pady=15)


    def add_details(self):
        if self.cust_name.get() == "" or self.cust_gender.get() == "" or self.cust_contact.get() =="" or self.cust_nationality.get() =="" or self.cust_id_type.get() =="" or  self.cust_idno.get() =="":
            messagebox.showerror("Error", "All fields are mandatory", parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s)", (
                   self.id.get(),
                   self.cust_name.get(),
                   self.cust_gender.get(),
                   self.cust_contact.get(),
                   self.cust_nationality.get(),
                   self.cust_id_type.get(),
                   self.cust_idno.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Details have been successfully added!!!", parent= self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong:{str(e)}", parent= self.root)  


    def update_details(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
        my_cursor= conn.cursor()
        my_cursor.execute("update customer set Name= %s, Gender= %s, Contact= %s, Nationality= %s, IdProof= %s, IdNo= %s where ID = %s" , (
                self.cust_name.get(),
                self.cust_gender.get(),
                self.cust_contact.get(),
                self.cust_nationality.get(),
                self.cust_id_type.get(),
                self.cust_idno.get(),
                self.id.get(),
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Update", "Details have been updates successfully !!!", parent= self.root)


    def delete_details(self):
        delete= messagebox.askyesno("Hotel Management System", "Are you sure want to delete the details?", parent= self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="t1tMp@1lyn@123", database ="hotel")
            my_cursor= conn.cursor()
            my_cursor.execute("delete from customer where ID= %s", (self.id.get(),))
        else:
            return
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Successfully deleted the data!!!")

    def reset_details(self):
        self.cust_name.set(""),
        self.cust_contact.set(""),
        self.cust_nationality.set(""),
        self.cust_idno.set("")
        x= random.randint(100,1000)
        self.id.set(str(x))





        


if __name__ == "__main__":
    root= Tk()
    obj= Customer(root)
    root.mainloop()


