from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import ImageGrab

""" TODO:
        Make all buttons bigger (especially in drawing tab) - Carla
        Create different tools - Veronica
        Placement of buttons (especially in colors, thickness tabs) - Carla
        Switching between drawing and selection modes (i.e. when pressing space bar) - All
        Different Canvas sizes - Keely
        """

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.wm_title('EyePaint')
        self.tabControl = ttk.Notebook(self.root)

        # Create Popup for naming:
        self.popup = Toplevel()
        self.popup.wm_title("Name")
        self.popup.attributes("-topmost", True) # New window will be at the foreground
        self.label1 = Label(self.popup, text='Name Your File')
        self.label2 = Label(self.popup, text='Filename:')
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.filename = StringVar() # Creates variable for the file name to be stored
        self.filename = 'filename'
        self.ask_filename = Entry(self.popup, textvariable=self.filename) # Entry box for name to be typed
        self.ask_filename.insert(0, "filename") # Default for the name of the file is "filename.jpg"
        self.ask_filename.grid(row=1, column=1)
        self.get_filename = Button(self.popup, text='Continue', command=self.get_name) # Press Button to continue
        self.get_filename.grid(row=2, column=0)

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

        ## TAB 1: DRAWING
        # The canvas for drawing:
        self.c = Canvas(self.tab1, bg='white', width=600, height=600)
        self.c.pack(side = LEFT, fill=BOTH, expand=1)

        # Button on tab1 that moves to tab2 so that COLOR can be selected
        color_button_png = PhotoImage(file='color_button.png')
        self.color_button = Button(self.tab1, image = color_button_png, command=self.choose_color)
        self.color_button.pack(side=TOP, pady=50)

        # Button on tab1 that moves to tab 3 so that TOOL can be selected
        tool_button_png = PhotoImage(file='art_tools_button.png')
        self.tool_button = Button(self.tab1, image = tool_button_png, command=self.choose_tool)
        self.tool_button.pack(side=TOP, pady=50)

        # Eraser Button
        eraser_button_png = PhotoImage(file='eraser_button.png')
        self.eraser_button = Button(self.tab1, image = eraser_button_png, command=self.use_eraser)
        self.eraser_button.pack(side=TOP, pady=50)

        # Size Selection
        size_button_png = PhotoImage(file='size_button.png')
        self.choose_size_button = Button(self.tab1, image = size_button_png, command=self.choose_size)
        self.choose_size_button.pack(side=TOP, pady=50)

        # Save Button
        save_button_png = PhotoImage(file='save_button.png')
        self.save_button = Button(self.tab1, image = save_button_png, command=self.snapsave)
        self.save_button.pack(side=TOP, pady=50)

        ## TAB 2: COLORS
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

        self.greyColor = Button(self.tab2, text='grey', bg='grey', width=20, height=10, command=self.colorGrey)
        self.greyColor.place(relx=.32, rely=.8,anchor=S)

        self.brownColor = Button(self.tab2, text='brown', bg='brown', width=20, height=10, command=self.colorBrown)
        self.brownColor.place(relx=.64, rely=.8,anchor=SE)

        # Adds button on tab2 to return to drawing (tab1)
        return_button_png = PhotoImage(file='return_button.png')
        self.return_from_color = Button(self.tab2, image=return_button_png, command=self.return_to_drawing)
        self.return_from_color.pack(side=BOTTOM)

        ## TAB 3: TOOLS - TOOLS CURRENTLY ARE NOT DIFFERENT
        # TODO: Make tools look different
        self.pen_button = Button(self.tab3, text='pen', command=self.use_pen)
        self.pen_button.pack(side=TOP, padx=1)

        self.brush_button = Button(self.tab3, text='brush', command=self.use_brush)
        self.brush_button.pack(side=TOP, padx=2)

        # Adds button on tab3 to return to drawing (tab1)
        self.return_from_tool = Button(self.tab3, image=return_button_png, command=self.return_to_drawing)
        self.return_from_tool.pack(side=BOTTOM)

        ##TAB 4: SIZE
        size1_png = PhotoImage(file='size_1.png')
        self.first_size = Button(self.tab4, image = size1_png,command=self.size1)
        self.first_size.place(relx=0, rely=0,anchor=NW)

        size2_png = PhotoImage(file='size_2.png')
        self.second_size = Button(self.tab4, image = size2_png,command=self.size2)
        self.second_size.place(relx=.32, rely=0,anchor=N)

        size3_png = PhotoImage(file='size_3.png')
        self.third_size = Button(self.tab4, image = size3_png,command=self.size3)
        self.third_size.place(relx=.64, rely=0,anchor=NE)

        size4_png = PhotoImage(file='size_4.png')
        self.fourth_size = Button(self.tab4, image = size4_png,command=self.size4)
        self.fourth_size.place(relx=0, rely=.4,anchor=W)

        size5_png = PhotoImage(file='size_5.png')
        self.fifth_size = Button(self.tab4, image = size5_png,command=self.size5)
        self.fifth_size.place(relx=.32, rely=.4,anchor=CENTER)

        # Adds button on tab4 to return to drawing (tab1)
        self.return_from_size = Button(self.tab4, image=return_button_png,command=self.return_to_drawing)
        self.return_from_size.pack(side=BOTTOM)

        ## Sets up GUI and checks for user input:
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 2
        #self.line_width = self.choose_size_button
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
        "Opens tab4, which shows size options."
        self.activate_button(self.eraser_button, eraser_mode=True)

    def choose_size(self):
        self.tabControl.select(self.tab4)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        #self.line_width = self.choose_size_button.get()
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
        canvas = self._canvas()  # Get Window Coordinates of Canvas
        savename = self.filename + '.jpg'
        self.grabcanvas = ImageGrab.grab(bbox=canvas).save(savename)

    def _canvas(self):
        """Returns box which encompases canvas"""
        x=self.c.winfo_rootx()+self.c.winfo_x()
        y=self.c.winfo_rooty()+self.c.winfo_y()
        x1=x+self.c.winfo_width()
        y1=y+self.c.winfo_height()
        box=(x,y,x1,y1)
        return box

    def get_name(self):
        """ Takes the text in the ask_filename entry widget in the starting popup window and names it to the filename
            variable. Destroys the popup window so that the user can now draw."""
        self.filename = self.ask_filename.get()
        print(self.filename)
        savename = self.filename + ".jpg"
        print(savename)
        self.popup.destroy()
        self.root.attributes("-topmost", True)

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

    def colorGrey(self):
        self.color='grey'
        self.greyColor.config(relifer=SUNKEN)

    ## SIZE FUNCTIONS
    def size1(self):
        self.line_width = 2
        self.first_size.config(relief=SUNKEN)

    def size2(self):
        self.line_width = 4
        self.second_size.config(relief=SUNKEN)

    def size3(self):
        self.line_width = 6
        self.third_size.config(relief=SUNKEN)

    def size4(self):
        self.line_width = 8
        self.fourth_size.config(relief=SUNKEN)

    def size5(self):
        self.line_width = 10
        self.fifth_size.config(relief=SUNKEN)


if __name__ == '__main__':
    Paint()

