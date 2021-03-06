from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import ImageGrab
import time

sys.path.append("Kind-of-Happy-Campers-master")
from CircleShape import Circle
import threading

""" TODO:
        Create different tools - Veronica
        Switching between drawing and selection modes (i.e. when pressing space bar) - All
        """


class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        # Shape
        self.currentShape = None

        # Start timer:
        t = threading.Timer(2700.0, self.warning)  # Displays warning after 45 minutes
        t.start()
        # Start GUI:
        self.root = Tk()
        self.root.wm_title('EyePaint')
        self.tabControl = ttk.Notebook(self.root)

        ## POPUP for Naming + Template Choice
        self.popup = Toplevel()
        self.popup.wm_title("Name")
        self.popup.attributes("-topmost", True)  # New window will be at the foreground
        # Templates:
        self.label3 = Label(self.popup, text="What would you like to make?")
        self.label3.grid(row=0, column=0)
        self.whole_page = Button(self.popup, text='Large Painting', command=self.wholePage, relief=SUNKEN)
        self.whole_page.grid(row=1, column=0)
        self.currentChoice = self.whole_page
        self.bookmark_option = Button(self.popup, text='Bookmark', command=self.makeBookmark)
        self.bookmark_option.grid(row=1, column=1)
        self.postcard_option = Button(self.popup, text='Postcard', command=self.makePostcard)
        self.postcard_option.grid(row=1, column=3)
        # Naming:
        self.label1 = Label(self.popup, text='Name Your File')
        self.label2 = Label(self.popup, text='Filename:')
        self.label1.grid(row=3, column=0)
        self.label2.grid(row=4, column=0)
        self.filename = StringVar()  # Creates variable for the file name to be stored
        self.filename = 'filename'
        self.ask_filename = Entry(self.popup, textvariable=self.filename)  # Entry box for name to be typed
        self.ask_filename.insert(0, "filename")  # Default for the name of the file is "filename.jpg"
        self.ask_filename.grid(row=4, column=1)
        self.get_filename = Button(self.popup, text='Continue', command=self.get_name)  # Press Button to continue
        self.get_filename.grid(row=5, column=0)

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
        self.c.pack(side=LEFT, fill=BOTH, expand=1)

        # Button on tab1 that moves to tab2 so that COLOR can be selected
        color_button_png = PhotoImage(file='color_button.png')
        self.color_button = Button(self.tab1, image=color_button_png, height=80, width=80, command=self.choose_color)
        self.color_button.pack(side=TOP, pady=10)

        # Button on tab1 that moves to tab 3 so that TOOL can be selected
        tool_button_png = PhotoImage(file='art_tools_button.png')
        self.tool_button = Button(self.tab1, image=tool_button_png, height=80, width=80, command=self.choose_tool)
        self.tool_button.pack(side=TOP, pady=10)

        # Eraser Button
        eraser_button_png = PhotoImage(file='eraser_button.png')
        self.eraser_button = Button(self.tab1, image=eraser_button_png, height=80, width=80, command=self.use_eraser)
        self.eraser_button.pack(side=TOP, pady=10)

        # Size Selection
        size_button_png = PhotoImage(file='size_button.PNG')
        self.choose_size_button = Button(self.tab1, image=size_button_png, height=80, width=80,
                                         command=self.choose_size)
        self.choose_size_button.pack(side=TOP, pady=10)

        # Save Button
        self.filename = StringVar()
        self.filename = 'filename'
        save_button_png = PhotoImage(file='save_button.png')
        self.save_button = Button(self.tab1, image=save_button_png, height=80, width=80, command=self.snapsave)
        self.save_button.pack(side=TOP, pady=10)

        # Undo Button
        undo_button_png = PhotoImage(file='undo_button.png')
        self.undo_button = Button(self.tab1, image=undo_button_png, height=80, width=80, command=self.undo)
        self.undo_button.pack(side=TOP, pady=10)

        ## TAB 2: COLORS
        self.redColor = Button(self.tab2, text='red', bg='red', width=30, height=10, command=self.colorRed)
        self.redColor.place(relx=0, rely=0, anchor=NW)

        self.blueColor = Button(self.tab2, text='blue', bg='blue', width=30, height=10, command=self.colorBlue)
        self.blueColor.place(relx=.5, rely=0, anchor=N)

        self.yellowColor = Button(self.tab2, text='yellow', bg='yellow', width=30, height=10, command=self.colorYellow)
        self.yellowColor.place(relx=1.0, rely=0, anchor=NE)

        self.greenColor = Button(self.tab2, text='green', bg='green', width=30, height=10, command=self.colorGreen)
        self.greenColor.place(relx=0, rely=.4, anchor=W)

        self.orangeColor = Button(self.tab2, text='orange', bg='orange', width=30, height=10, command=self.colorOrange)
        self.orangeColor.place(relx=.50, rely=.4, anchor=CENTER)

        self.purpleColor = Button(self.tab2, text='purple', bg='purple', width=30, height=10, command=self.colorPurple)
        self.purpleColor.place(relx=1.0, rely=.4, anchor=E)

        self.blackColor = Button(self.tab2, text='black', bg='black', fg='white', width=30, height=10,
                                 command=self.colorBlack, relief=SUNKEN)
        self.blackColor.place(relx=0, rely=.8, anchor=SW)
        self.currentColor = self.blackColor

        self.greyColor = Button(self.tab2, text='grey', bg='grey', width=30, height=10, command=self.colorGrey)
        self.greyColor.place(relx=.5, rely=.8, anchor=S)

        self.brownColor = Button(self.tab2, text='brown', bg='brown', width=30, height=10, command=self.colorBrown)
        self.brownColor.place(relx=1.0, rely=.8, anchor=SE)

        # Adds button on tab2 to return to drawing (tab1)
        return_button_png = PhotoImage(file='return_button.png')
        self.return_from_color = Button(self.tab2, image=return_button_png, height=125, width=125,
                                        command=self.return_to_drawing)
        self.return_from_color.pack(side=BOTTOM)

        ## TAB 3: TOOLS - TOOLS CURRENTLY ARE NOT DIFFERENT
        # TODO: Make tools look different
        self.pen_button = Button(self.tab3, text='pen', command=self.use_pen)
        self.pen_button.pack(side=TOP, padx=1)

        self.circle_button = Button(self.tab3, text='circle', command=self.use_circle)
        self.circle_button.pack(side=TOP, padx=2)

        self.triangle_button = Button(self.tab3, text='triangle', command=self.use_triangle)
        self.triangle_button.pack(side=TOP, padx=3)

        self.rectangle_button = Button(self.tab3, text='rectangle', command=self.use_rectangle)
        self.rectangle_button.pack(side=TOP, padx=4)

        # Adds button on tab3 to return to drawing (tab1)
        self.return_from_tool = Button(self.tab3, image=return_button_png, height=125, width=125,
                                       command=self.return_to_drawing)
        self.return_from_tool.pack(side=BOTTOM)

        self.tag = None

        ##TAB 4: SIZE
        # TODO: Add more sizes
        size1_png = PhotoImage(file='size_1.PNG')
        self.first_size = Button(self.tab4, image=size1_png, height=200, width=200, command=self.size1)
        self.first_size.place(relx=0, rely=0, anchor=NW)

        size2_png = PhotoImage(file='size_2.PNG')
        self.second_size = Button(self.tab4, image=size2_png, height=200, width=200, command=self.size2)
        self.second_size.place(relx=.5, rely=0, anchor=N)

        size3_png = PhotoImage(file='size_3.PNG')
        self.third_size = Button(self.tab4, image=size3_png, height=200, width=200, command=self.size3)
        self.third_size.place(relx=1.0, rely=0, anchor=NE)

        size4_png = PhotoImage(file='size_4.PNG')
        self.fourth_size = Button(self.tab4, image=size4_png, height=200, width=200, command=self.size4)
        self.fourth_size.place(relx=0, rely=.5, anchor=W)

        size5_png = PhotoImage(file='size_5.PNG')
        self.fifth_size = Button(self.tab4, image=size5_png, height=200, width=200, command=self.size5)
        self.fifth_size.place(relx=.5, rely=.5, anchor=CENTER)

        size6_png = PhotoImage(file='size_6.PNG')
        self.sixth_size = Button(self.tab4, image=size6_png, height=200, width=200, command=self.size6)
        self.sixth_size.place(relx=1.0, rely=.5, anchor=E)

        # Adds button on tab4 to return to drawing (tab1)
        self.return_from_size = Button(self.tab4, image=return_button_png, height=125, width=125,
                                       command=self.return_to_drawing)
        self.return_from_size.pack(side=BOTTOM)

        ## Sets up GUI and checks for user input:
        self.linelist = [
            self.c.create_line(0, 0, 0, 0, width=0, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=36)]
        self.setup()
        self.root.bind("<Key>", self.keypress)
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 2
        # self.line_width = self.choose_size_button
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.c.bind('<Motion>', self.callbackShape)
        self.c.bind('<ButtonPress-1>', self.resetShape)

    def choose_tool(self):
        """Moves to tab3 so that tool can be chosen"""
        self.tabControl.select(self.tab3)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def return_to_drawing(self):
        """ Returns to tab1"""
        self.tabControl.select(self.tab1)

    def use_circle(self):
        self.activate_button(self.circle_button)
        self.currentShape = self.c.create_oval(0, 0, 10 * (self.line_width), 10 * (self.line_width), fill=self.color,
                                               tag="oval")
        self.tag = "oval"

    def use_triangle(self):
        self.activate_button(self.triangle_button)
        # self.currentShape = self.c.create_oval(0, 0, 10*(self.line_width), 10*(self.line_width), fill = self.color, tag = "oval")
        self.currentShape = self.c.create_polygon(
            [0, 0, 10 * self.line_width, 0, (10 * self.line_width) / 2 - 10 * self.line_width, 0]
            , fill=self.color, tags="triangle")
        self.tag = "triangle"
        print(self.c.type(self.currentShape))

    def use_rectangle(self):
        self.activate_button(self.rectangle_button)
        self.currentShape = self.c.create_rectangle(0, 0, 10 * (self.line_width), 10 * (self.line_width),
                                                    fill=self.color, tag="rectangle")
        self.tag = "rectangle"

    def choose_color(self):
        """Opens tab2, which shows color options. Also turns eraser off"""
        self.eraser_on = False
        # self.color = askcolor(color=self.color)
        self.tabControl.select(self.tab2)

    def use_eraser(self):
        "Opens tab4, which shows size options."
        self.activate_button(self.eraser_button, eraser_mode=True)

    def choose_size(self):
        self.tabControl.select(self.tab4)

    def undo(self):
        for k in range(len(self.linelist)):
            self.c.delete(self.linelist[k])

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        # self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            newline = self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                         width=self.line_width, fill=paint_color,
                                         capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.linelist.append(newline)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    ## SAVING:
    def snapsave(self):
        # print('n def _snapsaveCanvas(self):')
        canvas = self._canvas()  # Get Window Coordinates of Canvas
        savename = self.filename + '.jpg'
        self.grabcanvas = ImageGrab.grab(bbox=canvas).save(savename)
        # TODO: save image name as something significant
        # print('Screencshot tkinter canvas and saved as "out_snapsave.jpg w/o displaying screenshoot."')

    def _canvas(self):
        """Returns box which encompases canvas"""
        x = self.c.winfo_rootx() + self.c.winfo_x()
        y = self.c.winfo_rooty() + self.c.winfo_y()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        box = (x, y, x1, y1)
        # print('box = ', box)
        return box

    def get_name(self):
        """ Takes the text in the ask_filename entry widget in the starting popup window and names it to the filename
            variable. Destroys the popup window so that the user can now draw."""
        self.filename = self.ask_filename.get()
        # print(self.filename)
        savename = self.filename + ".jpg"
        # print(savename)
        self.popup.destroy()
        self.root.attributes("-topmost", True)

    ## COLOR FUNCTIONS:
    def colorRed(self):
        self.color = 'red'
        self.currentColor.config(relief=RAISED)
        self.redColor.config(relief=SUNKEN)
        self.currentColor = self.redColor

    def colorBlue(self):
        self.color = 'blue'
        self.currentColor.config(relief=RAISED)
        self.blueColor.config(relief=SUNKEN)
        self.currentColor = self.blueColor

    def colorYellow(self):
        self.color = 'yellow'
        self.currentColor.config(relief=RAISED)
        self.yellowColor.config(relief=SUNKEN)
        self.currentColor = self.yellowColor

    def colorGreen(self):
        self.color = 'green'
        self.currentColor.config(relief=RAISED)
        self.greenColor.config(relief=SUNKEN)
        self.currentColor = self.greenColor

    def colorOrange(self):
        self.color = 'orange'
        self.currentColor.config(relief=RAISED)
        self.orangeColor.config(relief=SUNKEN)
        self.currentColor = self.orangeColor

    def colorPurple(self):
        self.color = 'purple'
        self.currentColor.config(relief=RAISED)
        self.purpleColor.config(relief=SUNKEN)
        self.currentColor = self.purpleColor

    def colorBlack(self):
        self.color = 'black'
        self.currentColor.config(relief=RAISED)
        self.blackColor.config(relief=SUNKEN)
        self.currentColor = self.blackColor

    def colorBrown(self):
        self.color = 'brown'
        self.currentColor.config(relief=RAISED)
        self.brownColor.config(relief=SUNKEN)
        self.currentColor = self.brownColor

    def colorGrey(self):
        self.color = 'grey'
        self.currentColor.config(relief=RAISED)
        self.greyColor.config(relief=SUNKEN)
        self.currentColor = self.greyColor

    ## SIZE FUNCTIONS
    def size1(self):
        self.line_width = 3
        self.first_size.config(relief=SUNKEN)

    def size2(self):
        self.line_width = 6
        self.second_size.config(relief=SUNKEN)

    def size3(self):
        self.line_width = 9
        self.third_size.config(relief=SUNKEN)

    def size4(self):
        self.line_width = 12
        self.fourth_size.config(relief=SUNKEN)

    def size5(self):
        self.line_width = 15
        self.fifth_size.config(relief=SUNKEN)

    def size6(self):
        self.line_width = 21
        self.sixth_size.config(relief=SUNKEN)

    ## TEMPLATE FUNCTIONS:
    def makePostcard(self):
        """Creates a postcard template"""
        self.c.delete('all')
        self.currentChoice.config(relief=RAISED)
        self.postcard_option.config(relief=SUNKEN)
        self.currentChoice = self.postcard_option
        self.c.create_rectangle(50, 50, 550, 350)

    def wholePage(self):
        """Clears the page so that the user can draw on the whole page"""
        self.c.delete('all')
        self.currentChoice.config(relief=RAISED)
        self.whole_page.config(relief=SUNKEN)
        self.currentChoice = self.whole_page

    def makeBookmark(self):
        """Draws a bookmark template"""
        self.c.delete('all')
        self.currentChoice.config(relief=RAISED)
        self.bookmark_option.config(relief=SUNKEN)
        self.currentChoice = self.bookmark_option
        self.c.create_rectangle(250, 50, 450, 550)
        self.c.create_oval(330, 60, 370, 100)

    ## WARNING FUNCTIONS:
    def warning(self):
        """Display warning when the user has been working for 45 minutes to warn against overuse"""
        self.display_warning = Toplevel()
        self.display_warning.wm_title("Time for a break?")
        self.display_warning.attributes("-topmost", True)
        self.warningLabel = Label(self.display_warning, text="You have been working for 45 minutes")
        self.warningLabel.grid(row=0, column=0)
        self.continue_from_warning = Button(self.display_warning, text="Conitnue", command=self.closeWarning)
        self.continue_from_warning.grid(row=1, column=0)

    def closeWarning(self):
        """Close the warning box, move main canvas to foreground"""
        self.display_warning.destroy()
        self.root.attributes("-topmost", True)

    ##Shapes
    def keypress(self, event):
        """If you go down or right increase
           If you go left of up decrease"""
        x = 0
        y = 0
        if event.char == "a":
            x = -10  # left
        elif event.char == "d":
            x = 10  # right
        elif event.char == "w":
            y = -10  # up
        elif event.char == "s":
            y = 10  # down
        self.c.move(self.currentShape, x, y)

    def draw(self, x, y):
        if (self.currentShape != None):
            # print(self.c.type(self.currentShape))
            if (self.tag == "oval"):
                self.c.coords(self.currentShape, x, y, x + 10 * self.line_width, y + 10 * self.line_width)
            if (self.tag == "triangle"):
                self.c.coords(self.currentShape, x, y, x + 10 * self.line_width, y, x + (10 * self.line_width) / 2,
                              y - 10 * self.line_width)
            if (self.tag == "rectangle"):
                self.c.coords(self.currentShape, x, y, x + 10 * self.line_width, y + 10 * self.line_width)

    def callbackShape(self, event):
        if (self.currentShape != None):
            self.draw(event.x, event.y)

    def resetShape(self, event):
        self.currentShape = None
        print('reset')


if __name__ == '__main__':
    Paint()