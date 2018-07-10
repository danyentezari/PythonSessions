from tkinter import Tk, Label, Button, Entry
from pprint import pprint

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        
        self.btnLabels = ('AC', '+/-','%','C','7','8','9','x','4','5','6','-','1','2','3','+','0','0','.','=')

        self.window.columnconfigure((0,1,2,3), weight=1)
        self.window.rowconfigure((0,1), weight=1)


        self.label = Label(window,
            text="The label",
            highlightthickness=1,
            highlightcolor="black",
            highlightbackground="black",
            anchor="ne"
        )

        # self.label.pack
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        newRow = 1
        newCol = 0
        index = 0

        for lbl in self.btnLabels:
            self.button = Button(window, text=lbl, command=self.btnInput)
            self.button.grid(row=newRow,column=newCol,sticky="nsew")

            index += 1
            newCol += 1
            if index % 4 == 0:
                newRow += 1
                newCol = 0

    def btnInput(self):
        self.label.configure(text="A")
        pprint(self.label)


# Create a new TK instance (object) called appWindow
appWindow = Tk()
appWindow.geometry("300x300")
myNewCalculator = Calculator(appWindow) 
appWindow.mainloop()