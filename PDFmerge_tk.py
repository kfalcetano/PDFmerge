# PDFMerge GUI for Python 2.7
# Kevin Falcetano August 2019

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox, tkFont, ScrolledText
from PyPDF2 import PdfFileMerger
import os

class Application(Tkinter.Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.pack(fill="both", expand=1)
        self.default_font = tkFont.Font(family="Helvetica",size = 10)
        self.filenames = list()
        self.create_widgets() 

    def create_widgets(self):
        self.flist = ScrolledText.ScrolledText(self, height=12, width = 80)
        self.flist["font"] = self.default_font
        self.flist.pack(side="left",fill="both",expand=1)
        self.flist.insert(Tkinter.END,"PDF Paths Listed Here:\n\n")
        self.flist.config(state="disabled")
        
        self.right = Tkinter.Frame(self)
        self.right.pack(side="right",padx=20)

        self.browse = Tkinter.Button(master=self.right)
        self.browse["text"] = "Add a PDF"
        self.browse["command"] = self.ask_filename
        self.browse["font"] = self.default_font
        self.browse.configure(bg = "light gray")
        self.browse.pack(pady=20,ipadx=5,ipady=5)

        self.merge = Tkinter.Button(master=self.right)
        self.merge["text"]= "Merge"
        self.merge["command"] = self.merge_from_list
        self.merge["font"] = self.default_font
        self.merge.configure(bg = "light gray")
        self.merge.pack(side="bottom",pady=35,ipadx=18,ipady=10)

        self.clear = Tkinter.Button(master=self.right)
        self.clear["text"] = "Clear List"
        self.clear["command"] = self.clear_list
        self.clear["font"] = self.default_font
        self.clear.configure(bg = "light gray")
        self.clear.pack(side="bottom",ipadx=5,ipady=5) 

    def ask_filename(self):
        filename = tkFileDialog.askopenfilename(title = "Select PDFs",filetypes=(("PDF files","*.pdf"),("All Files","*.*")))
        if filename != "":
            self.update_file_list(filename)

    def merge_from_list(self):
        if len(self.filenames)==0:
            tkMessageBox.showerror(title="Error",message="Plese select at least one file.")
        else:
            self.save_file()

    def save_file(self):
        filename = tkFileDialog.asksaveasfilename(filetypes=(("PDF files","*.pdf"),("All Files","*.*")),defaultextension=".pdf")
        if filename != "":
            merge_pdfs(filename,self.filenames)
            self.show_file_saved(filename)
    
    def show_file_saved(self, filename):
            self.clear_list()
            self.flist.config(state="normal")
            self.flist.insert(1.0,"Merge saved to: "+filename+"\n")
            self.flist.config(state="disabled")       
            
    def update_file_list(self, filename):
        self.flist.config(state="normal")
        self.flist.insert(Tkinter.END,str(self.filenames.__len__()+1)+". "+filename+"\n")
        self.filenames.append(filename)
        self.flist.config(state="disabled")
    
    def clear_list(self):
        self.flist.config(state="normal")
        del self.filenames[:]
        self.flist.delete(1.0,Tkinter.END)
        self.flist.insert(Tkinter.END,"PDF Paths Listed Here:\n\n")
        self.flist.config(state="disabled")

def merge_pdfs(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    for path in input_paths:
        pdf_merger.append(path)
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

if __name__ == "__main__":
    root = Tkinter.Tk(className=" PDF Merge")
    root.iconbitmap("icons/ayylmao2.ico")
    app = Application(master=root)
    app.mainloop()    