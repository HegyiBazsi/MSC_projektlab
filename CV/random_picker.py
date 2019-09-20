# I M P O R T   L I B S
import shutil
import numpy as np
from os import listdir
from os.path import isfile, join
from tkinter import filedialog
from tkinter import *


# M E N U
def menu():
    print("R A N D O M   P I C K E R   M E N U")
    print("1 - square train\n2 - star train\n3 - circle train\n")
    print("4 - square valid\n5 - star valid\n6 - circle valid\n")
    print("7 - square test\n8 - star test\n9 - circle test\n")


# S E L E C T O R
menu()
select = input()
sel = int(select)
if sel == 1:
    num_of_files = 10
    print("Square train")
elif sel == 2:
    num_of_files = 10
    print("Star train")
elif sel == 3:
    num_of_files = 10
    print("Circle train")
elif sel == 4:
    num_of_files = 10
    print("Square valid")
elif sel == 5:
    num_of_files = 10
    print("Star valid")
elif sel == 6:
    num_of_files = 10
    print("Circle valid")
elif sel == 7:
    num_of_files = 10
    print("Square test")
elif sel == 8:
    num_of_files = 10
    print("Star test")
elif sel == 9:
    num_of_files = 10
    print("Circle test")
else:
    exit()


# R A N D O M   P I C K E R
def random_picker():
    root = Tk()
    root.withdraw()

    print("\nSelect source")
    source = filedialog.askdirectory() + str("/")
    print("Select destination")
    destination = filedialog.askdirectory() + str("/")

    np.random.seed(num_of_files)
    files = [f for f in listdir(source) if isfile(join(source, f))]
    random_files = np.random.choice(files, num_of_files, replace=False)

    print("Moved file(s):", len(random_files))

    for f in random_files:
        print(f"File name: {f}")
        shutil.move(source + f, destination)
        print("Moved to", destination)


random_picker()
