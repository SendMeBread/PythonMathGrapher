import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
import Sine, Cosine

def tan(theta):
    try:
        return Sine.sin(theta)/Cosine.cos(theta)
    except:
        pass
#print(tan(pi.get_pi(10)))