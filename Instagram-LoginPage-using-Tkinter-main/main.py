from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login Instagram Page - Created by Aashish Baisla")
window.minsize(240,300)
window.resizable(width=False, height=False)
window.columnconfigure(0, weight=1)
window.wm_iconbitmap('login2.ico')


def getvalue():
    print("Username: ", uservalue.get())
    print("Passvalue: ", passvalue.get())


def loginfo():
    if uservalue.get()=="Phone number, username, or email" or passvalue.get()=="Password" or uservalue.get()=="" or passvalue.get()=="":
        messagebox.showwarning("Alert!", "Enter Details first!")

    elif uservalue.get() and passvalue.get():
        Label(text="LOGIN SUCCESSFUL!", fg="green", pady=15).grid(row=7, column=0)
        getvalue()


def temp_text_1(event):
    Username_Entry_1.delete(0,"end")
    Username_Entry_1.config(fg="black")

def temp_text_2(event):
    Password_Entry_2.delete(0, "end")
    Password_Entry_2.config(show="*")

def Ent_action(event):
    loginfo()


Insta_Logo = PhotoImage(file="icons/insta.png")
Insta_Logo_Label = Label(window, image=Insta_Logo).grid(row=0, column=0, padx=10, pady=5)

uservalue = StringVar()
passvalue = StringVar()

Username_Entry_1 = Entry(window, textvariable=uservalue, fg="grey" ,width=30, font=('Arial 10'), borderwidth=2)
Username_Entry_1.insert(0, "Phone number, username, or email")
Username_Entry_1.grid(row=1, column=0, padx=10, pady=8)
Username_Entry_1.bind("<Button>", temp_text_1)

Password_Entry_2 = Entry(window, textvariable=passvalue, fg="grey" ,width=30, font=('Arial 10'), borderwidth=2)
Password_Entry_2.insert(0, "Password")
Password_Entry_2.grid(row=2, column=0, padx=10,pady=8)
Password_Entry_2.bind("<Button>", temp_text_2)

Login_Button = Button(window ,text="Log In", bg="green",fg="white", command=loginfo, width=29, borderwidth=3)
Login_Button.grid(row=3, column=0, padx=5, pady=10)

Label_1 = Button(window, text="Log in with Facebook",relief="flat" , fg="blue").grid(row=4, column=0, pady=5)
Label_2 = Button(window, text="Forget Password?",relief="flat" , fg="black").grid(row=5, column=0, pady=5)
Label_3 = Button(window, text="Don't have an account? Sign up",relief="flat", fg="black").grid(row=6, column=0, pady=5)

window.bind("<Return>", Ent_action)

window.mainloop()