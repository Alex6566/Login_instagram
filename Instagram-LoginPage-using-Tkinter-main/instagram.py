from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("(<Login instagram>)")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(width=False,height=False)
root.wm_iconbitmap("login2.ico")
def getvalue():
    print("Username: ", userValue.get())
    print("Password: ", passValue.get())

        
def temp_text_1(event):
    user.delete(0,"end")
    user.config(fg="black")

def temp_text_2(event):
    code.delete(0, "end")
    


def on_leave2(e):
    name=user.get()
    if name == "" :
        user.insert(0,"User name")
        
def on_leave(e):
    name=code.get()
    if name == "" :
        code.insert(0,"Password")
def signin():
    username=user.get()
    password=code.get()
    
    if username == "admin" and password == "1234" :
        Label(frame,text="LOGIN SUCCESSFUL!",bg="white", fg="green", pady=15).place(x=125,y=300)
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        
        Label(screen,text="Hello Everyone!",bg="#fff",font=("calibri(Body)",50,"bold")).pack(expand=True)
        
        
        screen.mainloop()
    elif username!= "admin" and password != "1234":
        Label(frame,text="Enter Details first!",bg="white", fg="red", pady=15).place(x=125,y=300)
        
        getvalue()
    
UserValue = StringVar()
PassValue = StringVar()



img = PhotoImage(file= "login3.png")
Label(root,image=img,bg="white").place(x=-50,y=-20)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text= "sign in",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

user = Entry(frame,width=25,fg="black",textvariable=UserValue,border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0, "User name")
user.bind("<Button>", temp_text_1)
user.bind("<FocusOut>" , on_leave2)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

code = Entry(frame,width=25,fg="black",textvariable=PassValue,border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0 , "Password")
code.bind("<FocusOut>" , on_leave)
code.bind("<Button>", temp_text_2)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

Button(frame,width=39,pady= 7 , text="sign in",command=signin,bg="#57a1f8",fg="white",border=0).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)

signUp = Button(frame,width=6,text="sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8")
signUp.place(x=215,y=270)

root.mainloop()
