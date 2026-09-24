import math as m
def sucet_stvorcov(n):
    sucet = 0;
    for k in range(n + 1):
        sucet = sucet + k * k
    return sucet
print(sucet_stvorcov(3))   

def aritmeticka_postupnost(a_nulty,d,n):
    for k in range(n):
        print(a_nulty + k*d)

aritmeticka_postupnost(10, 2, 7)


def geometricka_postupnost(a_nulty,q,n):
    for k in range(n):
        print(a_nulty * m.pow(q, k))

geometricka_postupnost(1,2,5)


def postupny_sucet_geometrickeho_radu(a_nulty,q,n):
    for k in range(n):
        sucet = (a_nulty * m.pow(q, k)) + (a_nulty * m.pow(q, k + 1))
        print(sucet)
postupny_sucet_geometrickeho_radu(1,2,5)  

'''
def grid(n):
    for k in range(n):
        for j in range(n):
            print("+ - - - - +", end='')
'''

def vynasob(a, b):
    sucet = 0
    for k in range(a):
        sucet = sucet + b
    return sucet
print(vynasob(5, 2))

'''
def tretia_mocnina(a):
    sucet = 0
    for i in range(3):
        for k in range(a):
            sucet = sucet + a
    return(sucet)
print(tretia_mocnina(5))
'''

def umocni(n, k):
    sucet = 1
    for q in range(k):
        sucet = vynasob(sucet,n)

    return sucet

    
print(umocni(2, 5))

