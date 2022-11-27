import tkinter.ttk as ttk
from tkinter import *
import szamitas

ablak = Tk()
ablak.minsize(640, 480)
ablak.title('Ösztöndíj index')
i = 2
lsz = 3
n = 2

def hozzaad():
    global i
    global lsz
    k = str(i)
    j = str(i+100)
    l = str(i+1000)
    l = ttk.Label(ablak, text=str(lsz)+'.'+' tárgy')
    l.grid(row=1+i, column=0)
    k = ttk.Entry(ablak, width=1, name=k)
    k.grid(row=1+i, column=1)
    j = ttk.Entry(ablak, width=1, name=j)
    j.grid(row=1 + i, column=2)
    lsz = lsz+1
    i = i+1

def getval():
    global i
    global n
    ink = []
    inj = []
    for o in range(2, i):
        #l = 0
        h = str(o)
        g = str(o+100)
        ink.append(int(ablak.nametowidget(h).get()))
        inj.append(int(ablak.nametowidget(g).get()))
        #l=l+1
    ink.append(int(kreditm.get()))
    ink.append(int(kreditm2.get()))

    inj.append(int(jegym.get()))
    inj.append(int(jegym2.get()))


    eredmeny['state'] = NORMAL
    eredmeny.insert(END, szamitas.szamolas(ink, inj))
    eredmeny['state'] = DISABLED
    gomb['state'] = DISABLED
    szamol['state'] = DISABLED




labkredit = ttk.Label(ablak, text='Kredit')
labkredit.grid(row=0, column=1)

labjegy = ttk.Label(ablak, text='Jegy')
labjegy.grid(row=0, column=2)

kreditm = ttk.Entry(ablak, width=1, name='defk1')
kreditm.grid(row=1, column=1)

labtargy1 = ttk.Label(ablak, text='1. tárgy: ')
labtargy1.grid(row=1, column=0)

kreditm2 = ttk.Entry(ablak, width=1, name='defk2')
kreditm2.grid(row=2, column=1)

labtargy2 = ttk.Label(ablak, text='2. tárgy: ')
labtargy2.grid(row=2, column=0)

jegym = ttk.Entry(ablak, width=1, name='defj1')
jegym.grid(row=1, column=2)

jegym2 = ttk.Entry(ablak, width=1, name='defj2')
jegym2.grid(row=2, column=2)

gomb = ttk.Button(ablak, text='+', command=hozzaad)
gomb.grid(row=1, column=3)

szamol = ttk.Button(ablak, text='Számolás', command=getval)
szamol.grid(row=2, column=3)

eredmeny = ttk.Entry(ablak, width=10, name='eredmeny', state=DISABLED, foreground="red")
eredmeny.grid(row=2, column=4)

mainloop()
