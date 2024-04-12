from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class BillClass:
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
        logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1350,y=10,height=50,width=150)

        # sub title
        self.clock = Label(self.root, text="Welcome to Inventory Management System\t\tDate: DD-MM-YYYY\t\tTime: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.clock.place(x=0,y=70,relwidth=1,height=30)
        
        # =====ProductFrame=====
        self.var_search = StringVar()
        
        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        ProductFrame1.place(x=6, y=110, width=410, height=550)
        
        pTitle = Label(ProductFrame1, text='All Products', font=('goudy old style', 20, 'bold'), bg='#262626', fg='white').pack(side=TOP, fill=X)
        
        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg='white')
        ProductFrame2.place(x=2, y=42, width=398, height=90)
        
        lbl_search = Label(ProductFrame2, text='Search Product | By Name ', font=('times new roman', 15, 'bold'), bg='white', fg='green').place(x=2, y=5)
        
        lbl_name = Label(ProductFrame2, text='Product Name', font=('times new roman', 15, 'bold'), bg='white').place(x=2, y=45)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=('times new roman', 15), bg='lightyellow').place(x=130, y=47, width=150, height=22)
        btn_search = Button(ProductFrame2, text="Search", bg='blue', font=('goudy old style', 15), bd=1, relief=RIDGE, fg='white', cursor='hand2').place(x=285, y=47, width=100, height=23)
        btn_show_all = Button(ProductFrame2, text="Show All", cursor='hand2', font=('goudy old style', 15), bd=1, relief=RIDGE, bg='red', fg='white').place(x=285, y=5, height=25, width=100)
        
        # supplier detail using frame
        ProductFrame3=Frame(ProductFrame1,bd=4,relief=RIDGE)
        ProductFrame3.place(x=2, y=140,width=398,height=375)

        # scroll bars
        scrollY = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollX = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        # creating tree view class
        self.Product_Table = ttk.Treeview(ProductFrame3, columns=("p_id", "name", "price", "quantity", 'status'),yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)

        # packing scrollbars
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        # setting scroll command property
        scrollX.config(command=self.Product_Table.xview)
        scrollY.config(command=self.Product_Table.yview)

        self.Product_Table.heading("p_id",text="P ID")
        self.Product_Table.heading("name", text="Name")
        self.Product_Table.heading("price", text="Price")
        self.Product_Table.heading("quantity", text="QTY")
        self.Product_Table.heading("status", text="Status")

        self.Product_Table["show"]="headings"

        #resizing the column width
        self.Product_Table.column('p_id',width=100)
        self.Product_Table.column('name', width=100)
        self.Product_Table.column('price', width=100)
        self.Product_Table.column('quantity', width=100)
        self.Product_Table.column('status', width=100)

        self.Product_Table.pack(fill=BOTH, expand=1)

        # self.Product_Table.bind('<ButtonRelease-1>',self.get_data)  # its a event  that calls get_data()
        
        lbl_note = Label(ProductFrame1, text="Note: 'Enter 0 QTY to Remove the Product from the Cart'", anchor='w', font=('goudy old style', 12), bg='white', fg='black').pack(side=BOTTOM, fill=X)
        
        # =====CustomerFrame=====
        self.var_name = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        CustomerFrame.place(x=420, y=110, width=530, height=100)
        
        cTitle = Label(CustomerFrame, text='Customer Details', font=('goudy old style', 20, 'bold'), bg='lightgrey').pack(side=TOP, fill=X)
        
        lbl_CName = Label(CustomerFrame, text='Name', font=('times new roman', 15), bg='white').place(x=5, y=50)
        txt_CName = Entry(CustomerFrame, font=('times new roman', 15), textvariable=self.var_name, bg='lightyellow').place(x=55, y=50, width=170)
        
        lbl_Contact = Label(CustomerFrame, text='Contact No.', font=('times new roman', 15), bg='white').place(x=230, y=50, width=110)
        txt_Contact = Entry(CustomerFrame, textvariable=self.var_contact, font=('times new roman', 15), bg='lightyellow').place(x=345, y=50, width=160)
        
        Calc_Cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        Calc_Cart_Frame.place(x=420, y=190, width=530, height=470)
        
        
if __name__ == '__main__':
    root = Tk()

    obj = BillClass(root)
    root.mainloop()