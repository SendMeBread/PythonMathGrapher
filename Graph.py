import sys
def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step
def grabVarName(var):
    for name, value in globals().items():
        if value is var:
            return name
def graphVertAsymptote(x, color):
    plt.axvline(x, color=color, linestyle='--')
import sys
sys.path.append("Methods")
sys.path.append("Trig")
sys.path.append("Exponential_Logarithmic")
import pi
import matplotlib.pyplot as plt
plt.ion()
def plotGraphs(boolList, x, funcs, colors):
    labelList = ["sin(x)", "cos(x)", "tan(x)", "csc(x)", "sec(x)", "cot(x)"]
    for index, b in enumerate(boolList):
        if b is True:
            plt.plot(x, funcs[index], label=labelList[index], color=colors[index])
def showGraph():
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(pi.get_pi(2) * -6, pi.get_pi(2) * 6)
    plt.ylim(-5, 5)
    plt.xticks(ticks=[pi.get_pi(2) * -6,  pi.get_pi(2) * -3, 0, pi.get_pi(2) * 6, pi.get_pi(2) * 3], labels=["-6π", "-3π", "0", "3π", "6π"])
    plt.xticks(minor=True, ticks=[pi.get_pi(2) * -5, pi.get_pi(2) * -4, pi.get_pi(2) * -2, pi.get_pi(2) * -1, pi.get_pi(2) * 1, pi.get_pi(2) * 2, pi.get_pi(2), pi.get_pi(2) * 4, pi.get_pi(2) * 5], labels=["-5π", "-4π", "-2π", "-1π", "-π", "π", "2π", "4π", "5π"])
    plt.yticks(ticks=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    plt.title("Functions")
    plt.legend(loc='lower left')
    plt.minorticks_on()
    plt.grid(True)
    plt.show()