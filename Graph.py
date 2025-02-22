import sys
def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step
import sys
sys.path.append("Methods")
sys.path.append("Trig")
sys.path.append("Exponential_Logarithmic")
import pi
import Sine
import Cosine
import Tangent
import matplotlib.pyplot as plt
x = []
for i in f_range(pi.get_pi(10) * -8, pi.get_pi(10) * 8, 0.0001):
    x.append(i)

sin_y, cos_y, tan_y = [], [], []
if "t" in sys.argv or "c" in sys.argv or "s" in sys.argv:
    if "t" in sys.argv:
        if "c" in sys.argv:
            if "s" in sys.argv:
                for s in x:
                    sin_y.append(Sine.sin(s, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
                plt.plot(x, sin_y, label=sys.argv[1] + "sin(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="red")
                
                for c in x:
                    cos_y.append(Cosine.cos(c, float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8])))
                plt.plot(x, cos_y, label=sys.argv[5] + "cos(" + sys.argv[6] + "x - " + sys.argv[7] + ") + " + sys.argv[8], color="blue")
                    
                for t in x:
                    tan_y.append(Tangent.tan(s, float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12])))
                plt.plot(x, tan_y, label=sys.argv[9] + "tan(" + sys.argv[10] + "x - " + sys.argv[11] + ") + " + sys.argv[12], color="green")
            else:
                for c in x:
                    cos_y.append(Cosine.cos(c, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
                plt.plot(x, cos_y, label=sys.argv[1] + "cos(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="blue")
                
                for t in x:
                    tan_y.append(Tangent.tan(t, float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12])))
                plt.plot(x, tan_y, label=sys.argv[9] + "tan(" + sys.argv[10] + "x - " + sys.argv[11] + ") + " + sys.argv[12], color="green")
        elif "s" in sys.argv:
            for s in x:
                sin_y.append(Sine.sin(s, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
            plt.plot(x, sin_y, label=sys.argv[1] + "sin(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="red")
            
            for t in x:
                tan_y.append(Tangent.tan(t, float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8])))
            plt.plot(x, tan_y, label=sys.argv[5] + "tan(" + sys.argv[6] + "x - " + sys.argv[7] + ") + " + sys.argv[8], color="green")
        else:
            for t in x:
                tan_y.append(Tangent.tan(t, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
            plt.plot(x, tan_y, label=sys.argv[1] + "tan(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="green")
    else:
        if "c" in sys.argv:
            if "s" in sys.argv:
                for s in x:
                    sin_y.append(Sine.sin(s, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
                plt.plot(x, sin_y, label=sys.argv[1] + "sin(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="red")
                
                for c in x:
                    cos_y.append(Cosine.cos(c, float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8])))
                plt.plot(x, cos_y, label=sys.argv[5] + "cos(" + sys.argv[6] + "x - " + sys.argv[7] + ") + " + sys.argv[8], color="blue")
                
            else:
                for c in x:
                    cos_y.append(Cosine.cos(c, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
                plt.plot(x, cos_y, label=sys.argv[1] + "cos(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="blue")
        else:
            for s in x:
                sin_y.append(Sine.sin(s, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
            plt.plot(x, sin_y, label=sys.argv[1] + "sin(" + sys.argv[2] + "x - " + sys.argv[3] + ") + " + sys.argv[4], color="red")

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