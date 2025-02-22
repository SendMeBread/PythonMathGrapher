import sys
sys.path.append("../PythonMathGrapher/Methods")
import factorial
import pi
def cos(theta, A, B, C, D):
    result = 1
    sign = -1
    exp = 2
    for i in range(38):
        result += ((((B*theta)-C) ** exp)/factorial.factorial(exp))*sign
        sign *= -1
        exp += 2
    return round((A*result)-D, 4)
#print(round(cos(pi.get_pi(10)), 4))