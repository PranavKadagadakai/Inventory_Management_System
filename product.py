from tkinter import *
#from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Fingers")
        self.root.focus_force()

        #----------------- All Variable ------------------
        self.var_searchBy = StringVar()
        self.var_searchTxt = StringVar()

        self.var_cat=StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        #--------------------------------------------------

        # Left frame
        left_frame=Frame(self.root,bd=3,relief=RIDGE)
        left_frame.place(x=10,y=10,width=480,height=480)

        # left frame title
        left_title=Label(left_frame,text="Manage Product Details",font=("times new roman",15,"bold"),bg='#0f4d7d',fg='white').pack(side=TOP,fill=X)

        # 1st row
        lbl_category=Label(left_frame,text="Category",font=("goudy old style",12)).place(x=50,y=40)
        cmb_category = ttk.Combobox(left_frame,textvariable=self.var_cat,values=("Select"), state='readonly',font=("goudy old style", 10))  # Create Combobox inside searchFrame
        cmb_category.place(x=140, y=42, width=180)  # Place Combobox inside searchFrame
        cmb_category.current(0)

        # 2nd row
        lbl_supplier = Label(left_frame, text="Supplier", font=("goudy old style", 12)).place(x=50, y=80)
        cmb_supplier = ttk.Combobox(left_frame,textvariable=self.var_sup, values=("Select"), state='readonly',font=("goudy old style", 10))  # Create Combobox inside searchFrame
        cmb_supplier.place(x=140, y=82, width=180)  # Place Combobox inside searchFrame
        cmb_supplier.current(0)

        # 3rd row
        lbl_name = Label(left_frame, text="Name", font=("goudy old style", 12)).place(x=50, y=120)
        txt_name=Entry(left_frame,textvariable=self.var_name,font=("goudy old style",12),bg="lightyellow").place(x=140,y=122,width=180)

        # 4th row
        lbl_price = Label(left_frame, text="Price", font=("goudy old style", 12)).place(x=50, y=160)
        txt_price = Entry(left_frame, textvariable=self.var_price, font=("goudy old style", 12), bg="lightyellow").place(x=140, y=162, width=180)

        # 5th row
        lbl_quantity = Label(left_frame, text="Quantity", font=("goudy old style", 12)).place(x=50, y=200)
        txt_quantity = Entry(left_frame, textvariable=self.var_qty, font=("goudy old style", 12),bg="lightyellow").place(x=140, y=202, width=180)

        # 6th row
        lbl_status = Label(left_frame, text="Status", font=("goudy old style", 12)).place(x=50, y=240)
        cmb_status = ttk.Combobox(left_frame, textvariable=self.var_status, values=("Select","Active","Inactive"), state='readonly',font=("goudy old style", 10))  # Create Combobox inside searchFrame
        cmb_status.place(x=140, y=242, width=180)  # Place Combobox inside searchFrame
        cmb_status.current(0)


        # Button
        btn_save=Button(left_frame,text="Save",font=("goudy old style",12),bg="#2196f3",fg='white',cursor="hand2").place(x=10,y=400,width=100,height=28)
        btn_update = Button(left_frame, text="Update", font=("goudy old style", 12), bg="#4caf50", fg='white',cursor="hand2").place(x=130, y=400, width=100, height=28)
        btn_delete = Button(left_frame, text="Delete", font=("goudy old style", 12), bg="#f44336", fg='white',cursor="hand2").place(x=250, y=400, width=100, height=28)
        btn_clear = Button(left_frame, text="Clear", font=("goudy old style", 12), bg="#607d8b", fg='white',cursor="hand2").place(x=370, y=400, width=100, height=28)

        # Create search frame
        searchFrame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 12, "bold"), bd=3,relief=RIDGE)
        searchFrame.place(x=490, y=0, width=600, height=80)  # Place searchFrame using place method

        # Create search frame contents
        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_searchBy,values=("Select","Category","Supplier","Name"), state='readonly',font=("goudy old style", 10))  # Create Combobox inside searchFrame
        cmb_search.place(x=10, y=10, width=180)  # Place Combobox inside searchFrame
        cmb_search.current(0)

        txt_search = Entry(searchFrame, textvariable=self.var_searchTxt, font=("goudy old style", 10),bg="lightyellow").place(x=210, y=8, width=180, height=25)  # text box
        btn_search = Button(searchFrame, text="Search", font=("goudy old style", 10, "bold"),bg='#4caf50', cursor="hand2").place(x=410, y=4, width=150, height=30)


        # product detail using tree view
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=490, y=80,width=600, height=410)  # frame

        # scroll bars
        scrollY = Scrollbar(emp_frame, orient=VERTICAL)
        scrollX = Scrollbar(emp_frame, orient=HORIZONTAL)

        # creating tree view class
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("ID", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)

        # packing scrollbars
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        # setting scroll command property
        scrollX.config(command=self.EmployeeTable.xview)
        scrollY.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("ID", text="Employee ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"  # hiding default column

        # resizing the column width
        self.EmployeeTable.column("ID", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)



if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
