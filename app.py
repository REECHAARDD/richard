from tkinter import *
import tkinter.messagebox as MessageBox

root = Tk()
root.title("Login Form")
root.geometry("1600x1600")
root.configure(bg='Light blue')


def validate():
    username_result = t_uname.get()
    password_result = t_password.get()
    if username_result == "Richard" and password_result == "12345":
        MessageBox.showinfo("Login Access", "Login successful")

    else:
        MessageBox.showinfo("Wrong Entry", "Access Denied")


title = Label(root, text="Login Below", bg='Light Blue', fg="white", font=("bold", 30))
title.place(x=650, y=200)

uname = Label(root, text="USERNAME :", bg='Light Blue', fg="white", font=("bold", 13))
uname.place(x=600, y=297)
t_uname = Entry()
t_uname.place(x=800, y=300)

Email = Label(root, text="EMAIL ADDRESS:", bg='Light blue', fg="white", font=("bold", 13))
Email.place(x=600, y=350)
E_Email = Entry()
E_Email.place(x=800, y=350)

password = Label(root, text="PASSWORD:", bg='Light Blue', fg="white", font=("bold", 13))
password.place(x=600, y=400)
t_password = Entry(root, show="*")
t_password.place(x=800, y=400)

password = Label(root, text="CONFIRM PASSWORD:", bg='Light Blue', fg="white", font=("bold", 13))
password.place(x=600, y=450)
t2_password = Entry(root, show="*")
t2_password.place(x=800, y=450)

submit = Button(root, text="Login", bg='#003E53', fg="white", font=("bold", 13), command=validate)
submit.place(x=750, y=500)
root.mainloop()
