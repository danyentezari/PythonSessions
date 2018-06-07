# Import the tkinter module and include Tk, Label, and Button components.
# Note that Tk creates the actual window.
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, window):
        self.window = window
        window.title("A simple GUI")

        # Create a Label component (object)
        self.label = Label(window, text="This is our first GUI!")
        # Attach the component to the window
        self.label.pack()

        # Create a Button component (object)
        self.someButton = Button(window, text="Say Hello", command=self.sayHello)
        # Attach the component to the window
        self.someButton.pack()

        # Create a Button component (object)
        self.closeButton = Button(window, text="Close Window", command=window.quit)
        # Cttach the component to the window
        self.closeButton.pack()

    def sayHello(self):
        # Check the console for output
        print("Greetings!") 

# Create a new TK instance (object) called appWindow
appWindow = Tk()

# Create a new instance (object) of the class in this
# and pass appWindow as an argument. Note this is the window
# variable in the class.
myGUI = MyFirstGUI(appWindow)

# The mainloop() method belongs to the Tk() object.
# It will launch the window.
appWindow.mainloop()
