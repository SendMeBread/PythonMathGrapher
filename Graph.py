def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step

import sys
sys.path.append("/home/josephmbest/PythonMathGrapher/Methods")
sys.path.append("/home/josephmbest/PythonMathGrapher/Trig")
import pi
import Sine
import Cosine
import Tangent
import Secant
import Cosecant
import Cotangent
import matplotlib.pyplot as plt
x = []
for i in f_range(pi.get_pi(10) * -4, pi.get_pi(10) * 4, 0.0001):
    x.append(i)
sin_y = []
cos_y = []
tan_y = []
csc_y = []
sec_y = []
cot_y = []
for j in x:
    sin_y.append(Sine.sin(j))
    cos_y.append(Cosine.cos(j))
    tan_y.append(Tangent.tan(j))
    csc_y.append(Cosecant.csc(j))
    sec_y.append(Secant.sec(j))
    cot_y.append(Cotangent.cot(j))
    
plt.plot(x, sin_y, label="sin(x)", color="red")
plt.plot(x, cos_y, label="cos(x)", color="blue")
plt.plot(x, tan_y, label="tan(x)", color="green")
plt.plot(x, csc_y, label="csc(x)", color="orange")
plt.plot(x, sec_y, label="sec(x)", color="purple")
plt.plot(x, cot_y, label="cot(x)", color="olive")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(pi.get_pi(10) * -4, pi.get_pi(10) * 4)
plt.ylim(-3, 3)
plt.title("Trig Crap...")
plt.legend()
plt.grid(True)
plt.show()