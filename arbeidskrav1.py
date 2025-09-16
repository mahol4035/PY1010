# -*- coding: utf-8 -*-
"""
@author: Mariel.
Oppgaven er å finne ut kostandene for 1 års forbruk av El-bil og bensin-bil 
som har disse kostnadene. La oss tenke at bilene kjører 11000 km hvert år. 
Forsikring: 
    Elbil: 5000 kr/år. 
    Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 
    8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: 
    Elbil: 0,2 kWh/km. 
        Strømpris (antar kun hjemmelading): 2.00 kr/kWh. 
    Bensinbil: 1,0 kr/km.
Bomavgift: 
    Elbil: 0,1 kr/km. 
    Bensinbil: 0,3 kr/km.
"""
km=11000
"""
Kostnader Elbil for 1 år
"""
EL_F=5000 # forsikring per åt
EL_FA=8.35*365 # trafikkforsikringsavgift per år
EL_D=0.2*km #kwh/km: kwh brukt per år på lading
EL_L=2*EL_D #kr/kwh: kostander for kwh per år
EL_B=0.1*km #kr/km: bomavgift per år

KOST_EL=EL_B+EL_FA+EL_L+EL_B

print("Kostnader el-bil er", KOST_EL)
"""
Kostnader bensin bil for 1 år
"""
BENSIN_F=7500 # forsikring per år
BENSIN_FA=8.35*365 # trafikkforsikringsavgift per år
BENSIN_D=1*km #kr/km: kostander for bensin per år 
BENSIN_B=0.1*km #kr/km: kostander for bomavgift per år

KOST_BENSIN=BENSIN_B+BENSIN_FA+BENSIN_D+BENSIN_F

print("Kostnader bensin-bil er", KOST_BENSIN)

"""
Forskjell i kostnader
"""

DIFF=KOST_BENSIN-KOST_EL

print("Det koster", DIFF, "mer å kjøre bensil-bil enn el-bil")

