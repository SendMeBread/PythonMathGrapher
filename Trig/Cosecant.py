import Sine
import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
def csc(theta, A, B, C, D):
    try:
        return A*(1/(Sine.sin(theta, 1, B, C, 0))) - D
    except:
        pass
#print(csc(pi.get_pi(2), 1, 1, 0, 0))