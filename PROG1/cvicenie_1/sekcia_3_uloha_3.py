import turtle as t

#patuholnik -> vnutorny uhol je 108 stupnov
#je tam 10 5-uholnikov -> treba posun o polovicu uhla
t.speed(110)
for j in range(10):
    for k in range(5):
        t.forward(50)
        t.left(72)
    t.left(36)
t.done()