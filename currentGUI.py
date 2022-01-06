from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

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
        self.tabControl.add(self.tab1, text='Drawing')
        self.tabControl.add(self.tab2, text='Colors')
        self.tabControl.add(self.tab3, text='Tool')
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
        self.tool_button = Button(self.tab1, text='Tool', command=self.choose_tool)
        self.tool_button.grid(row=0, column=0)

        # Eraser Button
        eraser_button_png = PhotoImage(file='eraser_button.png')
        self.eraser_button = Button(self.tab1, image = eraser_button_png, command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        # Size Selection
        self.choose_size_button = Scale(self.tab1, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=3)

        # Save Button- CURRENTLY DOES NOTHING
        # TODO: make save button actually save file
        self.save_button = Button(self.tab1, text='Save')
        self.save_button.grid(row=0, column=4)

        ## TAB 2: COLORS
        # TODO: Add more colors
        self.redColor = Button(self.tab2, text='red', command=self.colorRed)
        self.redColor.grid(row=2, column=0)

        # Adds button on tab2 to return to drawing (tab1)
        self.return_from_color = Button(self.tab2, text='Return', command=self.return_to_drawing)
        self.return_from_color.grid(row=0, column=2)

        ## TAB 3: TOOLS - TOOLS CURRENTLY ARE NOT DIFFERENT
        # TODO: Make tools look different
        self.pen_button = Button(self.tab3, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.tab3, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        # Adds button on tab3 to return to drawing (tab1)
        self.return_from_tool = Button(self.tab3, text='Return', command=self.return_to_drawing)
        self.return_from_tool.grid(row=0, column=2)

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

    def colorRed(self):
        self.color='red'


if __name__ == '__main__':
    Paint()

