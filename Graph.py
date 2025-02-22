import sys
def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step
def grabVarName(var):
    for name, value in globals().items():
        if value is var:
            return name
import sys
sys.path.append("Methods")
sys.path.append("Trig")
sys.path.append("Exponential_Logarithmic")
import pi
import Sine
import Cosine
import Tangent
import matplotlib.pyplot as plt
def plotGraphs(boolList, x, funcs):
    labelList = ["sin(x)", "cos(x)", "tan(x)"]
    colorList = ["red", "cyan", "lawngreen"]
    for index, b in enumerate(boolList):
        if b is True:
            plt.plot(x, funcs[index], label=labelList[index], color=colorList[index])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(pi.get_pi(2) * -8, pi.get_pi(2) * 8)
    plt.ylim(-5, 5)
    plt.xticks(ticks=[pi.get_pi(2) * -8,  pi.get_pi(2) * -4, 0, pi.get_pi(2) * 4, pi.get_pi(2) * 8], labels=["-8π", "-4π", "0", "4π", "8π"])
    plt.xticks(minor=True, ticks=[pi.get_pi(2) * -7, pi.get_pi(2) * -6, pi.get_pi(2) * -5, pi.get_pi(2) * -3, pi.get_pi(2) * -2, pi.get_pi(2) * -1, pi.get_pi(2), pi.get_pi(2) * 2, pi.get_pi(2) * 3, pi.get_pi(2) * 5, pi.get_pi(2) * 6, pi.get_pi(2) * 7], labels=["-7π", "-6π", "-5π", "-3π", "-2π", "-π", "π", "2π", "3π", "5π", "6π", "7π"])
    plt.yticks(ticks=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    plt.title("Functions")
    plt.legend(loc='lower left')
    plt.minorticks_on()
    plt.grid(True)
    plt.show()