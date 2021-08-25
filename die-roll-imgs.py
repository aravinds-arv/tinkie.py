from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Die roll using Tkinter")
root.iconbitmap("./assets/python.ico")
root.geometry("700x450")

def rollEm():
    global imgList, dieLabel1, dieLabel2, dieLabel3
    dieNum1 = random.choice(imgList)
    dieNum2 = random.choice(imgList)
    dieLabel1.grid_forget()
    dieLabel2.grid_forget()
    dieLabel1 = Label(root, image=dieNum1)
    dieLabel2 = Label(root, image=dieNum2)
    dieLabel1.grid(row=2, column=0, pady=47)
    dieLabel2.grid(row=2, column=1, pady=47)

button = Button(root, text="Let's roll em", command=rollEm, bg="#5ebfff", fg="#fefefe", font=("poppins", 14))
button.grid(row=0, column=0, columnspan=2, padx=285, pady=25)

dieImg1 = ImageTk.PhotoImage(Image.open("./assets/die1.png"))
dieImg2 = ImageTk.PhotoImage(Image.open("./assets/die2.png"))

dieImg3 = ImageTk.PhotoImage(Image.open("./assets/die3.png"))
dieImg4 = ImageTk.PhotoImage(Image.open("./assets/die4.png"))
dieImg5 = ImageTk.PhotoImage(Image.open("./assets/die5.png"))
dieImg6 = ImageTk.PhotoImage(Image.open("./assets/die6.png"))

imgList = [dieImg1, dieImg2, dieImg3, dieImg4, dieImg5, dieImg6]

dieLabel1 = Label(root, image=dieImg1)
dieLabel2 = Label(root, image=dieImg2)
dieLabel1.grid(row=2, column=0, pady=47)
dieLabel2.grid(row=2, column=1, pady=47)

root.mainloop()