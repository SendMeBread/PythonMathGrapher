import factorial
def e():
    e = 1
    den = 1
    for i in range (100):
        e += 1/factorial.factorial(den)
        den += 1
    return e
#print(e())