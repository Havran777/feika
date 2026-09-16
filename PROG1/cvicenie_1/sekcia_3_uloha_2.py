import turtle as t

#vzorec na vypocet vnutorneho uhla mnohouholnika
# uhol = ((n - 2) * 180) / n

def nuholnik(n):
    for k in range(n):
        t.forward(50)
        t.left(180 - (((n - 2) * 180) / n))
    t.done()

nuholnik(13)