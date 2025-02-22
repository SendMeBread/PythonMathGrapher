import tkinter as tk
import subprocess
import Graph
import sys

sys.path.append("Methods")

win = tk.Tk()
win.title("Graph")

import Sine, Cosine, Tangent
import pi

screenW, screenH = win.winfo_screenwidth(), win.winfo_screenheight()
winW, winH = str(int(screenW/4)), str(int(screenH/4))
win.geometry(winW + "x" + winH + "+0+0")
sinInp = tk.Entry(win, width=20)
cosInp = tk.Entry(win, width=20)
tanInp = tk.Entry(win, width=20)
def getFuncs():
    graph.pack_forget()
    if sinBool.get() == 1:
        sinInp.pack()
    else:
        sinInp.pack_forget()
    if cosBool.get() == 1:
        cosInp.pack()
    else:
        cosInp.pack_forget()
    if tanBool.get() == 1:
        tanInp.pack()
    else:
        tanInp.pack_forget()
    graph.pack()
sinBool = tk.IntVar()
cosBool = tk.IntVar()
tanBool = tk.IntVar()

sinCheck = tk.Checkbutton(win, variable=sinBool, onvalue=1, offvalue=0)
sinCheck.config(selectcolor="black",  bg="lightgrey", fg="red", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Sine Function")
sinCheck.pack()

cosCheck = tk.Checkbutton(win, variable=cosBool, onvalue=1, offvalue=0)
cosCheck.config(selectcolor="black",  bg="lightgrey", fg="cyan", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Cosine Function")
cosCheck.pack()

tanCheck = tk.Checkbutton(win, variable=tanBool, onvalue=1, offvalue=0)
tanCheck.config(selectcolor="black",  bg="lightgrey", fg="lawn green", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Tangent Function")
tanCheck.pack()

def graphFuncs():
    xVals = []
    for i in Graph.f_range(pi.get_pi(10) * -8, pi.get_pi(10) * 8, 0.0001):
        xVals.append(i)
    args = []
    idList = []
    yVals = []
    if sinInp.get() != "":
        args = sinInp.get().split()
        idList.append(True)
        sinList = []
        for s in xVals:
            sinList.append(Sine.sin(s, float(args[0]), float(args[1]), float(args[2]), float(args[3])))
        yVals.append(sinList)
    else:
        idList.append(False)
        yVals.append([])

    if cosInp.get() != "":
        args = cosInp.get().split()
        idList.append(True)
        cosList = []
        for c in xVals:
            cosList.append(Cosine.cos(c, float(args[0]), float(args[1]), float(args[2]), float(args[3])))
        yVals.append(cosList)
    else:
        idList.append(False)
        yVals.append([])

    if tanInp.get() != "":
        args = tanInp.get().split()
        idList.append(True)
        tanList = []
        for t in xVals:
            tanList.append(Tangent.tan(t, float(args[0]), float(args[1]), float(args[2]), float(args[3])))
        yVals.append(tanList)
        yVals.append([])
    else:
        idList.append(False)
    Graph.plotGraphs(idList, xVals, yVals)
select = tk.Button(win, text="Confirm...", command=getFuncs)
select.pack()
graph = tk.Button(win, text="Graph!", command=graphFuncs)
errorText = tk.Text(win, state='disabled')
win.mainloop()