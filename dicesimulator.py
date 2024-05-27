import tkinter as tk
from tkinter import *
import random
guiwindow = tk.Tk()
guiwindow.title("Dice Simulator")
guiwindow.geometry("500x500")


dicelabel = tk.Label(guiwindow, text="Dice", font=("Arial", 72))
dicelabel.pack(padx=20, pady=20)


textbox = tk.Text(guiwindow, font=("Arial",16))


def rolldice():
    
    dice = random.randint(1, 6)
    if dice == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print(" ")
    if dice == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print(" ")
    if dice == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print(" ")
    if dice == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print(" ")
    if dice == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print(" ")
    if dice == 6:
        print("[0  0]")
        print("[0  0]")
        print("[0  0]")
        print(" ")
    dicelabel.config(text=str(dice))


rollbutton = tk.Button(guiwindow, text="Roll Dice", command=rolldice)
rollbutton.pack(pady=10,padx=10)


guiwindow.mainloop()
