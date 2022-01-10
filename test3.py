from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import ImageGrab

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title = 'EyePaint'
        self.tabControl = ttk.Notebook(self.root)

        # Create new tabs:
        self.tab1 = ttk.Frame(self.tabControl)  # Tab 1, for Drawing (main screen)
        self.tab2 = ttk.Frame(self.tabControl)  # Tab 2, for Color Selection
        self.tab3 = ttk.Frame(self.tabControl)  # Tab 3, for Tool Selection
        self.tab4 = ttk.Frame(self.tabControl)  # Tab 4, for Thickness Selection
        self.tabControl.add(self.tab1, text='Drawing')
        self.tabControl.add(self.tab2, text='Colors')
        self.tabControl.add(self.tab3, text='Tool')
        self.tabControl.add(self.tab4, text='Thickness')
        self.tabControl.pack(expand=1, fill="both")

        #self.switch_button = Button(self.tab1, text='Switch Tab', command=self.switch_tab)
        #self.switch_button.grid(row=0, column=5)

        ## TAB 1: DRAWING
        # The canvas for drawing:
        self.c = Canvas(self.tab1, bg='white', width=600, height=600)
        self.c.pack(side = LEFT, fill=BOTH, expand=1)

        # Button on tab1 that moves to tab2 so that COLOR can be selected
        color_button_png = PhotoImage(file='color_button.png')
        self.color_button = Button(self.tab1, image = color_button_png, command=self.choose_color)
        self.color_button.pack(side=TOP,pady=50)

        # Button on tab1 that moves to tab 3 so that TOOL can be selected
        self.tool_button = Button(self.tab1, text='Tool', command=self.choose_tool)
        self.color_button.pack(side=TOP,pady=50)

        # Eraser Button
        eraser_button_png = PhotoImage(file='eraser_button.png')
        self.eraser_button = Button(self.tab1, image = eraser_button_png, command=self.use_eraser)
        self.eraser_button.pack(side=TOP,pady=50)

        # Size Selection
        self.choose_size_button = Scale(self.tab1, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.pack(side=TOP,pady=50)

        # Save Button- CURRENTLY DOES NOTHING
        # TODO: fix save problem
        self.save_button = Button(self.tab1, text='Save', command=self.snapsave)
        self.save_button.pack(side=TOP,pady=50)

        ## TAB 2: COLORS
        # TODO: Add more colors
        self.redColor = Button(self.tab2, text='red', bg='red', width=20, height=10, command=self.colorRed)
        self.redColor.place(relx=0, rely=0,anchor=NW)

        self.blueColor = Button(self.tab2, text='blue', bg='blue', width=20, height=10, command=self.colorBlue)
        self.blueColor.place(relx=.32, rely=0,anchor=N)

        self.yellowColor = Button(self.tab2, text='yellow', bg='yellow', width=20, height=10, command=self.colorYellow)
        self.yellowColor.place(relx=.64, rely=0,anchor=NE)

        self.greenColor = Button(self.tab2, text='green', bg='green', width=20, height=10, command=self.colorGreen)
        self.greenColor.place(relx=0, rely=.4,anchor=W)

        self.orangeColor = Button(self.tab2, text='orange', bg='orange', width=20, height=10, command=self.colorOrange)
        self.orangeColor.place(relx=.32, rely=.4,anchor=CENTER)

        self.purpleColor = Button(self.tab2, text='purple', bg='purple', width=20, height=10, command=self.colorPurple)
        self.purpleColor.place(relx=.64, rely=.4,anchor=E)

        self.blackColor = Button(self.tab2, text='black', bg='black', fg='white', width=20, height=10, command=self.colorBlack)
        self.blackColor.place(relx=0, rely=.8,anchor=SW)

        self.greyColor = Button(self.tab2, text='grey', bg='grey', width=20, height=10, command=self.colorBlack)
        self.greyColor.place(relx=.32, rely=.8,anchor=S)

        self.brownColor = Button(self.tab2, text='brown', bg='brown', width=20, height=10, command=self.colorBrown)
        self.brownColor.place(relx=.64, rely=.8,anchor=SE)

        # Adds button on tab2 to return to drawing (tab1)
        self.return_from_color = Button(self.tab2, text='Return', command=self.return_to_drawing)
        self.return_from_color.pack(side=BOTTOM)

        ## TAB 3: TOOLS - TOOLS CURRENTLY ARE NOT DIFFERENT
        # TODO: Make tools look different
        self.pen_button = Button(self.tab3, text='pen', command=self.use_pen)
        self.pen_button.pack(side=TOP, padx=1)

        self.brush_button = Button(self.tab3, text='brush', command=self.use_brush)
        self.brush_button.pack(side=TOP, padx=2)

        # Adds button on tab3 to return to drawing (tab1)
        self.return_from_tool = Button(self.tab3, text='Return', command=self.return_to_drawing)
        self.return_from_tool.pack(side=BOTTOM)

        ## Sets up GUI and checks for user input:
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

    def choose_tool(self):
        """Moves to tab3 so that tool can be chosen"""
        self.tabControl.select(self.tab3)

    def use_pen(self):
        self.activate_button(self.pen_button)

    #def switch_tab(self):
    #    self.tabControl.select(self.tab2)

    def return_to_drawing(self):
        """ Returns to tab1"""
        self.tabControl.select(self.tab1)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        """Opens tab2, which shows color options. Also turns eraser off"""
        self.eraser_on = False
        #self.color = askcolor(color=self.color)
        self.tabControl.select(self.tab2)

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


    ## SAVING:
    def snapsave(self):
        #print('n def _snapsaveCanvas(self):')
        canvas = self._canvas()  # Get Window Coordinates of Canvas
        self.grabcanvas = ImageGrab.grab(bbox=canvas).save("test_image.jpg")
        # TODO: save image name as something significant
        #print('Screencshot tkinter canvas and saved as "out_snapsave.jpg w/o displaying screenshoot."')

    def _canvas(self):
        #print('  def _canvas(self):')
        #print('self.cv.winfo_rootx() = ', self.c.winfo_rootx())
        #print('self.cv.winfo_rooty() = ', self.c.winfo_rooty())
        #print('self.cv.winfo_x() =', self.c.winfo_x())
        #print('self.cv.winfo_y() =', self.c.winfo_y())
        #print('self.cv.winfo_width() =', self.c.winfo_width())
        #print('self.cv.winfo_height() =', self.c.winfo_height())
        x=self.c.winfo_rootx()+self.c.winfo_x()
        y=self.c.winfo_rooty()+self.c.winfo_y()
        x1=x+self.c.winfo_width()
        y1=y+self.c.winfo_height()
        box=(x,y,x1,y1)
        #print('box = ', box)
        return box

    ## COLOR FUNCTIONS:
    def colorRed(self):
        self.color='red'
        self.redColor.config(relief=SUNKEN)

    def colorBlue(self):
        self.color='blue'
        self.blueColor.config(relief=SUNKEN)

    def colorYellow(self):
        self.color='yellow'
        self.yellowColor.config(relief=SUNKEN)

    def colorGreen(self):
        self.color='green'
        self.greenColor.config(relief=SUNKEN)

    def colorOrange(self):
        self.color='orange'
        self.orangeColor.config(relief=SUNKEN)

    def colorPurple(self):
        self.color='purple'
        self.purpleColor.config(relief=SUNKEN)

    def colorBlack(self):
        self.color='black'
        self.blackColor.config(relief=SUNKEN)

    def colorBrown(self):
        self.color='brown'
        self.brownColor.config(relief=SUNKEN)


if __name__ == '__main__':
    Paint()