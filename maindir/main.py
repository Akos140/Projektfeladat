import tkinter.ttk as ttk
from tkinter import *
import szamitas

re = False
class atlag:
    def __init__(self):
        global re
        re = False

        self.ablak = Tk()
        self.ablak.minsize(100, 100)
        self.ablak.title('Ösztöndíj index')

        def validate(P):
            if len(P) == 0:
                return True
            elif len(P) == 1 and P.isdigit():
                return True
            else:
                return False

        self.vcmd = (self.ablak.register(validate), '%P')
        self.i = 2
        self.lsz = 3
        self.n = 2
        self.labkredit = ttk.Label(self.ablak, text='Kredit')
        self.labkredit.grid(row=0, column=1)

        self.labjegy = ttk.Label(self.ablak, text='Jegy')
        self.labjegy.grid(row=0, column=2)

        self.kreditm = ttk.Entry(self.ablak, width=1, name='defk1', validate="key", validatecommand=self.vcmd)
        self.kreditm.grid(row=1, column=1)

        self.labtargy1 = ttk.Label(self.ablak, text='1. tárgy: ')
        self.labtargy1.grid(row=1, column=0)

        self.kreditm2 = ttk.Entry(self.ablak, width=1, name='defk2', validate="key", validatecommand=self.vcmd)
        self.kreditm2.grid(row=2, column=1)

        self.labtargy2 = ttk.Label(self.ablak, text='2. tárgy: ')
        self.labtargy2.grid(row=2, column=0)

        self.jegym = ttk.Entry(self.ablak, width=1, name='defj1', validate="key", validatecommand=self.vcmd)
        self.jegym.grid(row=1, column=2)

        self.jegym2 = ttk.Entry(self.ablak, width=1, name='defj2', validate="key", validatecommand=self.vcmd)
        self.jegym2.grid(row=2, column=2)

        self.gomb = ttk.Button(self.ablak, text='+', command=self.hozzaad)
        self.gomb.grid(row=1, column=3)

        self.szamol = ttk.Button(self.ablak, text='Számolás', command=self.getval)
        self.szamol.grid(row=2, column=3)

        self.eredmeny = ttk.Entry(self.ablak, width=10, name='eredmeny', state=DISABLED, foreground="red")
        self.eredmeny.grid(row=2, column=4)

        self.reset = ttk.Button(self.ablak, text='Reset', command=self.resetting)
        self.reset.grid(row=3, column=3)



        mainloop()

    def resetting(self):
        global re
        re = True
        szamitas.index = 0
        self.ablak.destroy()

    def hozzaad(self):

        k = str(self.i)
        j = str(self.i+100)
        l = str(self.i+1000)
        l = ttk.Label(self.ablak, text=str(self.lsz)+'.'+' tárgy: ')
        l.grid(row=1+self.i, column=0)
        k = ttk.Entry(self.ablak, width=1, name=k, validate="key", validatecommand=self.vcmd)
        k.grid(row=1+self.i, column=1)
        j = ttk.Entry(self.ablak, width=1, name=j, validate="key", validatecommand=self.vcmd)
        j.grid(row=1 + self.i, column=2)
        self.lsz = self.lsz+1
        self.i = self.i+1

    def getval(self):

        self.ink = []
        self.inj = []
        for o in range(2, self.i):
            #l = 0
            h = str(o)
            g = str(o+100)
            self.ink.append(int(self.ablak.nametowidget(h).get()))
            self.inj.append(int(self.ablak.nametowidget(g).get()))
            #l=l+1
        self.ink.append(int(self.kreditm.get()))
        self.ink.append(int(self.kreditm2.get()))

        self.inj.append(int(self.jegym.get()))
        self.inj.append(int(self.jegym2.get()))

        self.eredmeny['state'] = NORMAL
        self.eredmeny.insert(END, szamitas.szamolas(self.ink, self.inj))
        self.eredmeny['state'] = DISABLED
        self.gomb['state'] = DISABLED
        self.szamol['state'] = DISABLED
atlag()
while re:
    atlag()





