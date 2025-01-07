from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,ttk
import random
from tkcalendar import DateEntry
from datetime import date
import mysql.connector
global test
global test2

####### cming from QR Code ###
import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import tkinter as tk
import re # Importing re module
import mysql.connector

################
def sam():
    class TwoColoredFrame(tk.Frame):
        def __init__(self, master, bg1, bg2, fraction=0.5, **kw):
            kw["bg"] = bg2  # color of the lower part of the Frame
            tk.Frame.__init__(self, master, **kw)
            # upper color stripe 
            tk.Frame(self, bg=bg1).place(relx=0, rely=0, relwidth=1, relheight=fraction)
    # connecting to database added by Medha
    db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
    mycur = db.cursor()
    #cursor.execute("DROP TABLE ticket1 ")
    mycur.execute("CREATE TABLE IF NOT EXISTS ticket1 (act_usr Varchar(100),name Varchar(100), ticket_id Varchar(20) PRIMARY KEY, ticket_date Varchar(100), Movie_name Varchar(100), Amount Varchar(30))")

    # fetching database
    global active_usr
    mycur.execute('SELECT act_usr FROM Active_usr')
    active_usr = mycur.fetchall()
    #messagebox.showinfo('Active User Value',active_usr)
    # Medha code ends here for DB connection and active user retrival


    # Create the main window
    parent = tk.Toplevel()
    parent.title("SAMBAHADUR")
    parent.geometry('1300x990')
    parent.resizable(True, True)
    #########
    frame = TwoColoredFrame(parent, width=100, height=100, bg2='antiquewhite1', bg1="gray28", fraction=0.10)
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
    #to make movie content
    win_label= Label(parent, text= "DESCRIPTION : Revolves around the high and low points of Sam Manekshaw who became the first Indian Army officer.", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=500)
    win_label= Label(parent, text= "Cast: Fatima Sana Shaikh ,Vicky Kaushal, Sanya Malhotra", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=530)
    win_label= Label(parent, text= "Director: Meghna Gulzar", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=560)
    win_label= Label(parent, text= "Producer: Ankita Chowfin", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=590)
    win_label= Label(parent, text= "Co-Producer: Pashan Jal", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=620)
    win_label= Label(parent, text= "Screenplay: Zahoor Qadir", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=650)
    win_label= Label(parent, text= "Director Of Photography: Jay I. Patel", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=680)
    win_label= Label(parent, text= "Music: Ehsaan Noorani", font= ('Roman', 17), fg= "black",bg="antiquewhite3")
    win_label.place(x=25, y=710)
    turn_on = Button(parent, text="MAINSCREEN", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="gray27",command=parent.destroy)
    turn_on.place(x=920, y=700)
    turn_on = Button(parent, text="BOOK TICKETS", font= ('Poplar Std', 15), fg= "antiquewhite1",bg="gray27",command=ticket)
    turn_on.place(x=1080, y=700)
    ###########################################################################
    # Create a photoimage object of the image in the path
    image2 = Image.open("home_page_logo.png")
    test2 = ImageTk.PhotoImage(image2)
    label1 = tk.Label(parent,image=test2)
    # Position image
    label1.place(x=20, y=21)
    image1 = Image.open("sammain.png")
    test = ImageTk.PhotoImage(image1)
    label1s = tk.Label(parent,image=test)
    # Position image
    label1s.place(x=350, y=110) 
    ############################################################################
    parent.mainloop()
def ticket():
    root=tk.Toplevel()
    root.title('TICKET CALCULATOR')
    root.geometry('1280x720')
    bg_color='gray28'
    dates = ['11-01-2024', '12-01-2024','13-01-2024', '14-01-2024','15-01-2024',
        '16-01-2024','17-01-2024','18-01-2024']
    movies = ['Sam Bahadur']
    #=================variables================
    person=IntVar()
    c_name=StringVar()
    c_phone=StringVar()
    ticket_no=StringVar()
    #======================================Frames=================
    def varify():
        global dis
        p = person.get()
        fs = open("marvel.txt",'r')
        con =int(fs.read(3))
        fs.close()
        n1= c_phone.get()    #input('Enter Mobile number :')  # Reading input from the user
        r=re.fullmatch('[6-9][0-9]{9}',n1) # calling fullmatch function by passing pattern and n
        if c_name.get() != "" or c_phone.get() != "":
            if c_phone.get().isnumeric() is not True:
                messagebox.showerror('Error','Phone number should be integer')
                return
            if r==None:
                messagebox.showerror('Error','Phone number should be 10 digits long')
                return
            ### Added by Medha to check the number of Tickets
            if p == 0 :
                messagebox.showerror('Error','Number of Tickets cannot be Zero')
                return
            if p - con > 0 :
                messagebox.showerror('Error','Your Booking number Exeeds available seats')
                person.set(0)
                return
        else:
            messagebox.showerror("Error", "User details are must")
            return
        messagebox.showinfo('Varified','Successfully Vairified')
        n_txt['state']=DISABLED
        cname_txt['state']=DISABLED
        cphone_txt['state']=DISABLED
        combo_s['state']=DISABLED
    ## Added by Medha to active the next button
        btn2['state']=NORMAL
        btn1['state']=DISABLED
    ##################
    fs = open("sam.txt",'r')
    con =int(fs.read(3))
    fs.close()
    st=str(con)
    def gticket():
        try:
            welcome()
            p=person.get()
            textarea.insert(END, f"\n {p} person ")
            textarea.insert(END, f"\n {35*'='}")
            textarea.insert(END, f"\nAmount :\t\t{p*120}")
            textarea.insert(END,f"\nYou can show your ticket number and select")
            textarea.insert(END, f"\nyour seats at CINETICKET theatre :) ")
            textarea.insert(END, f"\n {35*'='}")
            textarea.insert(END, f"\n\n {55*'*'}")
            textarea.config(state= DISABLED)
            fs = open("sam.txt",'r')
            con =int(fs.read(3))
            fs.close()
            new_seat_availability = con-p
            st=str(con)
            fs = open("sam.txt",'w')
            fs.write(str(new_seat_availability))
            fs.close()
        except Exception:
            messagebox.showwarning('Warning','Please varify the details first')
            clear()
        #### Added By Medha
        btn3['state']=NORMAL
        btn2['state']=DISABLED
        ####################
    def clear():
        c_name.set('')
        c_phone.set('')
        combo_s.set('select Date')
        person.set(0)
        welcome()
    def exit():
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            root.destroy()  
    def welcome():
        x = random.randint(1000, 9999)
        ticket_no.set(str(x))
        textarea.delete(1.0,END)
        textarea.insert(END,"\t\t  RECEIPT")
        textarea.insert(END,f"\n\nTicket Number:\t\t {    ticket_no.get()}")
        textarea.insert(END,f"\nName:\t\t  {    c_name.get()}")
        textarea.insert(END,f"\nPhone Number:\t\t    {    c_phone.get()}")
        textarea.insert(END, f"\n\n Date :\t\t      {combo_s.get()}")
        textarea.insert(END, f"\n\n Movie :\t\t      {combo_s2.get()}")
        textarea.configure(font='arial 15 bold')
    title=Label(root,pady=2,text="CINETICKET",bd=12,bg=bg_color,fg='orange',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
    title.pack(fill=X)
    #=================Product Frames=================
    F1=LabelFrame(root,bd=10,relief=GROOVE,text='Details',font=('times new romon',15,'bold'),fg='white',bg=bg_color)
    F1.place(x=0,y=80,relwidth=1)

    cname_lbl=Label(F1,text='Name',font=('times new romon',18,'bold'),bg=bg_color,fg='orange').grid(row=0,column=0,padx=20,pady=5)
    cname_txt=Entry(F1,width=15,state='normal',textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7)
    cname_txt.grid(row=0,column=1,padx=10,pady=5)

    cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='orange').grid(row=0,column=2,padx=20,pady=5)
    cphone_txt=Entry(F1,width=15,state='normal',font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7)
    cphone_txt.grid(row=0,column=3,padx=10,pady=5)

    available=Label(F1,text='Available seats',font=('times new romon',18,'bold'),bg=bg_color,fg='orange').grid(row=0,column=6,padx=20,pady=5)
    available=Label(F1,text=st,font=('times new romon',18,'bold'),bg=bg_color,fg='orange').grid(row=0,column=8,padx=20,pady=5)

    F2 = LabelFrame(root, text='Tickets', font=('times new romon', 18, 'bold'), fg='white',bg=bg_color)
    F2.place(x=20, y=180,width=630,height=500)

    n= Label(F2, text='Number of tickets', font=('times new romon',18, 'bold'), bg=bg_color, fg='orange').grid(
    row=2, column=0, padx=30, pady=20)
    n_txt = Entry(F2, width=20,state='normal',textvariable=person, font='arial 15 bold', relief=SUNKEN, bd=7)
    n_txt.grid(row=2, column=1, padx=10,pady=20)

    source= Label(F2, text='Date', font=('times new roman',18, 'bold'), bg=bg_color, fg='orange').grid(
    row=0, column=0, padx=30, pady=20)
    combo_s=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=dates)
    combo_s.grid(row=0,column=1,pady=10)
    #combo_s.set('select date')
    combo_s.set(dates[0])

    source= Label(F2, text='Movie name', font=('times new roman',18, 'bold'), bg=bg_color, fg='orange').grid(
    row=3, column=0, padx=30, pady=20)
    combo_s2=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=movies)
    combo_s2.grid(row=3,column=1,pady=10)
    combo_s2.set(movies[0]) #'select movie'
    combo_s2['state']=DISABLED
################ CODE FOR QR CODE ################
    def logg_destroy():
        roop.destroy()
        Payment()
        
    def Verify_Txid():
        global n
        global s
        n= transaction_id.get()    #input('Enter Mobile number :')  # Reading input from the user
        r=re.fullmatch('[6-9][0-9]{9}',n) # calling fullmatch function by passing pattern and n
        if r!=None: # checking whether it is none or not 
         if str(n)==str(s):
             messagebox.showinfo('Success!!', 'Success!! You will be redirected to the Booking Screen')
             win.destroy()
             try:
                db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
                mycur = db.cursor()
                #messagebox.showinfo('Username found',sql_s)
                #Amt = str(Amt,encoding='utf-8')
                p1 = person.get()
                #p1 = n_txt.get()
                Amt = int(p1)
                Amt1 = Amt *120
                mycur.execute("INSERT INTO ticket1 VALUES ('{}','{}', '{}', '{}','{}','{}','{}');".format ('UTF',str(c_name.get()), str(ticket_no.get()), str(combo_s.get()),str(combo_s2.get()),'QTY',str(n)))
                db.commit()
                mycur.execute("update ticket1 set Amount =" +str(Amt1)+ " where act_usr = 'UTF';")
                db.commit()
                mycur.execute("update ticket1 set act_usr = (select act_usr from Active_usr) where act_usr = 'UTF';")
                db.commit()
                #show_message('Successful', 'Your booking is successful, your ticket id is {}'.format(ticket_id.get()))
                #root.destroy()
             except mysql.connector.Error as e:
                show_message('Error', e)
             finally:
                db.close()
                messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
                btn3['state']=DISABLED
             

         elif str(n)!=str(s):
            messagebox.showinfo('ERROR!!', 'Not a valid Transaction ID....Try again.')
        else:
            messagebox.showinfo('ERROR!!', 'Not a valid Transaction ID....Try again.')
            

    def Payment():
        #root.destroy
        global img
        global win
        global s
        #win = Tk()
        win =Toplevel()
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
        ### QR CODE GENERATION###
        global img
        img = ImageTk.PhotoImage(Image.open("qr-img1.png"))
        # creating a QRCode object  
        obj_qr = qrcode.QRCode(  
            version = 1,  
            error_correction = qrcode.constants.ERROR_CORRECT_L,  
            box_size = 6,  
            border = 2)
        s = random.randint(6666666666, 9999999999)
        # using the add_data() function
        scrpt= "MedhaShikha@axl Amount : " + str(Amt1)+ ",Transaction id :"+str(s)
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

    def terms_accept():
        global roop
        roop = Tk()

        # specify size of window.
        roop.geometry("560x270")
         
        # Create text widget and specify size.
        T = Text(roop, height = 9, width = 87)
         
        # Create label
        l = Label(roop, text = "Terms and Conditions")
        l.config(font =("Courier", 20))
         
        Fact = """1> The Amount paid should be credited within 2 Hrs from the
        Transaction else the Booking will be automatiocally cancelled
        2> There will be no refund once the ticket is booked
        3> No Show does not entitle for any refund of Ticket price
        4> Cinimas reservers the right to cancel the booking anytime"""
         
        # Create button for next text.
        b1 = Button(roop, text = "Accept", command=logg_destroy)

         
        # Create an Exit button.
        b2 = Button(roop, text = "Decline",
                    command = roop.destroy) 
         
        l.pack()
        T.pack()
        b1.pack()
        b2.pack()
         
        # Insert The Fact.
        T.insert(tk.END, Fact)
        T.config(state= DISABLED)


        roop.mainloop()

################ CODE FOR QR CODE ENDS HERE #########
    def save_ticket():
        op=messagebox.askyesno("Pay & save", "You will be directed to the payment screen!")
        if op>0:
            db = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="techienaman")
            mycur = db.cursor()
            ticket_details="insert into bookings2 values('{}','{}')".format(str(c_name.get()),textarea.get(1.0,END))
            mycur.execute(ticket_details)
            db.commit()
            ########## Added Here by Medha #####
            mycur.execute("DELETE FROM MOVIE_AMT ")
            db.commit()
            p1 = person.get()
            global Amt1
            Amt = int(p1)
            Amt1 = Amt *120
            cur_details="insert into MOVIE_AMT values('{}','{}','{}')".format(str(movies[0]),str(Amt1),'TXN')
            mycur.execute(cur_details)
            db.commit()
            #QR_CODE()
            #messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
            terms_accept()
            #messagebox.showinfo('Back!!','We are Back')
        else:
            return
   #========================Ticket area================
    F3=Frame(root,relief=GROOVE,bd=10)
    F3.place(x=700,y=180,width=500,height=500)

    bill_title=Label(F3,text='Ticket',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
    scrol_y=Scrollbar(F3,orient=VERTICAL)
    textarea=Text(F3,yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    welcome()
    #=========================Buttons======================
    btn1=Button(F2,text='Verify',font='arial 15 bold',command=varify,bg='lightgreen',width=15)
    btn1.place(x=70, y=300)
    btn2=Button(F2,text='Ticket',font='arial 15 bold',command=gticket,bg='lightgreen',width=15)
    btn2.place(x=350, y=300)
    btn3=Button(F2,text='Pay & Save',font='arial 15 bold',command=save_ticket,bg='lightgreen',width=15)
    btn3.place(x=70, y=400)
    btn4=Button(F2,text='Exit',font='arial 15 bold',command=exit,bg='lightgreen',width=15)
    btn4.place(x=350, y=400)
    ### Medha added code for disabling the buttons
    btn2['state']=DISABLED
    btn3['state']=DISABLED
    ### End of Code
    root.mainloop()





