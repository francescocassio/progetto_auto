def calcola_distanza(partenza, destinazione):
    from geopy.distance import geodesic

    # Coordinate latitudine e longitudine (esempio: Roma e Milano)

    diz_coord = {
        "roma": (41.9028, 12.4964),
        "milano": (45.4642, 9.1900),
        "bologna": (44.2938, 11.2034),
        "torino": (45.0424, 7.4032),
        "venezia" : (45.2548, 12.1920),
        "bari": (41.1171, 16.8718)
    }

    # Calcolo distanza in km
    distanza = geodesic(diz_coord[partenza], diz_coord[destinazione]).kilometers
    # print(f"Distanza {partenza}-{destinazione}: {distanza:.2f} km")
    return distanza

def calcola_prezzi_carburante():
    import requests
    from bs4 import BeautifulSoup

    # URL dei prezzi medi regionali
    url = "https://www.mimit.gov.it/it/prezzo-medio-carburanti/regioni"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Richiesta HTTP
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Trova tabella con i prezzi
    tabella = soup.find("table")

    # Estrai righe della tabella
    righe = tabella.find_all("tr")

    # print(righe[1:5])

    diz_carburanti = {}

    for elem in righe[1:5]:
        tipo = str(elem.find_all("th")[0])[16:-5]
        valore = float(str(elem.find_all("td")[1])[4:-5])

        diz_carburanti[tipo] = valore

    return diz_carburanti

def calcola_distanza2(city_1, city_2):
    from geopy.distance import geodesic
    from geopy.geocoders import Nominatim

    # Inizializza il geolocalizzatore
    geolocator = Nominatim(user_agent="city_distance_app", timeout=10)

    # Ottieni le coordinate delle citta
    # city_1 = "New York"
    # city_2 = "Bari"
    city1 = geolocator.geocode(city_1)
    city2 = geolocator.geocode(city_2)

    # Estrai le coordinate
    coordinate_1 = (city1.latitude, city1.longitude)
    coordinate_2 = (city2.latitude, city2.longitude)

    # Calcola la distanza
    distance = geodesic(coordinate_1, coordinate_2).kilometers
    # print(f"Distanza tra {city_1} e {city_2}: {distance:.2f} km")
    return distance

