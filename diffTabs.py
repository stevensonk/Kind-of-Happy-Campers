from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk, ImageGrab
import time

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        # Create a GUI and name it
        self.root = Tk()
        self.root.title = 'EyePaint'
        # Create a notebook for different tabs
        self.tabControl = ttk.Notebook(self.root)

        # Create two tabs:
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Tab 1')
        self.tabControl.add(self.tab2, text='Save')
        self.tabControl.pack(expand=1, fill="both")

        # Button to switch between tabs:
        self.switch_button = Button(self.tab1, text='Switch Tab', command=self.switch_tab)
        self.switch_button.grid(row=0, column=5)

        # Save Button
        self.save_button = Button(self.tab1, text='Save', command=self._snapsaveCanvas)
        self.save_button.grid(row=0, column=6)

        self.pen_button = Button(self.tab1, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.tab1, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.tab1, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.tab1, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.tab1, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.tab1, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        # TAB 2: SAVE
        self.label1 = Label(self.tab2, text='Save File')
        self.label2 = Label(self.tab2, text='Filename:')
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.filename = StringVar()
        self.filename = 'filename'
        self.ask_filename = Entry(self.tab2, textvariable=self.filename)
        self.ask_filename.grid(row=1, column=1)
        self.get_filename = Button(self.tab2, text = 'Save', command = self._snapsaveCanvas)
        self.get_filename.grid(row=2,column=0)
        self.return_from_save = Button(self.tab2, text = 'Return', command = self.switch_tab)
        self.return_from_save.grid(row=2, column=1)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def switch_tab(self):
        self.tabControl.select(self.tab2)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND,smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def save(self):
        x=self.root.winfo_rootx()+self.c.winfo_x()
        y=self.root.winfor_rooty()+self.c.winfo_y()
        x1=x+self.c.winfo_width()
        y1=y+self.c.winfo_height()
        ImageGrab.grab()

    def _snapsaveCanvas(self):
        #self.tabControl.select(self.tab1)
        canvas = self._canvas()  # Get Window Coordinates of Canvas
        # Create a Popup window
        # self.popup = Toplevel(self.tab1)
        # self.popup.title('Save')
        # Ask for Title for save file
        # self.tabControl.select(self.tab1)
        #self.filename = self.ask_filename.get()
        #print(self.filename)
        self.get_name()
        savename = self.filename + ".jpg"
        print(savename)
        time.sleep(1)
        self.grabcanvas = ImageGrab.grab(bbox=canvas).save(savename)
        #print('Screencshot tkinter canvas and saved as "out_snapsave.jpg w/o displaying screenshoot."')

    def _canvas(self):
        x=self.root.winfo_rootx()+self.c.winfo_x()
        y=self.root.winfo_rooty()
        x1=x+800
        y1=y+800
        #x1=x+self.c.winfo_width()
        #y1=y+self.c.winfo_height()
        box=(x,y,x1,y1)
        return box

    def get_name(self):
        self.filename = self.ask_filename.get()
        print(self.filename)
        savename = self.filename + ".jpg"
        print(savename)
        self.tabControl.select(self.tab1)


if __name__ == '__main__':
    Paint()