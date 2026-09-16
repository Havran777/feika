sekundy = int(7525)

hodiny = int(sekundy / 3600)
sekundy = int(sekundy - hodiny * 3600)
minuty = int(sekundy / 60)
sekundy = int(sekundy - minuty * 60)

'''
#s kvocientom 
hodiny = int(sekundy / 3600)
minuty = int((sekundy - (sekundy // 3600 * 3600)) / 60)
sekundy = int(sekundy - (minuty * 60) - (hodiny * 3600)) 
'''


print(hodiny)
print(minuty)
print(sekundy)