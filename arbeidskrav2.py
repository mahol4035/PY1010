# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 PY1010
"""

# %%
## oppgave 1
alder = int(input("Hvilket år er du født?")) #input fra bruker
alder_2024 = 2024 - alder #regnestykke for alder i 2024
print("Din alder i år, 2024, er", alder_2024)


# %%
## oppgave 2
import numpy as np #importere biblotek for å bruke np.ceil
antall_elever = int(input("Skriv inn antall elever:"))
pizza = int(np.ceil(antall_elever/4)) # bruker int for helttall (slipper .0, i utprint) 
                                      # og bruker np.ceil for at det ikke skal runde ned men opp
                                      
print("For", antall_elever, "elever må det kjøpe inn", pizza, "pizzaer til festen")


# %%
## oppgave 3
import numpy as np # importerer for å bruke np.pi
v_grad = float(input('Skriv inn gradtallet:' )) # bruker skriver inn gradtallet
v_rad = v_grad*np.pi/180 # regnestyppe for å finne radianer

print("Radianen til grad", int(v_grad), "er", round(v_rad, ndigits=4))

# %%
# oppgave 4
# a) lage data
data = {"Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]}

# b) 
land = str(input("Skriv inn landet : ")) #skriv inn landet man ønsker informasjon fra
listLand = (data[land]) #ekstraherer og omgjør til liste for landet slik at det er mulig å printe ønsker info
print(listLand[0], "er hovedstaden i", land, "og det er", listLand[1], "mill. innbyggere i", listLand[0])

# c) 
# bruker legger til nytt variablene nytt land, by og inbyggerer
NyLand = str(input("Skriv inn nytt land: ")) 
NyBy = str(input("Hva er hovestanden til dette landet:"))
NyInbyggere = float(input("Hvor mange millioner inbyggere er det i hovedstaden:"))

# variablene brukes til å legge inn i data
data[NyLand] = [NyBy, NyInbyggere] 

print(data)

# %%
## oppgave 4 
import numpy as np
a = float(input("Skriv inn lengden på a (cm):")) #float betyr at det kan være komma
b = float(input("Skriv inn lengden på b (cm):"))
r = a/2 # regnestykke for radius

areal_sirkel = np.pi*r**2 #arealet for sirkelen
omkrets_sirkel = 2*np.pi*r #omrekts for sirkelen
areal_trekant = a*b/2 # arealet for trekant
c=np.sqrt(a**2 + b**2) # finne hypotenusen 
omkrets_trekant=c+b # kun omkrets av de sidene som skal være med i totale omkrets 

ytre_omkrets=round(omkrets_trekant+omkrets_sirkel/2, ndigits=2) # bare havle sirkelen er med i omkretensen, for finere utput kun 2 digits etter komme
areal=round(areal_trekant+areal_sirkel/2, ndigits=2) # bare halve sirkelen er med i arealet

print("Ytre omkrets er", ytre_omkrets, "cm og det totale arealet er", areal, "cm^2")

# %%
## Oppgave 5
import matplotlib.pyplot as plt #importerer for plotte funksjonen 
import numpy as np

x = np.linspace(-10, 10, 200) # 200 punkter mellom -10 og 10
y = -x**2 - 5 # y er en funksjon av x

plt.plot(x, y) # plotter x mot y
