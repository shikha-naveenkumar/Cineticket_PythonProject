import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tigermovie import tgrmv
from swift import swift
from marvel import marvel
from japanmovie import japan
from jigarthanda import jigar
from napolean import nap
from wish import wish
from wonka import wonka
from dunki import dunki
from animal import animal
from sam import sam
from fail import fail

def movie():
    class TwoColoredFrame(tk.Frame):
        def __init__(self, master, bg1, bg2, fraction=0.5, **kw):
            kw["bg"] = bg2  # color of the lower part of the Frame
            tk.Frame.__init__(self, master, **kw)
            # upper color stripe 
            tk.Frame(self, bg=bg1).place(relx=0, rely=0, relwidth=1, relheight=fraction)

            
    # Create the main window
    parent = tk.Tk()
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
    turn_on = Button(content_frame, text="LOG OUT", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="brown",command=parent.destroy)
    turn_on.place(x=999, y=36)
    '''win_label= Label(content_frame, text= "Hi SHIKHA!!", font= ('Verdana bold', 14), fg= "black",bg="bisque3")
    win_label.place(x=1115, y=40)'''
    turn_on.pack

        

    ###########################################################################
    # Create a photoimage object of the image in the path
    image1 = Image.open("home_page_logo.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    # Position image
    #label1.place(x=20, y=19)
    canvas.create_window(30, 50, window=label1, anchor='w')
    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))
    ################################################################################
    #ENG MOVIES
    win_label= Label(content_frame, text= "ENGLISH MOVIES", font= ('Verdana bold', 30), fg= "black",bg="bisque3")
    win_label.place(x=20, y=100)

    #global imge2
    self.imge2 = PhotoImage(file = 'marvelsposter.png')
    marvel=Button(content_frame,image=imge2,command=marvel)#command=call
    marvel.place(x=20, y=160)

    #global imge5
    self.imge5 = PhotoImage(file = 'tayloreraposter.png')
    taylor=Button(content_frame,image=imge5,command=swift)#command=call
    taylor.place(x=280, y=160)

    #global imge1
    self.imge1 = PhotoImage(file = 'napoleanposter.png')
    taylor=Button(content_frame,image=imge1,command=nap)#command=call
    taylor.place(x=540, y=160)

    #global imge3
    self.imge3 = PhotoImage(file = 'wishposter.png')
    taylor=Button(content_frame,image=imge3,command=wish)#command=call
    taylor.place(x=800, y=160)

    #global imge4
    self.imge4 = PhotoImage(file = 'wonkaposter.png')
    taylor=Button(content_frame,image=imge4,command=wonka)#command=call
    taylor.place(x=1060, y=160)

    win_label= Label(content_frame, text= "HINDI MOVIES", font= ('Verdana bold', 30), fg= "black",bg="bisque3")
    win_label.place(x=20, y=620)

    #global imge6
    self.imge6 = PhotoImage(file = 'tiger2poster.png')
    tiger=Button(content_frame,image=imge6,command=tgrmv)#command=call
    tiger.place(x=20, y=680)

    #global imge7
    self.imge7 = PhotoImage(file = 'dunkiposter.png')
    dunki=Button(content_frame,image=imge7,command=dunki)#command=call
    dunki.place(x=280, y=680)

    #global imge8
    self.imge8 = PhotoImage(file = 'animalposter.png')
    animal=Button(content_frame,image=imge8,command=animal)#command=call
    animal.place(x=540, y=680)

    #global imge9
    self.imge9 = PhotoImage(file = 'sambahadurposter.png')
    sam=Button(content_frame,image=imge9,command=sam)#command=call
    sam.place(x=800, y=680)

    #global imge10
    self.imge10 = PhotoImage(file = '12failposter.png')
    fail=Button(content_frame,image=imge10,command=fail)#command=call
    fail.place(x=1060, y=680)

    # Configure the scrollable region of the canvas
    content_frame.update_idletasks()  # Update the frame to get the correct size
    canvas.configure(scrollregion=canvas.bbox("all"))

    parent.mainloop()


