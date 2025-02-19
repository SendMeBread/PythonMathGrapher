import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
import Sine, Cosine

def cot(theta):
    try:
        return Cosine.cos(theta)/Sine.sin(theta)
    except:
        pass
#print(round(cot(pi.get_pi(10)), 4))