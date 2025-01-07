from tkinter import*
from tkinter import messagebox,ttk
import random
from tkcalendar import DateEntry
from datetime import date

root=Tk()
root.title('TICKET CALCULATOR')
root.geometry('1280x720')
bg_color='gray28'


#=================variables================
person=IntVar()
c_name=StringVar()
c_phone=StringVar()
ticket_no=StringVar()
#======================================Frames=================

def varify():
    global dis
    p = person.get()
    if c_name.get() != "" or c_phone.get() != "":
        if c_phone.get().isnumeric() is not True:
            messagebox.showerror('Error','Phone number should be integer')
            return
    else:
        messagebox.showerror("Error", "User details are must")
        return
    messagebox.showinfo('Varified','Successfully Vairified')

def gticket():
    try:
        welcome()
        p=person.get()
        textarea.insert(END, f"\n {p} person ")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\nAmount :\t\t{p*100}")
        textarea.insert(END,f"\nYou can show your ticket number and select")
        textarea.insert(END, f"\nyour seats at CINETICKET theatre :) ")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\n\n {55*'*'}")
        #save_ticket()
    except Exception:
        messagebox.showwarning('Warning','Please varify the details first')
        clear()

def clear():
    c_name.set('')
    c_phone.set('')
    person.set(0)
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()

'''def save_ticket():
    op=messagebox.askyesno("Save ticket","Do you want to download ticket ?")
    if op>0:
        ticket_details=textarea.get(1.0,END)
        f1=open("bills/"+str(ticket_no.get())+".txt","w")
        f1.write(ticket_details)
        f1.close()
        messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
    else:
        return'''

def welcome():
    x = random.randint(1000, 9999)
    ticket_no.set(str(x))
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t  RECEIPT")
    textarea.insert(END,f"\n\nTicket Number:\t\t {    ticket_no.get()}")
    textarea.insert(END,f"\nName:\t\t  {    c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t    {    c_phone.get()}")
    
    #textarea.insert(END,f"\nDate:\t\t    {    date.get()}")
    textarea.configure(font='arial 15 bold')


title=Label(root,pady=2,text="CINETICKET",bd=12,bg=bg_color,fg='orange',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Details',font=('times new romon',15,'bold'),fg='white',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Name',font=('times new romon',18,'bold'),bg=bg_color,fg='orange').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='orange').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Tickets', font=('times new romon', 18, 'bold'), fg='white',bg=bg_color)
F2.place(x=20, y=180,width=630,height=500)

n= Label(F2, text='Number of tickets', font=('times new romon',18, 'bold'), bg=bg_color, fg='orange').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=person, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,pady=20)


'''d=Label(F2, text='Booking Date', font=('times new romon',18, 'bold'), bg=bg_color, fg='orange').grid(row=3, column=0, padx=30, sticky='w', pady=10)
#d_txt =DateEntry(F2,selectmode='day', textvariable=ticket_date).grid(row=3, column=1)
d_txt =DateEntry(F2, width=20,textvariable=date, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=3, column=1, padx=10,pady=30)'''


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
btn1=Button(F2,text='Varify',font='arial 15 bold',command=varify,padx=5,pady=10,bg='lightgreen',width=15)
btn1.place(x=70, y=200)
#btn1.grid(row=3,column=0,padx=10,pady=200)
btn2=Button(F2,text='Ticket',font='arial 15 bold',command=gticket,padx=5,pady=10,bg='lightgreen',width=15)
btn2.place(x=350, y=200)
#btn2.grid(row=3,column=1,padx=10,pady=200)
#btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='lightgreen',width=15)
#btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='lightgreen',width=15)
btn4.place(x=200, y=300)

root.mainloop()
