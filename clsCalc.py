from tkinter import *
import os
import enum

#class EnumCalc(enum):
#    PLUS = 0
#    MINUS = 1
#    MULTIPLY = 2
#    DIVIDE = 3
#    SQUARE = 4
#    EQUAL = 5
#pass

def Print(self, numberOrSignal):

    if(("+" in str(numberOrSignal)) or ("-" in str(numberOrSignal)) or ("/" in str(numberOrSignal)) or ("*" in str(numberOrSignal) )):
        self.display["text"] = self.display["text"] + " " + str(numberOrSignal)
        pass #IF
    elif( ("1" in str(numberOrSignal)) or ("2" in str(numberOrSignal)) or ("3" in str(numberOrSignal)) or ("4" in str(numberOrSignal)) or ("5" in str(numberOrSignal)) or ("6" in str(numberOrSignal)) or ("7" in str(numberOrSignal)) or ("8" in str(numberOrSignal)) or ("9" in str(numberOrSignal)) or ("0" in str(numberOrSignal) )):
        self.display["text"] = self.display["text"] + str(numberOrSignal)
        pass #ELIF



def Sum(x, y):
    try:
        return x + y
    except:
        return -1
    pass #Sum

def Minus(x, y):
    try:
        return x - y
    except:
        return -1
    pass #Minus

def Division(x, y):
    try:
        return x / y
    except:
        return -1
    pass #Division

def Multiply(x, y):
    try:
        return x + y
    except:
        return -1
    pass #Multiply

def Square(x, y):
    try:
        return x ^ y
    except:
        return -1
    pass #Square

class clsCalc():

    def __init__(self, master=None):
        self.Container1 = Frame(master)
        self.Container1.pack()        

        self.display = Label(self.Container1, text="")
        self.display["bg"] = "white"
        self.display["pady"] = 5
        self.display["padx"] = 30
        self.display.grid(row=0, column=0, columnspan=3)

        self.button1 = Button(self.Container1, text=" 1 ", command=lambda: Print(self, 1)) 
        self.button1.grid(row=1, column=0)
        #self.button1.pack()

        self.button2 = Button(self.Container1, text=" 2 ", command=lambda: Print(self, 2))
        self.button2.grid(row=1, column=1)
        #self.button2.pack()

        self.button3 = Button(self.Container1, text=" 3 ", command=lambda: Print(self, 3))
        self.button3.grid(row=1, column=2)
        #self.button3.pack()

        self.button4 = Button(self.Container1, text=" 4 ", command=lambda: Print(self, 4))
        self.button4.grid(row=2, column=0)
        #self.button4.pack()

        self.button5 = Button(self.Container1, text=" 5 ", command=lambda: Print(self, 5))
        self.button5.grid(row=2, column=1)
        #self.button5.pack()

        self.button6 = Button(self.Container1, text=" 6 ", command=lambda: Print(self, 6))
        self.button6.grid(row=2, column=2)
        #self.button6.pack()

        self.button7 = Button(self.Container1, text=" 7 ", command=lambda: Print(self, 7))
        self.button7.grid(row=3, column=0)
        #self.button7.pack()

        self.button8 = Button(self.Container1, text=" 8 ", command=lambda: Print(self, 8))
        self.button8.grid(row=3, column=1)
        #self.button8.pack()

        self.button9 = Button(self.Container1, text=" 9 ", command=lambda: Print(self, 9))
        self.button9.grid(row=3, column=2)
        #self.button9.pack()

        self.button0 = Button(self.Container1, text=" 0 ", command=lambda: Print(self, 0))
        self.button0.grid(row=4, column=1)
        #self.button0.pack()

        self.buttonDiv = Button(self.Container1, text=" / ", command=lambda: Print(self, "/"))
        self.buttonDiv.grid(row=5, column=0)
        #self.buttonDiv.pack()

        self.buttonMult = Button(self.Container1, text=" * ", command=lambda: Print(self, "*"))
        self.buttonMult.grid(row=5, column=1)
        #self.buttonMult.pack()

        self.buttonPlus = Button(self.Container1, text=" + ", command=lambda: Print(self, "+"))
        self.buttonPlus.grid(row=5, column=2)
        #self.buttonPlus.pack()

        self.buttonMinus = Button(self.Container1, text=" - ", command=lambda: Print(self, "-"))
        self.buttonMinus.grid(row=5, column=3)
        #self.buttonMinus.pack()
        


        
        pass


    pass #clsScreen

def main():
    Tela = Tk(className="Calculadore Python Jussa!")
    Tela.geometry("200x500")
    clsCalc(Tela)
    Tela.mainloop()

if __name__ == "__main__":
    main()
else:
    quit()