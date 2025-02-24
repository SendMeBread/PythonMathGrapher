import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
import Sine, Cosine

def tan(theta, A, B, C, D):
    try:
        return A*(Sine.sin(theta, 1, B, C, 0)/Cosine.cos(theta, 1, B, C, 0)) - D
    except:
        pass
#print(tan(pi.get_pi(10)))