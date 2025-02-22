import tkinter as tk
import subprocess
win = tk.Tk()
win.title("Graph")

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
sinCheck.config(selectcolor="green",  bg="lightgrey", fg="red", font=("Arial", 14), relief='groove', padx=4, pady=4, width=12, height=0, text="Sine Function")
sinCheck.pack()

cosCheck = tk.Checkbutton(win, variable=cosBool, onvalue=1, offvalue=0)
cosCheck.config(selectcolor="green",  bg="lightgrey", fg="red", font=("Arial", 14), relief='groove', padx=4, pady=4, width=12, height=0, text="Cosine Function")
cosCheck.pack()

tanCheck = tk.Checkbutton(win, variable=tanBool, onvalue=1, offvalue=0)
tanCheck.config(selectcolor="green",  bg="lightgrey", fg="red", font=("Arial", 14), relief='groove', padx=4, pady=4, width=12, height=0, text="Tangent Function")
tanCheck.pack()

def graphFuncs():
    args = []
    idList = []
    if sinInp.get() != "":
        sinArgs = sinInp.get().split()
        args += sinArgs
        idList.append("s")
    if cosInp.get() != "":
        cosArgs = cosInp.get().split()
        args += cosArgs
        idList.append("c")
    if tanInp.get() != "":
        tanArgs = tanInp.get().split()
        args += tanArgs
        idList.append("t")
    if len(args) > 0:
        result = subprocess.run(["python3", "Graph.py"] + args + idList, capture_output=True, text=True)
        if result.returncode == 0:
                print("Script executed successfully:")
                print(result.stdout)
        else:
            print("Script failed with error: ")
            print(result.stderr)
select = tk.Button(win, text="Confirm...", command=getFuncs)
select.pack()
graph = tk.Button(win, text="Graph!", command=graphFuncs)

win.mainloop()