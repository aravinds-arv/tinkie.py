from tkinter import *
import random

root = Tk()
root.title("Roll a die using Tkinter")
root.iconbitmap("./assets/python.ico")
root.geometry("550x450")

def roll():
    global die1, die2
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dieNum1 = random.choice(number)
    dieNum2 = random.choice(number)
    die1.grid_forget()
    die2.grid_forget()
    die1 = Label(root, text=dieNum1, font=('Helvetica', 260))
    die1.grid(row=1, column=0)
    die1 = Label(root, text=dieNum2, font=('Helvetica', 260))
    die1.grid(row=1, column=1)


button = Button(root, text="Let's roll em", command=roll)
button.grid(row=0, column=0, columnspan=2)

die1 = Label(root, text='\u2680', font=('Helvetica', 260))
die1.grid(row=1, column=0)
die2 = Label(root, text='\u2680', font=('Helvetica', 260))
die2.grid(row=1, column=1)

root.mainloop()