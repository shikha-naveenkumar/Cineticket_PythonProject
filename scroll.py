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
#root.destroy()
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
