from tkinter import *
import cv2
import numpy as np
import pyautogui
import threading
import os
import time

#create output folder
if not os.path.exists('output'):
    os.makedirs('output')

window = Tk()
window.title("Py Screen Recorder")
window.geometry('350x200')
window.configure(bg='white')

lbl = Label(window, text="Welcome to Py Screen Recorder", font=("Arial Bold", 12), bg='white')
lbl.place(bordermode=OUTSIDE, x=10, y=10, height=50, width=350)

global r 
r = False

def record():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    SCREEN_SIZE = (screen_width, screen_height)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    #output filename
    filename = 'output/'+time.strftime("%Y%m%d-%H%M%S")+'.avi'
    out = cv2.VideoWriter(filename, fourcc, 20.0, (SCREEN_SIZE))
    global r
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if r==False:
            break

def clicked():
    global r
    if r == False:
        lbl.configure(text="Recording Started...")
        btn.configure(text="Stop")
        r=True
        th = threading.Thread(target=record)
        th.start()
    else:
        lbl.configure(text="Recorded")
        btn.configure(text="Start Recorder")
        r=False

def exitapp():
    global r
    r=False
    window.destroy()

btn = Button(window, text="Start Recorder", command=clicked, bg='#eeeeee',borderwidth= 0,foreground = '#000000')
btn.place(bordermode=OUTSIDE, x=20, y=60, height=50, width=310)

btnexit = Button(window, text="Exit", command=exitapp, bg='#ee0000',borderwidth= 0,foreground = '#ffffff')
btnexit.place(bordermode=OUTSIDE, x=20, y=120, height=50, width=310)

window.mainloop()