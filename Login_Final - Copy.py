from tkinter import*
from tkinter import messagebox
import ast
from tkvideo import tkvideo

from Scroll import home
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tigermovie import tgrmv
from marvel import marvel

root=Tk()
root.title('Login')
root.geometry('925x500+300+20')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password==r[username]:
        #screen=Toplevel(root)
        #screen.title("CiniTickets")
        #screen.geometry('925x500+300+200')
        #screen.config(bg="White")
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("logo_v.mp4", my_label,size = (925,500))#loop = 1,
        player.play()
        root.after(5000, root.destroy)

        def create_window():
            """root2=Tk()
            root2.title('Try')
            root2.geometry('925x500+300+20')
            root2.configure(bg="#fff")
            root2.resizable(True,True)
            Label(root2)#,command=home(m))#.pack(expand=True)#text='Welcome!',bg='#fff',font=('Calibri(Body)',50,'bold"""
            home()
            """screen=Toplevel(root2)
            screen.title("CiniTickets")
            screen.geometry('925x500+300+200')
            screen.config(bg="White")
            Label(screen,text='Welcome!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)"""

        root.after(4999,create_window)

        #Label(screen,text='Welcome!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        
        #screen.mainloop()

    else:
        messagebox.showerror('Invalid','invalid username or password')

#############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if password==conform_password:             
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()


                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Signup','sucessfully sign up')
                window.destroy()


            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid','Both password should match')


    def sign():
        window.destroy()

    img=PhotoImage(file='Logo.png')
    Label(window,image=img,border=0,bg='white').place(x=2,y=5)


    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    ####-------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    ####-------------------------------------
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')

    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    ####-------------------------------------
    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Confirm Password')

    conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,'Confirm Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    #------------------------------------

    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)



    window.mainloop()




##############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    

#img = PhotoImage(file=r'C:\Users\Medha\OneDrive\Desktop\Login 1.png')
#Label(root,image=img,bg='white').place(x=5,y=50)
img=PhotoImage(file='schoollogo.png')
Label(root,image=img,bg='white').place(x=100,y=100)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

        
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

        
code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,height=2,text='sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Dont have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text='Sign up',border=1,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=240,y=270)


root.mainloop()


      

        
