

from tkinter import *
from tkinter import ttk





def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y),
                      fill=color,
                      width=2)
    lasx, lasy = event.x, event.y

app = Tk()
app.geometry("400x400")
canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)


canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)


def blueCallBack():
   color='blue'

B = ttk.Button(app, text ="Blue", command = blueCallBack)

B.pack()

app.mainloop()