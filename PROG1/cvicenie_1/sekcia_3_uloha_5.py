import math
import turtle as t

def odmocnina(n):
    krok = 1
    for k in range(n):
        t.left(90)
        t.forward(krok)
        # s je vzdialenost od bodu 0, 0 - t.    
        s = t.distance(0, 0)
        # u je uhol bodu od daneho bodu - v tomto pripade 0, 0
        u = t.towards(0, 0)
        t.setheading(u)
        t.forward(s)
        #nastavenie uhla - kam smeruje
        t.setheading(180 + u)
        t.forward(s)
    return s

#print(odmocnina(5))
print(odmocnina(5))