import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

root.title('Tkinter Window Demo')
root.geometry('1300x990')
root.configure(bg='blue')
root.resizable(False, False)


videoplayer = TkinterVideo(master=root, scaled=True)

videoplayer.load("logo_v.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()



