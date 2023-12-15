from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import sys
import os

class GUI:

    def __init__(self):
        self.nroot = Tk()
        self.iusnames = self.parsenames("USnames.txt", True)
        self.ieunames = self.parsenames("EUnames.txt", True)
        self.usnames = self.parsenames("USnames.txt", False)
        self.eunames = self.parsenames("EUnames.txt", False)
        self.win()
        self.nroot.mainloop()
    
    def nl_clean(self, smd):
        count = -1
        for l in smd:
            count += 1
            smd[count] = l[:-l.count("\n")]
        return smd

    def parsenames(self, ref, lowercase):
        with open(ref, 'r') as n:
            listt = n.readlines()
            if lowercase:
                listt = self.imlazyLIST(self.nl_clean(listt))
            else:
                listt = self.nl_clean(listt)
            return listt
    
    def imlazy(self, stringy):
        return stringy.lower()
    
    def imlazyLIST(self, stringy):
        count = -1
        for s in stringy:
            count += 1
            stringy[count] = s.lower()
        return stringy
    
    def win(self):
        self.nroot.title("MKWii Translator")

        frame = Frame(self.nroot, borderwidth=2, relief="sunken")
        frame.grid(column=6, row=6, sticky=(N, E, S, W))
        self.nroot.columnconfigure(1, weight=1)
        self.nroot.rowconfigure(1, weight=1)

        self.us_label = Label(frame, text="Translate from NTSC")
        self.us_label.grid(column=1, row=1, sticky=(S, W), padx=10, pady=(10, 0))
        
        self.usString = StringVar()
        self.usname_entry = Entry(frame, textvariable=self.usString)
        self.usname_entry.grid(column=1, row=2, sticky=(N, E, W), padx=10, pady=5, ipadx=100, ipady=39)

        euflag = PhotoImage(file = r"images\jaffle.png")
        euflag = euflag.subsample(4, 4)
        eutrans = Button(frame, image=euflag, command=self.eutranslate)
        eutrans.photo = euflag
        eutrans.grid(column=2, row=2, sticky=(N), padx=5, pady=5)

        usflag = PhotoImage(file = r"images\burger.png")
        usflag = usflag.subsample(4, 4)
        ustrans = Button(frame, image=usflag, command=self.ustranslate)
        ustrans.photo = usflag
        ustrans.grid(column=2, row=2, sticky=(N), padx=5, pady=(60, 0))

        self.eu_label = Label(frame, text="Translate from PAL")
        self.eu_label.grid(column=3, row=1, sticky=(S, W), padx=10, pady=(10, 0))

        self.euString = StringVar()
        self.euname_entry = Entry(frame, textvariable=self.euString)
        self.euname_entry.grid(column=3, row=2, sticky=(N, E, W), padx=10, pady=5, ipadx=100, ipady=39)
    
    def eutranslate(self):
        # I originally wanted to have each translation hardcoded (for a reason I still don't know) but that would've
        # been WAY too clunky and would've made code that's awful to read
        cu = self.usString.get().lower()
        try:
            transname = self.iusnames.index(cu)
            self.euString.set(self.eunames[transname])
        except:
            self.euString.set(self.usString.get())
    
    def ustranslate(self):
        cu = self.euString.get().lower()
        try:
            transname = self.ieunames.index(cu)
            self.usString.set(self.usnames[transname])
        except:
            self.usString.set(self.euString.get())

a = GUI()