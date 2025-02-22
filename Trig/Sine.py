import sys
sys.path.append("../PythonMathGrapher/Methods")
import factorial
import pi
def sin(theta, A, B, C, D):
    result = (B*theta)-C
    sign = -1
    exp = 3
    for i in range(38):
        result += ((((B*theta)-C)**exp)/factorial.factorial(exp))*sign
        sign *= -1
        exp += 2
    return round((A*result) + D, 5)
#print(round(sin(pi.get_pi(2)*8, 1, 1, 0, 0), 10))