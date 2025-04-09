import mysql.connector
from flask import Flask
from flask import Response
import json
yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port= 3306,
            database='flight_game',
            user= 'root',
            password='Ip802mok223_',
            autocommit=True
            )
app = Flask(__name__)
@app.route('/hauki/<icao>')
def hauki(icao):
    icao = ("'" + icao + "'")
    sql = (f"select airport.name, airport.municipality from airport, country where airport.ident = {icao};")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
         kenttä = {
            "ICAO":icao,
            "Name":tulos[0][0],
            "Municipality":tulos[0][1]
        }
    #return str(kenttä)

    jsonvast = json.dumps(kenttä)
    return Response(response=jsonvast, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)