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
#root = tk.Tk()
root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('1300x990')
root.configure(bg='blue')
root.resizable(True, True)


videoplayer = TkinterVideo(master=root, scaled=True)

videoplayer.load("logo_v.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video
root.after(5000,root.destroy)

root.mainloop()


#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
mycur = db.cursor()


root=Tk()
root.title('Login')
root.geometry('925x500+300+20')
root.configure(bg="#fff")
root.resizable(False,False)





def root_destroy():
    root.destroy()



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
    heading.place(x=650,y=3)
    global username
    global password
    username = StringVar()
    password = StringVar()
    l1=Label(root1,text="Username :",font="bold")
    l1.place(x=690,y=120)
    l2=Entry(root1,textvariable=username)
    l2.place(x=670,y=150)
    l3=Label(root1, text="Password :")
    l3.place(x=690,y=190)
    l4=Entry(root1, textvariable=password,show="*")
    l4.place(x=670,y=230)
    btn=Button(root1,text="Sign up",bg="lightblue",command=register_user)
    btn.place(x=700,y=280)

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold",width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red",command=login_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global videoplayer
    global logg
    logg = Toplevel(root)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    #Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()
    Button(logg, text="Go to CINETICNET!", bg="grey", width=18, height=1, command=home).pack()
    

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


def main_screen():
    global img

    img=PhotoImage(file='Logo.png')
    Label(root,image=img,border=0,bg='white').place(x=2,y=5)

    frame=Frame(root,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='LOG IN',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',28,'bold'))
    heading.place(x=190,y=3)

    global username_varify
    global password_varify
    username_varify = StringVar()
    password_varify = StringVar()
    l1=Label(root, text="")
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
    Label(root, text="")
    l8=Label(root, text="Dont have an account? ", font="bold",fg="DeepSkyBlue4")
    l8.place(x=630,y=330)
    l9=Button(root, text="Sign up", bg="lightblue",command=registration)
    l9.place(x=800,y=330)
    
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
    #parent = tk.Tk()
    parent = tk.Toplevel()
    parent.title("CINETICKET")
    parent.geometry('1290x1000')
    parent.resizable(True, True)

    ########
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



    #########bisque3

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
    ''''stream= Button(content_frame, text="STREAM",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
    stream.place(x=270, y=40)
    events= Button(content_frame, text="EVENTS",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
    events.place(x=340, y=40)
    plays= Button(content_frame, text="PLAYS",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
    plays.place(x=410, y=40)
    sports= Button(content_frame, text="SPORTS",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
    sports.place(x=470, y=40)
    activities= Button(content_frame, text="ACTIVITIES",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
    activities.place(x=540, y=40)
    buzz= Button(content_frame, text="BUZZ",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
    buzz.place(x=630, y=40)'''


    # movie poster buttons on home screen
    imge1 = PhotoImage(file = 'tiger2poster.png')
    tiger=Button(content_frame,image=imge1,command=tgrmv)#command=call
    tiger.place(x=30, y=500)

    imge2 = PhotoImage(file = 'marvelsposter.png')
    marvel=Button(content_frame,image=imge2,command=marvel1)#command=call
    marvel.place(x=280, y=500)

    imge3 = PhotoImage(file = 'japanposter.png')
    japan=Button(content_frame,image=imge3,command=japan)#command=call
    japan.place(x=525, y=500)

    imge4 = PhotoImage(file = 'jigarthandaposter.png')
    jigar=Button(content_frame,image=imge4,command=jigar)#command=call
    jigar.place(x=770, y=500)

    imge5 = PhotoImage(file = 'tayloreraposter.png')
    taylor=Button(content_frame,image=imge5,command=swift)#command=call
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
    content_frame.after(1000,animate_label, txt)

    '''# To add design to mainscreen
    image2 = Image.open("mainscreen extra.png")
    resize_image = image2.resize((1300, 100))
    test2 = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=test2)
    label1.image = test2
    # Position image
    label1.place(x=0, y=450)'''







    ###########################################################################


    #Hi_Shikha
    
    turn_on =Button(content_frame,text="LOG OUT", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="brown",command=logg_destroy)
    turn_on.place(x=900, y=36)
    l=Label(content_frame, text="Welcome {}!! ".format(username_varify.get()),bg="gray28", fg="white", font= ('Poplar Std', 20))
    l.place(x=1020, y=36)
    #win_label= Label(content_frame, text= "Hi SHIKHA!!", font= ('Verdana bold', 14), fg= "black",bg="bisque3")
    #win_label.place(x=1115, y=40)
    turn_on.pack

        

    ###########################################################################
    image4 = Image.open("home_page_logo.png")
    test3 = ImageTk.PhotoImage(image4)
    label1s = tk.Label(parent,image=test3)
    label1s.image = test3
    #label1s.image = test
    # Position image
    #label1s.place(x=20, y=21)
    canvas.create_window(20, 50, window=label1s, anchor='w')

    '''# Create a photoimage object of the image in the path
    image1 = Image.open("home_page_logo.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    # Position image
    #label1.place(x=20, y=19)
    canvas.create_window(30, 50, window=label1, anchor='w') '''



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



    #########bisque3

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


    #Hi_Shikha
    turn_on = Button(content_frame, text="<-BACK", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="brown",command=parent.destroy)
    turn_on.place(x=900, y=36)
    l=Label(content_frame, text="Welcome {}!! ".format(username_varify.get()),bg="gray28", fg="white", font= ('Poplar Std', 20))
    l.place(x=1020, y=36)
    turn_on.pack

        

    ###########################################################################
    # Create a photoimage object of the image in the path
    image2 = Image.open("home_page_logo.png")
    test2 = ImageTk.PhotoImage(image2)
    label1s = tk.Label(parent,image=test2)
    #label1s.image = test
    # Position image
    label1s.place(x=20, y=21)
    '''image1 = Image.open("home_page_logo.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    # Position image
    #label1.place(x=20, y=19)
    canvas.create_window(30, 50, window=label1, anchor='w')'''
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
    dunki=Button(content_frame,image=imge7,command=dunki)#command=call
    dunki.place(x=270, y=610)

    imge8 = PhotoImage(file = 'animalposter.png')
    animal=Button(content_frame,image=imge8,command=animal)#command=call
    animal.place(x=510, y=610)

    imge9 = PhotoImage(file = 'sambahadurposter.png')
    sam=Button(content_frame,image=imge9,command=sam)#command=call
    sam.place(x=770, y=610)

    imge10 = PhotoImage(file = '12failposter.png')
    fail=Button(content_frame,image=imge10,command=fail)#command=call
    fail.place(x=1030, y=610)

    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))

    parent.mainloop()






    

main_screen()
root.mainloop()


