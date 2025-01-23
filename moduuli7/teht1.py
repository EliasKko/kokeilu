Vuodenajat = {}
Vuodenajat["8"]= "syksy"
Vuodenajat["9"]= "syksy"
Vuodenajat["10"]= "syksy"
Vuodenajat["11"]= "Talvi"
Vuodenajat["12"]= "Talvi"
Vuodenajat["1"]= "Talvi"
Vuodenajat["2"]= "Kevät"
Vuodenajat["3"]= "Kevät"
Vuodenajat["4"]= "Kevät"
Vuodenajat["5"]= "Kesä"
Vuodenajat["6"]= "Kesä"
Vuodenajat["7"]= "Kesä"
a = input("anna kuukausi numerona: ")
if a in Vuodenajat:
        print("Kuukausi on", Vuodenajat[a])
if a not in Vuodenajat:
        print("Ei ole kuukausi")