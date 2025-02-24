import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
import Sine, Cosine

def cot(theta, A, B, C, D):
    try:
        return A*(Cosine.cos(theta, 1, B, C, 0)/Sine.sin(theta, 1, B, C, 0)) - D
    except:
        pass
#print(round(cot(pi.get_pi(10)), 4))