from Tkinter import *
import Tkinter
from WER_final_c import *

top=Tk()
L1 = Label(top, text="MT Evaluator",font="Times 24",fg="orange").grid(row=0,columnspan=4)
L2 = Label(top, text="Enter translated Sentence",).grid(row=1,column=0)
L3 = Label(top, text="Enter reference sentence",).grid(row=2,column=0)
L4 = Label(top, text="WER Score",).grid(row=4,column=0)

E1 = Entry(top, bd =5)
E1.grid(row=1,column=3)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=3)
E3 = Entry(top, bd =5)
E3.grid(row=4,column=3)


def process():
    hypot=Entry.get(E1)
    refer=Entry.get(E2)
    r = hypot.split()
    h = refer.split()
    Entry.insert(E3,0,wer(r, h))

B=Button(top, text ="Submit",font="Arial 10",command = process).grid(row=5,column=1)
top.mainloop()
