from Tkinter import *
import Tkinter
from WER_final_c import *
from gtm_forMT import *
from Bleu import *

top=Tk()
L0 = Label(top, text="MT Evaluator",font="Times 24",fg="orange").grid(row=0,columnspan=2)
L1 = Label(top, text="Enter translated Sentence",).grid(row=1,column=0)
L2 = Label(top, text="Enter reference sentence",).grid(row=2,column=0)
L3 = Label(top, text="WER Score",).grid(row=3,column=0)
L4 = Label(top, text="GTM Score",).grid(row=4,column=0)
L5 = Label(top, text="BLEU 1gram Score",).grid(row=5,column=0)
L6 = Label(top, text="BLEU 2gram Score",).grid(row=6,column=0)
L7 = Label(top, text="BLEU 3gram Score",).grid(row=7,column=0)
L8 = Label(top, text="BLEU 4gram Score",).grid(row=8,column=0)


E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
E5 = Entry(top, bd =5)
E5.grid(row=5,column=1)
E6 = Entry(top, bd =5)
E6.grid(row=6,column=1)
E7 = Entry(top, bd =5)
E7.grid(row=7,column=1)
E8 = Entry(top, bd =5)
E8.grid(row=8,column=1)


def process():
    hypot=Entry.get(E1).lower()
    refer=Entry.get(E2).lower()
    r = hypot.split()
    h = refer.split()
    Entry.insert(E3,0,wer(r, h)) #wer takes parameters r and h as list
    Entry.insert(E4,0,gtm(refer,hypot)) #gtm takes parameters r and h as strings
    Entry.insert(E5,0,Bleu1gram(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E6,0,Bleu2gram(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E7,0,Bleu3gram(refer,hypot)) #bleu takes parameters r and h as strings
    Entry.insert(E8,0,Bleu4gram(refer,hypot)) #bleu takes parameters r and h as strings

B=Button(top, text ="Submit",font="Arial 10",command = process).grid(row=9,columnspan=2)
top.mainloop()
