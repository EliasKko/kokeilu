import geopy.geocoders
from geopy import distance
from geopy.geocoders import Nominatim
lista1 = []
lista2 = []

import mysql.connector
yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port= 3306,
            database='flight_game',
            user= 'root',
            password='Ip802mok223_',
            autocommit=True
            )
def hauki():
    ask = input("Anna lentokentän ICAO: koodi: ")
    ask = ("'" + ask + "'")
    sql = (f"select latitude_deg, longitude_deg from airport where airport.ident ={ask}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchall()
    if kursori.rowcount >0:
        lista1.append(tulos1)
        ask = input("Anna lentokentän ICAO: koodi: ")
        ask = ("'" + ask + "'")
        sql = (f"select latitude_deg, longitude_deg from airport where airport.ident ={ask}")
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos2 = kursori.fetchall()
        if kursori.rowcount > 0:
            lista2.append(tulos2)
    return
hauki()
from geopy import distance
yks = (lista1)
kaks = (lista2)
print("Etäisyys on ", int((distance.distance(yks, kaks).km)), "kilometriä")
