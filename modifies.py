import mttkinter
from tkinter import *
import mttkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tigermovie import tgrmv
from swift import swift
from marvel import marvel1
from japanmovie import japan
from jigarthanda import jigar
from napolean import nap
from wish import wish
from wonka import wonka
from dunki import dunki
from animal import animal
from sam import sam
from fail import fail
import threading
import matplotlib as plt
import matplotlib.pyplot as plt
#to play video
'''root = tk.Tk()
root.title('VIDEO')
root.geometry('1300x990')
root.configure(bg='blue')
root.resizable(True, True)
videoplayer = TkinterVideo(master=root, scaled=True)

videoplayer.load("logo_v.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video
root.after(5000,root.destroy)

root.mainloop()'''
################################################################3
#connecting to the database

################################################################################
#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
mycur = db.cursor()

root=tk.Tk()
root.title('Login')
root.geometry('925x500+300+20')
root.configure(bg="#fff")
root.resizable(False,False)


def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Sign up successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "insert into login values(%s,%s)"
        t = (username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()


def registration():
    global img2
    global root1
    root1 = Toplevel(root)
    root1.title('Sign up')
    root1.geometry('925x500+300+20')
    root1.configure(bg="#fff")
    root1.resizable(False,False)
    img2=PhotoImage(file='Logo.png')
    Label(root1,image=img2,border=0,bg='white').place(x=2,y=5)
    frame=Frame(root1,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading=Label(root1,text='SIGN UP',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',28,'bold'))
    heading.place(x=550,y=60)
    global username
    global password
    username = StringVar()
    password = StringVar()
    def on_enter(e):
        username.delete(0,'end')
    def on_leave(e):
        if username.get()=='':
            username.insert(0,'Username')

    username=Entry(root1,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    username.place(x=560,y=150)
    username.insert(0,'Username')
    username.bind("<FocusIn>",on_enter)
    username.bind("<FocusOut>",on_leave)


    Frame(root1,width=295,height=2,bg='black').place(x=558,y=187)
################
    def on_enter(e):
        password.delete(0,'end')
    def on_leave(e):
        if password.get()=='':
            password.insert(0,'Password')

    password=Entry(root1,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    password.place(x=560,y=210)
    password.insert(0,'Password')
    password.bind("<FocusIn>",on_enter)
    password.bind("<FocusOut>",on_leave)

    Frame(root1,width=295,height=2,bg='black').place(x=558,y=247)

    Button(root1,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=register_user).place(x=550,y=280)
    #label=Label(root1,text='I have an account!',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    #label.place(x=560,y=327)

    #b=Button(root1,width=6,text='Sign in',border=1,bg='white',cursor='hand2',fg='#57a1f8',command=main_screen)
    #b.place(x=680,y=327)


    root1.mainloop()

    #######################

    '''l1=Label(root1,text="Username :",font="bold")
    l1.place(x=690,y=120)
    l2=Entry(root1,textvariable=username)
    l2.place(x=670,y=150)
    l3=Label(root1, text="Password :")
    l3.place(x=690,y=190)
    l4=Entry(root1, textvariable=password,show="*")
    l4.place(x=670,y=230)
    btn=Button(root1,text="Sign up",bg="lightblue",command=register_user)
    btn.place(x=700,y=280)'''
#############################

def logg_destroy():
    logg.destroy()
    root.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    root.wm_state('iconic')
    global videoplayer
    global logg
    logg = tk.Tk()
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Go to CINETICKET!", bg="grey", width=18, height=1, command=home).pack()
    
def failed():
    global fail
    fail = Toplevel(root)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()

def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where username = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            
            break
    else:
        failed()

#imge1 = PhotoImage(file = 'tiger2poster.png')
#tiger=Button(content_frame,image=imge1,command=tgrmv)
view = PhotoImage(file = 'view.png')
hide = PhotoImage(file = 'hide.png')
def toggle_password():
   
    if password_varify.cget('show') =='*':
        password_varify.config(show='')
        toggle_btn.config(image=view)
    else:
        password_varify.config(show='*')
        toggle_btn.config(image=hide)#text='view Password')
###############################################
def main_screen():
    global toggle_btn
    global img
    img=PhotoImage(file='Logo.png')
    Label(root,image=img,border=0,bg='white').place(x=2,y=5)
    frame=Frame(root,width=350,height=350,bg='#fff')
    frame.place(x=480,y=70)
    heading=Label(frame,text='LOG IN',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',28,'bold'))
    heading.place(x=110,y=3)
    global username_varify
    global password_varify
    username = StringVar()
    password = StringVar()
    
    def on_enter(e):
        username_varify.delete(0,'end')

    def on_leave(e):
        name=username_varify.get()
        if name=='':
            username_varify.insert(0,'Username')

            
    username_varify=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    username_varify.place(x=30,y=80)
    username_varify.insert(0,'Username')
    username_varify.bind('<FocusIn>',on_enter)
    username_varify.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    def on_enter(e):
        password_varify.delete(0,'end')

    def on_leave(e):
        name=password_varify.get()
        if name=='':
            password_varify.insert(0,'Password')
#text='Show Password',
    
    toggle_btn=Button(frame,image=view, height=22,width=30,bg='white',highlightthickness = 0, bd = 0,command=toggle_password)
    toggle_btn.place(x=280,y=150)
            
    password_varify= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    password_varify.place(x=30,y=150)
    password_varify.insert(0,'password')
    password_varify.bind('<FocusIn>',on_enter)
    password_varify.bind('<FocusOut>',on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##################################
            
    '''user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)'''
    
    Button(frame,width=39,height=2,text='Log-In',bg='#57a1f8',fg='white',border=0,command=login_varify).place(x=35,y=204)
    label=Label(frame,text="Dont have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    label.place(x=75,y=270)
    sign_up=Button(frame,width=6,text='Sign up',border=1,bg='white',cursor='hand2',fg='#57a1f8',command=registration)
    sign_up.place(x=240,y=270)


    root.mainloop()
    
    '''l1=Label(root, text="")
    l1.place(x=90,y=90)
    l2=Label(root, text="Username :", font="bold")
    l2.place(x=690,y=120)
    l6=Entry(root, textvariable=username_varify)
    l6.place(x=670,y=150)
    l3=Label(root, text="")
    l3=Label(root, text="Password :")
    l3.place(x=690,y=190)
    l7=Entry(root, textvariable=password_varify, show="*")
    l7.place(x=670,y=230)
    l4=Label(root, text="")
    l4.place(x=550,y=170)
    l5=Button(root, text="Log-In", bg="lightblue",command=login_varify)
    l5.place(x=700,y=280)
    Label(root, text="")'''
    '''l8=Label(root, text="Dont have an account? ", font="bold",fg="DeepSkyBlue4")
    l8.place(x=630,y=330)
    l9=Button(root, text="Sign up", bg="lightblue",command=registration)
    l9.place(x=800,y=330)'''

def failed2_destroy():
    fail2.destroy()

def failed2():
    global fail2
    fail2 = Toplevel(root)
    fail2.title("ERROR")
    fail2.geometry("200x100")
    Label(fail2, text="User not found...", fg="red", font="bold").pack()
    Label(fail2, text="").pack()
    Button(fail2, text="Ok", bg="grey", width=8, height=1, command=failed2_destroy).pack()

    
def update():
    global img9
    global root1
    root1 = Toplevel(root)
    root1.title('Update')
    root1.geometry('925x500+300+20')
    root1.configure(bg="#fff")
    root1.resizable(False,False)
    img9=PhotoImage(file='Logo.png')
    Label(root1,image=img9,border=0,bg='white').place(x=2,y=5)
    frame=Frame(root1,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading=Label(root1,text='UPDATE ACCOUNT',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',28,'bold'))
    heading.place(x=545,y=90)
    global user
    global username2
    global password2
    user= StringVar()
    username2 = StringVar()
    password2 = StringVar()
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Existing Username')

    user=Entry(root1,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=550,y=153)
    user.insert(0,'Existing Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(root1,width=295,height=2,bg='black').place(x=550,y=187)

    Button(root1,width=20,height=1,text='Check',bg='#57a1f8',fg='white',border=0,command=check).place(x=570,y=200)
    
    #btn=Button(root1,width=6,text='check',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=check)
    #btn.place(x=720,y=50)
    ####-------------------------------------
    def on_enter(e):
        password2.delete(0,'end')
    def on_leave(e):
        if password2.get()=='':
            password2.insert(0,'New Password')

    password2=Entry(root1,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    password2.place(x=550,y=250)
    password2.insert(0,'New Password')
    password2.bind("<FocusIn>",on_enter)
    password2.bind("<FocusOut>",on_leave)

    Frame(root1,width=295,height=2,bg='black').place(x=550,y=287)

    Button(root1,width=20,height=1,text='Sign up',bg='#57a1f8',fg='white',border=0,command=register_user2).place(x=570,y=300)
    
    label=Label(root1,text='Want to delete account?',fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
    label.place(x=565,y=350)

    
    y=Button(root1,width=7,text='yes',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=delete)
    y.place(x=740,y=350)
    ####-------------------------------------
   
    
    '''l1=Label(root1,text="Existing Username:",font="bold")
    l1.place(x=690,y=120)
    l2=Entry(root1,textvariable=user)
    l2.place(x=690,y=160)
    btn=Button(root1,text="Check",bg="lightblue",command=check)
    btn.place(x=720,y=200)
    l5=Label(root1, text="New Password :")
    l5.place(x=692,y=270)
    l6=Entry(root1, textvariable=password2,show="*")
    l6.place(x=690,y=300)
    btn=Button(root1,text="Sign up",bg="lightblue",command=register_user2)
    btn.place(x=720,y=350)
    l8=Label(root1, text="Want to delete account? ", font="bold",fg="DeepSkyBlue4")
    l8.place(x=630,y=400)
    l9=Button(root1, text="yes!", bg="lightblue",command=delete)
    l9.place(x=800,y=400)'''
    

def delete():
    global img8
    global root1
    root1 = Toplevel(root)
    root1.title('Update')
    root1.geometry('925x500+300+20')
    root1.configure(bg="#fff")
    root1.resizable(False,False)
    img8=PhotoImage(file='Logo.png')
    Label(root1,image=img8,border=0,bg='white').place(x=2,y=5)
    frame=Frame(root1,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading=Label(root1,text='DELETE ACCOUNT',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',28,'bold'))
    heading.place(x=550,y=100)
    global username2
    global password2
    username2 = StringVar()
    password2 = StringVar()
    def on_enter(e):
        username2.delete(0,'end')
    def on_leave(e):
        if username2.get()=='':
            username2.insert(0,'Existing Username')

    username2=Entry(root1,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    username2.place(x=550,y=205)
    username2.insert(0,'Existing Username')
    username2.bind("<FocusIn>",on_enter)
    username2.bind("<FocusOut>",on_leave)


    Frame(root1,width=295,height=2,bg='black').place(x=550,y=235)

    #btn=Button(root1,text="Check",bg="lightblue",command=check)
    #btn.place(x=720,y=200)
    ####-------------------------------------
    def on_enter(e):
        password2.delete(0,'end')
    def on_leave(e):
        if password2.get()=='':
            password2.insert(0,'Existing Password ')

    password2=Entry(root1,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    password2.place(x=550,y=255)
    password2.insert(0,'Existing Password')
    password2.bind("<FocusIn>",on_enter)
    password2.bind("<FocusOut>",on_leave)

    Frame(root1,width=295,height=2,bg='black').place(x=550,y=285)

    #label=Label(root1,text='Want to delete account?',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    #label.place(x=560,y=327)

    Button(root1,width=39,height=2,text='Delete',bg='#57a1f8',fg='white',border=0,command=verify2).place(x=550,y=300)
    #btn=Button(root1,width=6,text='Check',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=verify2)
    #btn.place(x=700,y=327)
    '''l3=Label(root1, text="Existing Username:")
    l3.place(x=692,y=120)
    l4=Entry(root1,textvariable=username2)
    l4.place(x=690,y=150)
    l5=Label(root1, text="Existing Password :")
    l5.place(x=692,y=190)
    l6=Entry(root1, textvariable=password2,show="*")
    l6.place(x=690,y=210)
    btn=Button(root1,text="Check",bg="lightblue",command=verify2)
    btn.place(x=720,y=250)'''

    
def deletion():
    username_info = username2.get()
    password_info = password2.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "delete from login where password=(%s) and username=(%s)"
        t = ([password_info, username_info])
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success2()


def success2():        
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("300x100")
    Label(succ, text="Account successfully deleted...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

    

def verify2():
    user_varify = username2.get()
    pas_varify = password2.get()
    sql = "select * from login where username = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            deletion()
            root1.destroy()
            break
        return
    else:
        failed2()




def check():
    username_info = user.get()
    if username_info == "":
        error()
    else:
        if l2():
            '''sql = "delete from login where username=(%s)"
            t = ([username_info])
            mycur.execute(sql, t)
            db.commit()'''
            messagebox.showinfo('Username found','User found')
            return



def register_user2():
    username_info = user.get()
    password_info = password2.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "update login set password=(%s) where username=(%s)"
        t = ([password_info, username_info])
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()


def l2():
    user_varify = user.get()
    sql = "select * from login where username = (%s)"
    mycur.execute(sql,[(user_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            break
        return True
                        
    else:
        failed2()
########################################################
def home():
    global marvel
    global japan
    global jigar
    global taylor
    global test
    global img
    global img2
    global img3
    global x
    global test
    global test3
    class TwoColoredFrame(tk.Frame):
        def __init__(self, master, bg1, bg2, fraction=0.5, **kw):
            kw["bg"] = bg2  # color of the lower part of the Frame
            tk.Frame.__init__(self, master, **kw)
            # upper color stripe 
            tk.Frame(self, bg=bg1).place(relx=0, rely=0, relwidth=1, relheight=fraction)       
    # Create the main window
    parent = tk.Toplevel()
    parent.title("CINETICKET")
    parent.geometry('1290x1000')
    parent.resizable(True, True)
   #########&&&&&&&&&&&&&&&&&############################
    #To create a scrollbar
    def on_scrollbar_move(*args):
        canvas.yview(*args)
 
    frame1 = Frame(parent)
    frame1.pack(fill=BOTH, expand=True)
 
    # Create a canvas widget
    canvas = Canvas(frame1)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
 
    # Create a scrollbar widget
    scrollbar = Scrollbar(frame1, command=on_scrollbar_move)
    scrollbar.pack(side=RIGHT, fill=Y)
 
    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
 
    # Create a frame inside the canvas to hold the content
    content_frame = Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor=NW)
 
    #########
    frame = TwoColoredFrame(content_frame, width=1290, height=1000, bg2='antiquewhite1', bg1="gray28", fraction=0.10)
    frame.pack_propagate(0)
    frame.pack(fill="both", expand=True)
    label1 = tk.Label(frame, bg='antiquewhite1')
    label1.pack(side="bottom")
 
    label1 = tk.Label(frame, bg='gray28', fg="white")
    label1.pack(side="top")
    #########################################################
    def call():
        # Create an instance of tkinter window 
        win = Tk()
        # Define the geometry of the window
        win.geometry("700x500")       
    # Define buttons for menu bar
    movies2= Button(content_frame, text="MOVIES",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=movies)
    movies2.place(x=200, y=40)
    # movie poster buttons on home screen
    imge1 = PhotoImage(file = 'tiger2poster.png')
    tiger=Button(content_frame,image=imge1,command=tgrmv)
    tiger.place(x=30, y=500)
    imge2 = PhotoImage(file = 'marvelsposter.png')
    marvel=Button(content_frame,image=imge2,command=marvel1)
    marvel.place(x=280, y=500)
    imge3 = PhotoImage(file = 'japanposter.png')
    japan2=Button(content_frame,image=imge3,command=japan)
    japan2.place(x=525, y=500)
    imge4 = PhotoImage(file = 'jigarthandaposter.png')
    jigar2=Button(content_frame,image=imge4,command=jigar)
    jigar2.place(x=770, y=500)
    imge5 = PhotoImage(file = 'tayloreraposter.png')
    taylor=Button(content_frame,image=imge5,command=swift)
    taylor.place(x=1015, y=500)
    # To add design to mainscreen
    txt = 'Hastle free ticket booking....Anytime......Anywhere!!'
    lbl = tk.Label(content_frame, font='Bell 36 bold', width=43,bg = "brown",fg = "orange")
    lbl.place(x=0, y=400)
    def animate_label(text, n=0):
        if n < len(text)-1:
            # not complete yet, schedule next run one second later
            lbl.after(1000, animate_label, text, n+1)
        # update the text of the label
        lbl['text'] = text[:n+1]
    # start the "after loop" one second later
    content_frame.after(1000,animate_label, txt)    ###########################################################################
    #upper buttons
    turn_on =Button(content_frame,text="Change password", font= ('Poplar Std', 15), fg= "black",bg="lightgreen",command=update)
    turn_on.place(x=700, y=36)
    turn_on =Button(content_frame,text="LOG OUT", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="brown",command=logg_destroy)
    turn_on.place(x=900, y=36)
    l=Label(content_frame, text="Welcome {}!! ".format(username_varify.get()),bg="gray28", fg="white", font= ('Poplar Std', 20))
    l.place(x=1020, y=36)
    turn_on.pack
   ###########################################################################
    image4 = Image.open("home_page_logo.png")
    test3 = ImageTk.PhotoImage(image4)
    label1s = tk.Label(parent,image=test3)
    label1s.image = test3
    canvas.create_window(20, 50, window=label1s, anchor='w')
   ############################################################################
    # loading the images 
    img=ImageTk.PhotoImage(Image.open("image1.png")) 
    img2=ImageTk.PhotoImage(Image.open("image2.png")) 
    img3=ImageTk.PhotoImage(Image.open("image3.png")) 
    l=Label(content_frame)
    l.place(x=100,y=110)
    #l.pack(padx=90,pady=280)
    # using recursion to slide to next image 
    x = 1
    # function to change to next image 
    def move(): 
            global x 
            if x == 4: 
                    x = 1
            if x == 1: 
                    l.config(image=img) 
            elif x == 2: 
                    l.config(image=img2) 
            elif x == 3: 
                    l.config(image=img3) 
            x = x+1
            content_frame.after(2000, move)
 
    # calling the function 
    move()
    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))
    parent.mainloop()


    
#########$$$$$$$$$$$$$$$$$$#########################3
def movies():
    global marvel2
    global dunki
    global animal
    global taylor
    global tiger
    global sam
    global fail
    global test
    global test2    
    class TwoColoredFrame(tk.Frame):
        def __init__(self, master, bg1, bg2, fraction=0.5, **kw):
            kw["bg"] = bg2  # color of the lower part of the Frame
            tk.Frame.__init__(self, master, **kw)
            # upper color stripe 
            tk.Frame(self, bg=bg1).place(relx=0, rely=0, relwidth=1, relheight=fraction)            
    # Create the main window
    parent = tk.Toplevel()
    parent.title("MOVIES")
    parent.geometry('1290x1000')
    parent.resizable(True, True)
    def on_scrollbar_move(*args):
        canvas.yview(*args)
    frame1 = Frame(parent)
    frame1.pack(fill=BOTH, expand=True)
    # Create a canvas widget
    canvas = Canvas(frame1)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    # Create a scrollbar widget
    scrollbar = Scrollbar(frame1, command=on_scrollbar_move)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    # Create a frame inside the canvas to hold the content
    content_frame = Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor=NW)
    #########
    frame = TwoColoredFrame(content_frame, width=1290, height=1000, bg2='antiquewhite1', bg1="gray28", fraction=0.10)
    frame.pack_propagate(0)
    frame.pack(fill="both", expand=True)
    label1 = tk.Label(frame, bg='antiquewhite1')
    label1.pack(side="bottom")
    label1 = tk.Label(frame, bg='gray28', fg="white")
    label1.pack(side="top")
    #########################################################
    def call():
        # Create an instance of tkinter window 
        win = Tk()
        # Define the geometry of the window
        win.geometry("700x500")
    ###########################################################################
    #upper buttons
    turn_on = Button(content_frame, text="<-BACK", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="brown",command=parent.destroy)
    turn_on.place(x=900, y=36)
    l=Label(content_frame, text="Welcome {}!! ".format(username_varify.get()),bg="gray28", fg="white", font= ('Poplar Std', 20))
    l.place(x=1020, y=36)
    turn_on.pack    
    ###########################################################################
    # Create a photoimage object of the image in the path
    image4 = Image.open("home_page_logo.png")
    test3 = ImageTk.PhotoImage(image4)
    label1s = tk.Label(parent,image=test3)
    label1s.image = test3
    canvas.create_window(20, 50, window=label1s, anchor='w')
    ###########################################################################
    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))
    ################################################################################
    #ENG MOVIES
    win_label= Label(content_frame, text= "ENGLISH MOVIES", font= ('Verdana bold', 30), fg= "black",bg="bisque3")
    win_label.place(x=20, y=100)
    imge2 = PhotoImage(file = 'marvelsposter.png')
    marvel2=Button(content_frame,image=imge2,command=marvel1)#command=call
    marvel2.place(x=20, y=160)
    imge5 = PhotoImage(file = 'tayloreraposter.png')
    taylor=Button(content_frame,image=imge5,command=swift)#command=call
    taylor.place(x=270, y=160)
    imge1 = PhotoImage(file = 'napoleanposter.png')
    taylor=Button(content_frame,image=imge1,command=nap)#command=call
    taylor.place(x=530, y=160)
    imge3 = PhotoImage(file = 'wishposter.png')
    taylor=Button(content_frame,image=imge3,command=wish)#command=call
    taylor.place(x=790, y=160)
    imge4 = PhotoImage(file = 'wonkaposter.png')
    taylor=Button(content_frame,image=imge4,command=wonka)#command=call
    taylor.place(x=1050, y=160)
    win_label= Label(content_frame, text= "HINDI MOVIES", font= ('Verdana bold', 30), fg= "black",bg="bisque3")
    win_label.place(x=20, y=550)
    imge6 = PhotoImage(file = 'tiger2poster.png')
    tiger=Button(content_frame,image=imge6,command=tgrmv)#command=call
    tiger.place(x=20, y=610)
    imge7 = PhotoImage(file = 'dunkiposter.png')
    dunki1=Button(content_frame,image=imge7,command=dunki)#command=call
    dunki1.place(x=270, y=610)
    imge8 = PhotoImage(file = 'animalposter.png')
    animal1=Button(content_frame,image=imge8,command=animal)#command=call
    animal1.place(x=510, y=610)
    imge9 = PhotoImage(file = 'sambahadurposter.png')
    sam1=Button(content_frame,image=imge9,command=sam)#command=call
    sam1.place(x=770, y=610)
    imge10 = PhotoImage(file = '12failposter.png')
    fail1=Button(content_frame,image=imge10,command=fail)#command=call
    fail1.place(x=1030, y=610)
    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))
    parent.mainloop()
def bookings():
    global test4
    global image5
    class TwoColoredFrame(tk.Frame):
        def __init__(self, master, bg1, bg2, fraction=0.5, **kw):
            kw["bg"] = bg2  # color of the lower part of the Frame
            tk.Frame.__init__(self, master, **kw)
            # upper color stripe 
            tk.Frame(self, bg=bg1).place(relx=0, rely=0, relwidth=1, relheight=fraction)            
    # Create the main window
    parent1 = tk.Toplevel()
    parent1.title("Bookings")
    parent1.geometry('1290x1000')
    parent1.resizable(True, True)
    #########&&&&&&&&&&&&&&&&&############################
    def on_scrollbar_move(*args):
        canvas.yview(*args)
    frame1 = Frame(parent1)
    frame1.pack(fill=BOTH, expand=True)
    # Create a canvas widget
    canvas = Canvas(frame1)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    # Create a scrollbar widget
    scrollbar = Scrollbar(frame1, command=on_scrollbar_move)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    # Create a frame inside the canvas to hold the content
    content_frame = Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor=NW)

    #########
    frame = TwoColoredFrame(content_frame, width=1290, height=1000, bg2='antiquewhite1', bg1="gray28", fraction=0.10)
    frame.pack_propagate(0)
    frame.pack(fill="both", expand=True)
    label1 = tk.Label(frame, bg='antiquewhite1')
    label1.pack(side="bottom")
    label1 = tk.Label(frame, bg='gray28', fg="white")
    label1.pack(side="top")
    turn_on = Button(content_frame, text="<-BACK", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="brown",command=parent1.destroy)
    turn_on.place(x=900, y=36)
    l=Label(content_frame, text="{}\'s bookings!".format(username_varify.get()),bg="gray28", fg="white", font= ('Poplar Std', 20))
    l.place(x=1020, y=36)
    image5 = Image.open("home_page_logo.png")
    test4 = ImageTk.PhotoImage(image5)
    label1s = tk.Label(parent1,image=test4)
    label1s.image = test4
    canvas.create_window(20, 50, window=label1s, anchor='w')
    db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
    mycur = db.cursor()
    c="select bookings from bookings2 where username='{}';".format(str(username_varify.get()))
    mycur.execute(c)
    data=mycur.fetchall();
    l=Label(content_frame, text=data, font= ('Poplar Std',10), fg= "black",bg="white")
    l.place(x=25, y=110)
    db.close()
    mycur.close()
    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))
    parent1.mainloop()
main_screen()
root.mainloop()









            








