from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

import sys

import pandas as pd

app = tk.Tk()
app.geometry("800x600")
app.resizable(0, 0)
last_step = "start"


def clear_frame():
    for widget in app.winfo_children():
        widget.destroy()


def go_last(last_p):
    clear_frame()
    if last_p == "start":
        start()


def exit_button(last):
    clear_frame()
    title = tk.Label(app, text="Are you sure to close the tools?", font=("Arial", 20), pady=120)
    title.pack()
    yes = tk.Button(text="Yes", font=("Arial", 20), command=sys.exit)
    yes.pack(side=LEFT, padx=120)
    no = tk.Button(text="No", font=("Arial", 20), command=lambda: go_last(last))
    no.pack(side=RIGHT, padx=120)


def start(last="start"):
    clear_frame()
    title = tk.Label(app, text="Boing International Trading Assistant Tools\n\n伯英工具箱", font=("Arial", 20), pady=120)
    title.pack()

    version = tk.Label(app, text="Version 0.0.1", font=("Arial", 10))
    version.pack(side=BOTTOM, pady=25)
    exit = tk.Button(text="Exit", font=("Arial", 20), command=lambda: exit_button("start"))
    exit.pack(side=BOTTOM,  pady=50)


start()
app.mainloop()
