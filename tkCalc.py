from tkinter import *
from tkinter import font

# Window that holds all of your widgets
window = Tk()
window.configure(background='black')

# Defines the title of our window
window.title("Calculator")

# A string that holds the values for calculation
topTxt = ""

""" Add a number to the string

    Parameters:
        value (string): The value to be added to the string
"""
def addNumber(value):
    global topTxt
    topTxt = str(topTxt)
    topTxt += value
    top.configure(text = topTxt)

# Calculate the logical operations in the string
def calculate():
    global topTxt
    topTxt = eval(topTxt)
    top.configure(text = topTxt)

# Clears the string for the calculation to reset
def clearText():
    global topTxt
    topTxt = ""
    top.configure(text = topTxt)

btnFont = font.Font(size=20, weight='bold', family='Helvetica')
# The label to hold the visuals for the calculation
top = Label(window, text=topTxt, background='black', foreground='white', font=btnFont)

# Buttons for numbers 7-9
btn7 = Button(window, bg='orange', font=btnFont, text="7", command=lambda: addNumber(btn7['text']))
btn8 = Button(window, bg='orange', font=btnFont, text="8", command=lambda: addNumber(btn8['text']))
btn9 = Button(window, bg='orange', font=btnFont, text="9", command=lambda: addNumber(btn9['text']))

# Buttons for numbers 4-6
btn4 = Button(window, bg='orange', font=btnFont, text="4", command=lambda: addNumber(btn4['text']))
btn5 = Button(window, bg='orange', font=btnFont, text="5", command=lambda: addNumber(btn5['text']))
btn6 = Button(window, bg='orange', font=btnFont, text="6", command=lambda: addNumber(btn6['text']))

# Buttons for numbers 1-3
btn1 = Button(window, bg='orange', font=btnFont, text="1", command=lambda: addNumber(btn1['text']))
btn2 = Button(window, bg='orange', font=btnFont, text="2", command=lambda: addNumber(btn2['text']))
btn3 = Button(window, bg='orange', font=btnFont, text="3", command=lambda: addNumber(btn3['text']))

# Button for number 0
btn0 = Button(window, bg='orange', font=btnFont, text="0", command=lambda: addNumber(btn0['text']))

# Button for decimal point
btnDec = Button(window, bg='orange', font=btnFont, text=".", command=lambda: addNumber(btnDec['text']))

# Buttons for plus and equal signs
btnPlus = Button(window, bg='orange', font=btnFont, text="+", command=lambda: addNumber(btnPlus['text']))
btnEqual = Button(window, bg='orange', font=btnFont, text="=", command=calculate)

# Buttons for division, multiplication, and subtraction signs
btnDiv = Button(window, bg='orange', font=btnFont, text="/", command=lambda: addNumber(btnDiv['text']))
btnMult = Button(window, bg='orange', font=btnFont, text="*", command=lambda: addNumber(btnMult['text']))
btnMinus = Button(window, bg='orange', font=btnFont, text="-", command=lambda: addNumber(btnMinus['text']))

# Button to clear the topTxt
btnClear = Button(window, bg='orange', font=btnFont, text="Clear", command=clearText)


# Holds the information on how to allocate space in our grid

top.grid(column=0, row=0, columnspan=10, sticky=W)

btn7.grid(column=0, row=1, sticky=W+E)
btn8.grid(column=1, row=1, sticky=W+E)
btn9.grid(column=2, row=1, sticky=W+E)

btn4.grid(column=0, row=2, sticky=W+E)
btn5.grid(column=1, row=2, sticky=W+E)
btn6.grid(column=2, row=2, sticky=W+E)

btn1.grid(column=0, row=3, sticky=W+E)
btn2.grid(column=1, row=3, sticky=W+E)
btn3.grid(column=2, row=3, sticky=W+E)

btn0.grid(column=0, row=4, sticky=W+E, columnspan=2)

btnDec.grid(column=2, row=4, sticky=W+E)

btnPlus.grid(column=3, row=1, sticky=W+E+N+S, rowspan=2)
btnEqual.grid(column=3, row=3, sticky=W+E+N+S, rowspan=2)

btnDiv.grid(column=0, row=5, sticky=W+E)
btnMult.grid(column=1, row=5, sticky=W+E)
btnMinus.grid(column=2, row=5, sticky=W+E, columnspan=2)

btnClear.grid(column=0, row=7, sticky=W+E, columnspan = 5)

# Sets the window size to 200x200
window.geometry("165x375")

# Executes the code in our window
window.mainloop()