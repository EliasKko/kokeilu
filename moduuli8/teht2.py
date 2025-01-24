
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
    ask = input("Anna maan maakoodi: ")
    ask = ("'" + ask + "'")
    sql = (f"select count(name) from airport where iso_country = {ask} and type =  'small_airport';")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        print("Pieniä lentokenttiä on: ", tulos)
        sql = (f"select count(name) from airport where iso_country = {ask} and type =  'medium_airport';")
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            print("Keskikokoisia lentokenttiä on: ", tulos)
            sql = (f"select count(name) from airport where iso_country = {ask} and type =  'heliport';")
            kursori = yhteys.cursor()
            kursori.execute(sql)
            tulos = kursori.fetchall()
            if kursori.rowcount > 0:
                print("Helikopterikenttiä on: ", tulos)

    return

hauki()
