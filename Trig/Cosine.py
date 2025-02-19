import sys
sys.path.append("../PythonMathGrapher/Methods")
import factorial
import pi
def cos(theta):
    result = 1
    sign = -1
    exp = 2
    for i in range(20):
        result += ((theta ** exp)/factorial.factorial(exp))*sign
        sign *= -1
        exp += 2
    return round(result, 4)
#print(round(cos(pi.get_pi(10)), 4))