import os
import shutil
from tkinter import filedialog
from tkinter import *


def fileMover():
    root = Tk()
    root.withdraw()
    print("Choose destination")
    destination = filedialog.askdirectory() + str("/")
    print("Choose source")
    source = filedialog.askdirectory() + str("/")
    Human = os.listdir(source)
    for f in Human:
        shutil.move(source + f, destination)
        print(f, "moved to", destination, "\n")


fileMover()
