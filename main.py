from tkinter import filedialog
from tkinter import *
import os, sys, subprocess

Saved = False
saveLocation = None

root = Tk()
root.config(background="#2d2d2d")
root.title("Dev Studio")

def open_():
    global text, Saved, saveLocation
    Saved = True
    pla = sys.platform
    if pla == 'linux':
        saveLocation = filedialog.askopenfilename(initialdir="~/Documents", title="Select file to open")
    else:
        saveLocation = filedialog.askopenfilename(initialdir="/", title="Select file to open")
    
    text.delete("1.0", "end-1c")
    file1 = open(saveLocation, "r")
    text.insert("1.0", file1.read())
    file1.close()

def save():
    global text, Saved, saveLocation

    t = text.get("1.0", "end-1c")

    if Saved:
        file = open(saveLocation, "w+")
        file.write(t)
        file.close()
    else:
        Saved = True

        pla = sys.platform
        if pla == "linux":
            saveLocation = filedialog.asksaveasfilename(title="Select save location", initialdir="~/Documents")
        else:
            saveLocation = filedialog.asksaveasfilename(title="Select save location", initialdir="/")
        file = open(saveLocation, "w+")
        file.write(t)
        file.close()

def run():
    global output, platform
    pla = sys.platform
    if pla == 'linux':
        out = subprocess.check_output(["python3", saveLocation])
    else:
        out = subprocess.check_output("python " + saveLocation)
        
    output.config(text=out)

def FontHelvetica():
    global text
    text.config(font="Helvetica")
def FontCourier():
    global text
    text.config(font="Courier")
def ThemeDark():
    global text, root, output, bF
    text.config(background="#1d1d1d", fg="white", insertbackground="white")
    root.config(background="#2d2d2d")
    output.config(background="#2d2d2d", fg="white")
    bF.config(background="#2d2d2d")
def ThemeLight():
    global text, root, output, bF
    text.config(background="#f7f5f4", fg="black", insertbackground="black")
    root.config(background="#e5e5e5")
    output.config(background="#f7f5f4", fg="black")
    bF.config(background="#e5e5e5")

def init():
    global text, root, saveButton, Preferences, output, bF, tF

    bF = Frame(root)
    bF.grid(row=0, column=0, sticky="nsew")
    bF.config(background="#2d2d2d")

    saveButton = Button(bF, text="Save", command=save)
    saveButton.grid(row=1, column=1)

    openButton = Button(bF, text="Open", command=open_)
    openButton.grid(row=1, column=2)

    runButton = Button(bF, text="Run", command=run)
    runButton.grid(row=1, column=3)

    Preferences = Menubutton(bF, text="Preferences")
    Preferences.grid(row=1, column=4)

    Preferences.menu=Menu(Preferences, tearoff=0)
    Preferences["menu"] = Preferences.menu

    Helvetica = IntVar()
    Courier = IntVar()
    Light = IntVar()
    Dark = IntVar()

    text = Text(root)
    text.grid(sticky=N+S+E+W, row=2)
    text.config(background="#1d1d1d", fg="white", insertbackground="white", width="132", height="43")
    root.columnconfigure(0, weight=100)
    root.rowconfigure(2, weight=100)

    oF = Frame(root)
    oF.grid(row=3, sticky="nsew")
    oF.columnconfigure(0, weight=100)
    oF.rowconfigure(0, weight=100)
    output = Label(oF, background="#1d1d1d", fg="white", text="")
    output.grid(sticky="nsw", column=0, row=0)

    Preferences.menu.add_checkbutton(label="Courier", command=FontCourier)
    Preferences.menu.add_checkbutton(label="Helvetica", command=FontHelvetica)
    Preferences.menu.add_checkbutton(label="Dark Theme", command=ThemeDark)
    Preferences.menu.add_checkbutton(label="Light Theme", command=ThemeLight)

init()
while True:
    output.grid(sticky="we")
    root.mainloop()
