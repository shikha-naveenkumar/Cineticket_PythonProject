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
from moviespage import movie
##def home():
##    global img
##    global img2
##    global img3
##    global imge1
##    global imge2
##    global imge3
##    global imge4
##    global imge5

class TwoColoredFrame(tk.Frame):
    def __init__(self, master, bg1, bg2, fraction=0.5, **kw):
        kw["bg"] = bg2  # color of the lower part of the Frame
        tk.Frame.__init__(self, master, **kw)
        # upper color stripe 
        tk.Frame(self, bg=bg1).place(relx=0, rely=0, relwidth=1, relheight=fraction)

        
# Create the main window
parent = tk.Tk()
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
movies= Button(content_frame, text="MOVIES",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=movie)
movies.place(x=200, y=40)
Button.pack(expand = True)
'''stream= Button(content_frame, text="STREAM",font= ('Poplar Std', 10), fg= "antiquewhite1",bg="gray32",command=call)
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
marvel=Button(content_frame,image=imge2,command=marvel)#command=call
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




