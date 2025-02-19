import Cosine
import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
def sec(theta):
    try:
        return 1/Cosine.cos(theta)
    except:
        pass
#print(round(sec(pi.get_pi(10)), 4))