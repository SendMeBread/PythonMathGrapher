import tkinter as tk
import Graph
import sys

sys.path.append("Methods")

win = tk.Tk()
win.title("Select Functions...")

import Sine, Cosine, Tangent, Cosecant, Secant, Cotangent
import pi, e

screenW, screenH = win.winfo_screenwidth(), win.winfo_screenheight()
winW, winH = int(screenW/2), int(screenH/2)
win.geometry(f"{winW}x{winH}+{int(winW/2)}+{int(winH/2)}")

sinInp = tk.Entry(win, width=20, bg="#FF0015")
cosInp = tk.Entry(win, width=20, bg="#14A3EB")
tanInp = tk.Entry(win, width=20, bg="#2CD34F")
cscInp = tk.Entry(win, width=20, bg="#00FFEA")
secInp = tk.Entry(win, width=20, bg="#EB5C14")
cotInp = tk.Entry(win, width=20, bg="#D32CB0")
    

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
    if cscBool.get() == 1:
        cscInp.pack()
    else:
        cscInp.pack_forget()
    if secBool.get() == 1:
        secInp.pack()
    else:
        secInp.pack_forget()
    if cotBool.get() == 1:
        cotInp.pack()
    else:
        cotInp.pack_forget()
    graph.pack()
sinBool = tk.IntVar()
cosBool = tk.IntVar()
tanBool = tk.IntVar()
cscBool = tk.IntVar()
secBool = tk.IntVar()
cotBool = tk.IntVar()

#Numpad:

#Trig Functions (Including Recipricals):
sinCheck = tk.Checkbutton(win, variable=sinBool, onvalue=1, offvalue=0)
sinCheck.config(selectcolor="black",  bg="lightgrey", fg="#FF0015", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Sine Function")
sinCheck.pack()

cosCheck = tk.Checkbutton(win, variable=cosBool, onvalue=1, offvalue=0)
cosCheck.config(selectcolor="black",  bg="lightgrey", fg="#14A3EB", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Cosine Function")
cosCheck.pack()

tanCheck = tk.Checkbutton(win, variable=tanBool, onvalue=1, offvalue=0)
tanCheck.config(selectcolor="black",  bg="lightgrey", fg="#2CD34F", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Tangent Function")
tanCheck.pack()

cscCheck = tk.Checkbutton(win, variable=cscBool, onvalue=1, offvalue=0)
cscCheck.config(selectcolor="black",  bg="lightgrey", fg="#00FFEA", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Cosecant Function")
cscCheck.pack()

secCheck = tk.Checkbutton(win, variable=secBool, onvalue=1, offvalue=0)
secCheck.config(selectcolor="black",  bg="lightgrey", fg="#EB5C14", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Secant Function")
secCheck.pack()

cotCheck = tk.Checkbutton(win, variable=cotBool, onvalue=1, offvalue=0)
cotCheck.config(selectcolor="black",  bg="lightgrey", fg="#D32CB0", font=("Arial", 14), relief='groove', padx=4, pady=4, width=20, height=0, text="Cotangent Function")
cotCheck.pack()
def graphFuncs():
    InpList = [sinInp.get(), cosInp.get(), tanInp.get(), cscInp.get(), secInp.get(), cotInp.get()]
    funcList = [Sine.sin, Cosine.cos, Tangent.tan, Cosecant.csc, Secant.sec, Cotangent.cot]
    idList = []
    yVals = []
    xVals=[]
    colorList = ["#FF0015", "#14A3EB", "#2CD34F", "#00FFEA", "#EB5C14", "#D32CB0"]
    for x in Graph.f_range(pi.get_pi(10) * -6, pi.get_pi(10) * 6, 0.0001):
        xVals.append(x)
    for index, i in enumerate(InpList):
        if i != "":
            args = i.split()
            idList.append(True)
            vals=[]
            for x_val in xVals:
                y = funcList[index](x_val, float(args[0]), float(args[1]), float(args[2]), float(args[3]))
                if y == None:
                    Graph.graphVertAsymptote(x_val, colorList[index])
                vals.append(y)
            yVals.append(vals)
        else:
            idList.append(False)
            yVals.append([])
    Graph.plotGraphs(idList, xVals, yVals, colorList)
    Graph.showGraph()
select = tk.Button(win, text="Confirm...", command=getFuncs)
select.pack()
graph = tk.Button(win, text="Graph!", command=graphFuncs)
win.mainloop()