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
        self.c.grid(row=1, columnspan=5)

        # Button on tab1 that moves to tab2 so that COLOR can be selected
        color_button_png = PhotoImage(file='color_button.png')
        self.color_button = Button(self.tab1, image = color_button_png, command=self.choose_color)
        self.color_button.grid(row=0, column=1)

        # Button on tab1 that moves to tab 3 so that TOOL can be selected
        tool_button_png = PhotoImage(file='art_tools_button.png')
        self.tool_button = Button(self.tab1, image = tool_button_png, command=self.choose_tool)
        self.tool_button.grid(row=0, column=0)

        # Eraser Button
        eraser_button_png = PhotoImage(file='eraser_button.png')
        self.eraser_button = Button(self.tab1, image = eraser_button_png, command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        # Size Selection
        size_button_png = PhotoImage(file='size_button.png')
        self.choose_size_button = Button(self.tab1, image = size_button_png, command=self.choose_size)
        self.choose_size_button.grid(row=0, column=3)

        # Save Button- CURRENTLY DOES NOTHING
        # TODO: fix save problem
        save_button_png = PhotoImage(file='save_button.png')
        self.save_button = Button(self.tab1, image = save_button_png, command=self.snapsave)
        self.save_button.grid(row=0, column=4)

        ## TAB 2: COLORS
        # TODO: Add more colors
        self.redColor = Button(self.tab2, text='red', bg='red', width=20, height=10, command=self.colorRed)
        self.redColor.grid(row=1, column=1)

        self.blueColor = Button(self.tab2, text='blue', bg='blue', width=20, height=10, command=self.colorBlue)
        self.blueColor.grid(row=2, column=0)

        self.yellowColor = Button(self.tab2, text='yellow', bg='yellow', width=20, height=10, command=self.colorYellow)
        self.yellowColor.grid(row=2, column=2)

        self.greenColor = Button(self.tab2, text='green', bg='green', width=20, height=10, command=self.colorGreen)
        self.greenColor.grid(row=2, column=1)

        self.orangeColor = Button(self.tab2, text='orange', bg='orange', width=20, height=10, command=self.colorOrange)
        self.orangeColor.grid(row=1, column=2)

        self.purpleColor = Button(self.tab2, text='purple', bg='purple', width=20, height=10, command=self.colorPurple)
        self.purpleColor.grid(row=1, column=0)

        self.blackColor = Button(self.tab2, text='black', bg='black', fg='white', width=20, height=10, command=self.colorBlack)
        self.blackColor.grid(row=0, column=0)

        self.greyColor = Button(self.tab2, text='grey', bg='grey', width=20, height=10, command=self.colorBlack)
        self.greyColor.grid(row=0, column=1)

        self.brownColor = Button(self.tab2, text='brown', bg='brown', width=20, height=10, command=self.colorBrown)
        self.brownColor.grid(row=0, column=2)

        # Adds button on tab2 to return to drawing (tab1)
        return_button_png = PhotoImage(file='return_button.png')
        self.return_from_color = Button(self.tab2, image=return_button_png, command=self.return_to_drawing)
        self.return_from_color.grid(row=3, column=1)

        ## TAB 3: TOOLS - TOOLS CURRENTLY ARE NOT DIFFERENT
        # TODO: Make tools look different
        self.pen_button = Button(self.tab3, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.tab3, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        # Adds button on tab3 to return to drawing (tab1)
        self.return_from_tool = Button(self.tab3, text='Return', command=self.return_to_drawing)
        self.return_from_tool.grid(row=0, column=2)

        ##TAB 4: SIZE
        # TODO: Add more sizes
        size1_png = PhotoImage(file='size_1.png')
        self.first_size = Button(self.tab4, image = size1_png,command=self.size1)
        self.first_size.grid(row=0, column=1)

        size2_png = PhotoImage(file='size_2.png')
        self.second_size = Button(self.tab4, image = size2_png,command=self.size2)
        self.second_size.grid(row=0, column=2)

        size3_png = PhotoImage(file='size_3.png')
        self.third_size = Button(self.tab4, image = size3_png,command=self.size3)
        self.third_size.grid(row=0, column=3)

        size4_png = PhotoImage(file='size_4.png')
        self.fourth_size = Button(self.tab4, image = size4_png,command=self.size4)
        self.fourth_size.grid(row=1, column=1)

        size5_png = PhotoImage(file='size_5.png')
        self.fifth_size = Button(self.tab4, image = size5_png,command=self.size5)
        self.fifth_size.grid(row=1, column=2)


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
        #print('n def _snapsaveCanvas(self):')
        canvas = self._canvas()  # Get Window Coordinates of Canvas
        self.grabcanvas = ImageGrab.grab(bbox=canvas).save("test_image.jpg")
        # TODO: save image name as something significant
        #print('Screencshot tkinter canvas and saved as "out_snapsave.jpg w/o displaying screenshoot."')

    def _canvas(self):
        """Returns box which encompases canvas"""
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

