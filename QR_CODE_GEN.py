# importing the qrcode module  
import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import tkinter as tk
import re # Importing re module
import mysql.connector

def QR_CODE():
    # connecting to database added by Medha
    db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
    mycur = db.cursor()
    global amt
    mycur.execute('SELECT act_amt FROM MOVIE_AMT')
    amt = mycur.fetchall()
    #messagebox.showinfo('Amount', amt)

    #def QR_CODE():

    def logg_destroy():
        root.destroy()
        Payment()

    def Verify_Txid():
        n= transaction_id.get()    #input('Enter Mobile number :')  # Reading input from the user
        r=re.fullmatch('[6-9][0-9]{9}',n) # calling fullmatch function by passing pattern and n
        if r!=None: # checking whether it is none or not 
         #print('Valid Number')
         mycur.execute('Update MOVIE_AMT set tx_id = '+n)
         db.commit()
         db.close()
         messagebox.showinfo('Success!!', 'Success!! You will be redirected to the Booking Screen')
         #return
         win.destroy()
        else:
         messagebox.showinfo('Alert!!','Not a valid Transaction Id Try again')


    ############################ Code for Payment Screen here #########################
    # Define the geometry of the window
    def Payment():
        #root.destroy
        global img
        global win
        #win = Tk()
        win =tk.Toplevel()
        win.geometry('800x750+300+20')
        win.configure(bg="antiquewhite1")
        win.resizable(False,False)

        frame = Frame(win, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        win_label= Label(win, text= "Payment form", font= ('Verdana bold', 50), fg= "black",bg="bisque3")
        win_label.place(x=120, y=40)

        done=Button(win,text="Done",bg="yellow",font= ('Verdana bold', 10),width=13,height=3, command=Verify_Txid)
        done.place(x=200, y=590)

        cancel=Button(win,text="cancel",bg="orange",font= ('Verdana bold', 10),width=13,height=3,command=win.destroy)
        cancel.place(x=400, y=590)
        #done=Button(win,text="Done", height=22,width=30,bg='white',highlightthickness = 0, bd = 0,command=toggle_passwordd)
        #done.place(x=320,y=172)

        scan= Label(win, text= "Scan QR code", font= ('Verdana bold', 30), fg= "black",bg="bisque3")
        scan.place(x=240, y=170)
        global transaction_id
        transaction_label=Label(win,text='Enter Transaction ID:',font=('times new romon',18,'bold'),bg="bisque3",fg='black')
        transaction_label.place(x=180, y=530)
        transaction_id=Entry(win,width=15,textvariable=transaction_label,state='normal',font='arial 15 bold',relief=SUNKEN,bd=7)
        transaction_id.place(x=430, y=530)


        # Create an object of tkinter ImageTk
        global img
        img = ImageTk.PhotoImage(Image.open("qr-img1.png"))
    ############################################################################
        # Create a Label Widget to display the text or Image


        #from typing_extensions import Required
        # creating a QRCode object  
        obj_qr = qrcode.QRCode(  
            version = 1,  
            error_correction = qrcode.constants.ERROR_CORRECT_L,  
            box_size = 8,  
            border = 4)  
        # using the add_data() function
        scrpt= "MedhaShikha@axl Amount : " + str(amt)
        #messagebox.showinfo('Validated', scrpt)
        obj_qr.add_data(scrpt)  
        # using the make() function  
        obj_qr.make(fit = True)  
        # using the make_image() function  
        qr_img = obj_qr.make_image(fill_color = "cyan", back_color = "black")  
        # saving the QR code image  
        qr_img.save("qr-img1.png")
        img = ImageTk.PhotoImage(Image.open("qr-img1.png"))
        label = Label(frame, image=img)
        label.pack()

        win.mainloop()
    ##############################################################################
    # Create an instance of tkinter window


    ###################### Code for Terms and Conditions ############################
    global root
    root = Tk()

    # specify size of window.
    root.geometry("550x270")
     
    # Create text widget and specify size.
    T = Text(root, height = 9, width = 82)
     
    # Create label
    l = Label(root, text = "Terms and Conditions")
    l.config(font =("Courier", 20))
     
    Fact = """1> The Amount paid should be credited within 2 Hrs from the
    Transaction else the Booking will be automatiocally cancelled
    2> There will be no refund once the ticket is booked
    3> No Show does not entitle for any refund of Ticket price
    4> Cinimas reservers the right to cancel the booking anytime"""
     
    # Create button for next text.
    b1 = Button(root, text = "Accept", command=logg_destroy)

     
    # Create an Exit button.
    b2 = Button(root, text = "Decline",
                command = root.destroy) 
     
    l.pack()
    T.pack()
    b1.pack()
    b2.pack()
     
    # Insert The Fact.
    T.insert(tk.END, Fact)

    root.mainloop()

    ########################### Code Ends Here ########################################



