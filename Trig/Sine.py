import sys
sys.path.append("../PythonMathGrapher/Methods")
import factorial
import pi
def sin(theta):
    result = theta
    sign = -1
    exp = 3
    for i in range(20):
        result += ((theta**exp)/factorial.factorial(exp))*sign
        sign *= -1
        exp += 2
    return round(result, 4)
#print(round(sin(pi.get_pi(10)*4), 10))