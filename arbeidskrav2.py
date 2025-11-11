# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 PY1010
"""

# %%
## oppgave 1
alder = int(input("Hvilket år er du født?"))
alder_2024 = 2024 - alder
print("Din alder i år, 2024, er", alder_2024)


# %%
## oppgave 2
import numpy as np
antall_elever = int(input("Skriv inn antall elever:"))
pizza = int(np.ceil(antall_elever/4)) # bruker int for helttall (slipper .0, i utprint) 
                                      # og bruker np.ceil for at det ikke skal runder ned
                                      
print("For", antall_elever, "elever må det kjøpe inn", pizza, "pizzaer til festen")


# %%
## oppgave 3
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180

print("Radianen til grad", int(v_grad), "er", round(v_rad, ndigits=4))

# %%
# oppgave 4
# a)
data = {"Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]}

# b) 
land = str(input("Skriv inn landet : "))
listLand = (data[land])
print(listLand[0], "er hovedstaden i", land, "og det er", listLand[1], "mill. innbyggere i", listLand[0])

# c) 
NyLand = str(input("Skriv inn nytt land: "))
NyBy = str(input("Hva er hovestanden til dette landet:"))
NyInbyggere = float(input("Hvor mange millioner inbyggere er det i hovedstaden:"))

data[NyLand] = [NyBy, NyInbyggere]

print(data)


# %%
## oppgave 4 
import numpy as np
a = float(input("Skriv inn lengden på a (cm):"))
b = float(input("Skriv inn lengden på b (cm):"))
r = a/2

areal_sirkel = np.pi*r**2
omkrets_sirkel = 2*np.pi*r
areal_trekant = a*b/2
c=np.sqrt(a**2 + b**2)
omkrets_trekant=c+b # kun omkrets av sidene som skal være med i totale omkrets 

ytre_omkrets=round(omkrets_trekant+omkrets_sirkel/2, ndigits=2)
areal=round(areal_trekant+areal_sirkel/2, ndigits=2)

print("Ytre omkrets er", ytre_omkrets, "cm og det totale arealet er", areal, "cm^2")

# %%
## Oppgave 5
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y)
