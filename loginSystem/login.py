from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class Login_system:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+50+50")
        
        #---images---
        self.bg_icon=ImageTk.PhotoImage(file="bg.png")
        self.user_icon=PhotoImage(file="user.png")
        self.pass_icon=PhotoImage(file="pass.png")
        self.logo_icon=PhotoImage(file="login.png")

        #---variable---
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root, text="loginSystem", font=("times new roman",40,"bold"),bg="blue",fg="white",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=450,y=150)

        logolbl=Label(Login_Frame,image=self.logo_icon).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white", command=self.Login).grid(row=3,column=1,pady=10)
    
    def Login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror(title="Error",message="all field")
        elif self.uname.get()=="misha" or self.pass_.get()=="mmmm":
            messagebox.showinfo(title="successful",message= f"welcome{self.uname.get()}")
        else:
            messagebox.showerror(title="Error",message="all field rquire")
    
    
    
root=Tk()
obj=Login_system(root)
root.mainloop()