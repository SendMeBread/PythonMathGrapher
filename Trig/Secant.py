import Cosine
import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
def sec(theta, A, B, C, D):
    try:
        return A*(1/Cosine.cos(theta, 1, B, C, 0)) - D
    except:
        pass
#print(round(sec(pi.get_pi(10)), 4))