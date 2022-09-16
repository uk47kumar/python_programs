import builtins
from tkinter import*
from tkinter import font
from matplotlib import pyplot as plt
import seaborn as sns
from numpy import random

# Title-Probability values for different distribution
# @Author-Ujjwal kumar (11202773)
# @Author-Ashish kumar (11202772)
# Date-03/01/2022


window = Tk()
window.title("Distribution")


def Poissondistribution():
    lamp = int(uservalue1p.get())
    sizep = int(uservalue2p.get())
    xp = random.poisson(lamp, sizep)
    sns.distplot(random.poisson(lamp, sizep), kde=False)
    plt.show()
    print(xp)
    t30.delete("1.0", END), t30.insert(END, xp)


l00 = Label(window, text="\nPoisson Distribution: \n")
l10 = Label(window, text="rate")
l11 = Label(window, text="Size - ", )
uservalue1p = StringVar()
uservalue2p = StringVar()
e20 = Entry(window, textvariable=uservalue1p)
e21 = Entry(window, textvariable=uservalue2p)
b23 = Button(window, text="Claculate", command=Poissondistribution,)
l300 = Label(window, text="Result: ")
t30 = Text(window, height=1, width=40)
l00.grid(row=0, columnspan=2)
l10.grid(row=1, column=0)
l11.grid(row=1, column=1)
e20.grid(row=2, column=0)
e21.grid(row=2, column=1)
b23.grid(row=2, column=4)
l300.grid(row=4, columnspan=1)
t30.grid(row=4, columnspan=4)


def binomialdistribution():
    nb = int(uservalue1b.get())
    pb = float(uservalue2b.get())
    sizeb = int(uservalue3b.get())
    xb = random.binomial(nb, pb, sizeb)
    sns.distplot(random.binomial(nb, pb, sizeb), hist=True, kde=False)
    plt.show()
    t80.delete("1.0", END), t80.insert(END, xb)


l50 = Label(
    window, text="\nBinomial Distribution:\n", )
l60 = Label(window, text="No of Trails")
l61 = Label(window, text="Probability", )
l62 = Label(window, text="Size")
uservalue1b = StringVar()
uservalue2b = StringVar()
uservalue3b = StringVar()
e70 = Entry(window, textvariable=uservalue1b)
e71 = Entry(window, textvariable=uservalue2b)
e72 = Entry(window, textvariable=uservalue3b)
b73 = Button(window, text="Claculate", command=binomialdistribution,)
l800 = Label(window, text="Result: ")
t80 = Text(window, height=1, width=40)
l50.grid(row=5, columnspan=2)
l60.grid(row=6, column=0)
l61.grid(row=6, column=1)
l62.grid(row=6, column=2)
e70.grid(row=7, column=0)
e71.grid(row=7, column=1)
e72.grid(row=7, column=2)
b73.grid(row=7, column=4)
l800.grid(row=8, columnspan=1)
t80.grid(row=8, columnspan=4)


def normaldistribution():
    locn = float(uservalue1n.get())
    scalen = float(uservalue2n.get())
    sizeAn = int(uservalue3n.get())
    sizeBn = int(uservalue4n.get())
    xn = random.normal(locn, scalen, size=(sizeAn, sizeBn))
    sns.distplot(random.normal(xn), hist=False)
    plt.show()
    print(xn)
    t130.delete("1.0", END),
    t130.insert(END, xn)


l100 = Label(window, text="\nNormal Distribution:\n", )
l110 = Label(window, text="Mean")
l111 = Label(window, text="Standard Deviation", )
l112 = Label(window, text="Size (A) ")
l113 = Label(window, text="Size (B)")
uservalue1n = StringVar()
uservalue2n = StringVar()
uservalue3n = StringVar()
uservalue4n = StringVar()
e120 = Entry(window, textvariable=uservalue1n)
e121 = Entry(window, textvariable=uservalue2n)
e122 = Entry(window, textvariable=uservalue3n)
e123 = Entry(window, textvariable=uservalue4n)
b123 = Button(window, text="Claculate", command=normaldistribution, )
l1300 = Label(window, text="Result: ")
t130 = Text(window, height=2, width=30)
l100.grid(row=10, columnspan=2)
l110.grid(row=11, column=0)
l111.grid(row=11, column=1)
l112.grid(row=11, column=2)
l113.grid(row=11, column=3)
e120.grid(row=12, column=0)
e121.grid(row=12, column=1)
e122.grid(row=12, column=2)
e123.grid(row=12, column=3)
b123.grid(row=12, column=4)
t130.grid(row=14, columnspan=4)
l1300.grid(row=14, columnspan=1)
t130.grid(row=14, columnspan=4)
window.mainloop()
