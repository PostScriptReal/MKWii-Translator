from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import sys
import os

class GUI:

    def __init__(self):
        self.nroot = Tk()
        self.scrdir = os.getcwd().replace("\\", "/") + "/"
        self.win()
        self.nroot.mainloop()
    
    def imlazy(self, stringy):
        return stringy.lower()
    
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
        cu = self.usString.get().lower()
        if cu == "dk summit":
            self.euString.set("DK's Snowboard Cross")
        elif cu == "chain chomp wheel":
            self.euString.set("Chain Chomp Roulette")
        elif cu == "galaxy colosseum":
            self.euString.set("Galaxy Arena")
        elif cu == self.imlazy("Booster Seat"):
            self.euString.set("Baby Booster")
        elif cu == self.imlazy("Mini Beast"):
            self.euString.set("Concerto")
        elif cu == self.imlazy("Rally Romper"):
            self.euString.set("Tiny Titan")
        elif cu == self.imlazy("Jet Bubble"):
            self.euString.set("Bubble Bike")
        else:
            self.euString.set(cu)
    
    def ustranslate(self):
        cu = self.euString.get().lower()
        if cu == "dk's snowboard cross":
            self.usString.set("DK Summit")
        elif cu == "chain chomp roulette":
            self.usString.set("Chain Chomp Wheel")
        elif cu == "galaxy arena":
            self.usString.set("Galaxy Colosseum")
        elif cu == "baby booster":
            self.usString.set("Booster Seat")
        elif cu == self.imlazy("Concerto"):
            self.usString.set("Mini Beast")
        elif cu == self.imlazy("Rally Romper"):
            self.usString.set("Tiny Titan")
        elif cu == self.imlazy("Bubble Bike"):
            self.usString.set("Jet Bubble")
        else:
            self.usString.set(cu)

a = GUI()