def binary_split(a, b):
    if b == a + 1:
        Pab = -(6*a -5)*(2*a - 1)*(6*a - 1)
        Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)

        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab

def get_pi(n):
    #Chudnovsky algorithm
    Pln, Qln, Rln = binary_split(1, n)
    return ((426880 * (10005**(1/2))) * Qln) / (13591409*Qln + Rln)
#print(get_pi(10))