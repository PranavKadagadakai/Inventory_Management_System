from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
import os
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x775+0+0")
        self.root.title("Inventory Management System | Developed by Fingers")
        #self.root.config(bg="grey")

        # Title
            #image resizing
        self.title_icon=Image.open("image/inventory_10951884.png")
        self.title_icon=self.title_icon.resize((50,50),Image.LANCZOS)
        self.title_icon=ImageTk.PhotoImage(self.title_icon)

        title=Label(self.root,text="Inventory Management System",image=self.title_icon,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        # logout button
        logout=Button(self.root,text="Logout", command=self.logout ,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1350,y=10,height=50,width=150)

        # sub title
        self.clock = Label(self.root, text="Welcome to Inventory Management System\t\tDate: DD-MM-YYYY\t\tTime: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock.place(x=0,y=70,relwidth=1,height=30)


        #Left Menu Frame
            # Left Menu Icon resize
        self.Frame_icon=Image.open("image/Left_frame_icon.png")
        self.Frame_icon=self.Frame_icon.resize((200,200),Image.LANCZOS)
        self.Frame_icon=ImageTk.PhotoImage(self.Frame_icon)

        leftFrame=Frame(self.root,bd=2,relief=RIDGE,bg="#eeeee4")
        leftFrame.place(x=0,y=102,width=250,height=625)

        lbl_Frame_icon=Label(leftFrame,image=self.Frame_icon)
        lbl_Frame_icon.pack(side=TOP,fill=X)

        # Frame button image resize
        self.frame_btn_icon = Image.open("image/Arrow.png")
        self.frame_btn_icon = self.frame_btn_icon.resize((40, 40), Image.LANCZOS)
        self.frame_btn_icon = ImageTk.PhotoImage(self.frame_btn_icon)

        #Frame Menu
        menu=Label(leftFrame,text="Menu",font=("times new roman",25),bg="#009688").pack(side=TOP,fill=X)

        #Frame button Employee
        employee=Button(leftFrame,text="Employee",command=self.employee,image=self.frame_btn_icon,compound=LEFT,padx=15,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=4,cursor="hand2").pack(side=TOP,fill=X)

        # Frame button Supplier
        supplier = Button(leftFrame, text="Supplier",command=self.supplier,image=self.frame_btn_icon,compound=LEFT,padx=15,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)

        # Frame button Category
        category = Button(leftFrame, text="Category",command=self.category,image=self.frame_btn_icon,compound=LEFT,padx=15,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)

        # Frame button Product
        product = Button(leftFrame, text="Product",image=self.frame_btn_icon,compound=LEFT,padx=15,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)

        # Frame button Sales
        sales = Button(leftFrame, text="Sales",image=self.frame_btn_icon,compound=LEFT,padx=15,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)

        # Frame button Exit
        exit = Button(leftFrame, text="Exit",image=self.frame_btn_icon,compound=LEFT,padx=15,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=4,cursor="hand2").pack(side=TOP, fill=X)


        # main Contents
        # Total Employee
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE).place(x=375,y=120,height=150,width=300)

        # Total Supplier
        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bg="#ff5722", fg="white",font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE).place(x=725, y=120,height=150, width=300)

        # Total Category
        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bg="#009688", fg="white",font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE).place(x=1075, y=120,height=150, width=300)

        # Total Product
        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bg="#607d8b", fg="white",font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE).place(x=375, y=325,height=150, width=300)

        # Total Sales
        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bg="#ffc107", fg="white",font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE).place(x=725, y=325,height=150, width=300)

        # footer
        footer=Label(self.root,text="IMS- Inventory Management System | Developed by Fingers\nFor any technical issue contact : 1234567890",font=("times new roman",12),bg="#4d636d",fg="white").pack(side="bottom",fill=X)

#--------------------------------------------- function definations ----------------------------------

    # employee screen
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def logout(self):
       self.root.destroy()
       os.system("python login.py")


if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()




