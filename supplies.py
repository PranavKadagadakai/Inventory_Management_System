from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Finance Management System | Developed by FinTech Innovators")
        self.root.focus_force()

        #Title
        title=Label(self.root,text="Customer Bill Reports",font=("times new roman",15,"bold"),bg='#0f4d7d',fg='white').pack(side=TOP,fill=X,padx=5,pady=10)

        # 1st row
        lbl_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",12)).place(x=50,y=60)
        txt_invoice=Entry(self.root,font=("goudy old style",12),bg='lightyellow').place(x=140,y=60,width=180)

        # Button
        btn_search=Button(self.root,text="Search",font=("goudy old style",12),bg='#2196f3',fg='white',cursor='hand2').place(x=330,y=56,width=130,height=28)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 12), bg="#607d8b",fg='white', cursor="hand2").place(x=470, y=56, width=130, height=28)

        # left frame
        left_frame=Frame(self.root,bd=3,relief=RIDGE)
        left_frame.place(x=50,y=90,width=240,height=380)

        # left frame scroll bar
        scrollY=Scrollbar(left_frame,orient=VERTICAL)
        self.sales_List=Listbox(left_frame,font=("goudy old style",15),yscrollcommand=scrollY.set)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollY.config(command=self.sales_List.yview)
        self.sales_List.pack(fill=BOTH,expand=1)

        # Bill Area
        bill_area_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_area_frame.place(x=300,y=90,width=410,height=380)

        # Title2
        title2 = Label(bill_area_frame, text = "Customer Bill Area", font = ("times new roman", 13, "bold"), bg = 'orange').pack(side=TOP, fill=X)

        # Bill Area scroll bar
        scrollY2 = Scrollbar(bill_area_frame, orient=VERTICAL)
        self.bill_area = Text(bill_area_frame, font=("goudy old style", 12),bg='lightyellow', yscrollcommand=scrollY2.set)
        scrollY2.pack(side=RIGHT, fill=Y)
        scrollY2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)


if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()