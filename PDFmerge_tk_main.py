# PDFMerge GUI for Python 2.7
# Kevin Falcetano August 2019

from PDFmerge_tk import *

if __name__ == "__main__":
    root = Tkinter.Tk(className=" PDF Merge")
    root.iconbitmap("icons/ayylmao2.ico")
    app = PDFwindow(master=root)
    app.mainloop()