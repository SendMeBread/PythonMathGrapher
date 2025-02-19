import Sine
import sys
sys.path.append("../PythonMathGrapher/Methods")
import pi
def csc(theta):
    try:
        return 1/Sine.sin(theta)
    except:
        pass
#print(round(csc(pi.get_pi(10)), 4))