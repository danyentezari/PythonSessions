from tkinter import Tk, Label, Button, Entry
from pprint import pprint
import re

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.total = 0
        self.arithmeticMode = False
        
        self.btnLabels = ('AC', '+/-','%','C','7','8','9','x','4','5','6','-','1','2','3','+','0','.','=')

        self.window.columnconfigure((0,1,2,3), weight=1)
        self.window.rowconfigure((0,1,2,3,4,5), weight=1)


        self.label = Label(window,
            text="0",
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

        self.window.bind('<Key>', self.keyInput)

        for lbl in self.btnLabels:
            self.button = Button(window, text=lbl)
            self.button.bind('<Button-1>', self.btnInput)
            if(lbl == "0"):
                self.button.grid(row=newRow,column=newCol, columnspan=2, sticky="nsew")
                newCol+=1
            else:
                self.button.grid(row=newRow,column=newCol,sticky="nsew")

            index += 1
            newCol += 1
            if index % 4 == 0:
                newRow += 1
                newCol = 0

    def keyInput(self, event=None):
        if(re.match('[0-9]',event.keysym)):
            self.label.configure(text=event.keysym)
        
    def btnInput(self, event):
        lcd = self.label
        
        # Clear the screen when the calculator first starts
        if(lcd["text"] == "0"):
            lcd["text"] = ""

        # If the plus button is pressed
        if(event.widget["text"] == "+"):
            self.arithmeticMode = True
            self.total = self.total + int(lcd["text"])
            lcd.configure(text= str(self.total))

        # If any other key is pressed    
        else:
            if(self.arithmeticMode == False):
                lcd.configure(text= lcd["text"] + event.widget["text"])
            else:
                lcd.configure(text= event.widget["text"])
                self.arithmeticMode = False

        pprint(self.total)



# Create a new TK instance (object) called appWindow
appWindow = Tk()
appWindow.geometry("300x300")
myNewCalculator = Calculator(appWindow) 
appWindow.mainloop()