from os import system,startfile 
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd

def analyze():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = fd.askopenfilename(title = "Select file",filetypes = (("Data Files","*.data"),("All","*.txt")))
    print("==================ARCHIVE======================")
    print(filename)
    print("-----------------------------------------------")
    with open(filename, 'r') as reader:
        print(reader.read())
    print('-----------------------------------------------')

def main():
    analyze()
if __name__ == "__main__": 
    analyze()