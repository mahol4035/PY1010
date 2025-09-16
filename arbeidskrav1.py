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
EL_FORSIKRING = 5000 # forsikring per år
EL_TRAF_FORSIKRING = 8.35*365 # trafikkforsikringsavgift per år
EL_KWH = 0.2*km #kwh per km: kwh brukt per år på lading
EL_LADING = 2*EL_KWH #kr per kwh: kostander for kwh per år
EL_BOM = 0.1*km #kr per km: bomavgift per år

KOST_EL = EL_FORSIKRING + EL_TRAF_FORSIKRING + EL_LADING + EL_BOM #summerer alle kostnader

print("Kostnader for 1 år forbuk med el-bil er", KOST_EL)
"""
Kostnader bensin bil for 1 år
"""
BENSIN_FORSIKRING = 7500 # forsikring per år
BENSIN_TRAF_FORSIKRING = 8.35*365 # trafikkforsikringsavgift per år
BENSIN_BENSIN = 1*km #kr per km: kostander for bensin per år 
BENSIN_BOM = 0.1*km #kr per km: kostander for bomavgift per år

KOST_BENSIN= BENSIN_FORSIKRING + BENSIN_TRAF_FORSIKRING + BENSIN_BENSIN + BENSIN_BOM #summerer alle kostnader

print("Kostnader for 1 år forbuk me bensin-bil er", KOST_BENSIN)

"""
Forskjell i kostnader
"""

DIFF= KOST_BENSIN - KOST_EL #kostnad av bensin bil minus kostand av el bil

print("Det koster", DIFF, "mer å kjøre bensil-bil enn el-bil")

