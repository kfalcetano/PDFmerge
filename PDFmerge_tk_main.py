# PDFMerge GUI for Python 2.7
# Kevin Falcetano August 2019

from PDFmerge_tk import *

if __name__ == "__main__":
    root = tk.Tk(className=" PDF Merge")
    root.iconbitmap("icons/ayylmao2.ico")
    app = Application(master=root)
    app.mainloop()