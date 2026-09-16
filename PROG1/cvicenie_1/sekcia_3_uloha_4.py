import turtle as t

krok = 75

t.speed(1)
t.forward(krok)

for k in range(5):
    t.left(90)
    t.forward(krok)
    # s je vzdialenost od bodu 0, 0 - t.    
    s = t.distance(0, 0)
    # u je uhol bodu od daneho bodu - v tomto pripade 0, 0
    u = t.towards(0, 0)
    t.setheading(u)
    t.forward(s)
    t.setheading(180 + u)
    t.forward(s)

t.left(90)
t.forward(krok)
t.done()