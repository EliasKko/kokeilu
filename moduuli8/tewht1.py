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
    sql = (f"select airport.name, country.name from airport, country where airport.ident = {ask} and airport.iso_country = country.iso_country;")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        print("Lentokenttä on: ", tulos)
    return
hauki()
