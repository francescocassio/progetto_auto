class Persona:
    def __init__(self, nome, cognome, eta, sesso, nazione):
        self.nome = nome.capitalize()
        self.cognome = cognome.capitalize()
        self.eta = eta

        if sesso.upper() in ["M", "F"]:
            self.sesso = sesso.upper()
        else:
            self.sesso = "ND"
        self.nazione = nazione

    def stampaDati(self):
        print("Nome:", self.nome)
        print("Cognome:", self.cognome)
        print("Eta:", self.eta)
        print("Nazione:", self.nazione)
        print("---------------------")

    def calcola_data_nascita(self):
        from datetime import datetime
        data_odierna = datetime.today()
        anno_odierno = data_odierna.year

        anno_nascita = anno_odierno - self.eta

        return anno_nascita

    def is_maggiorenne(self):
        if self.eta >= 18:
            return True
        else:
            return False

    def inserisci_nel_db(self, nome_db, nome_tabella):
        import mysql.connector

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= nome_db
        )

        cursor = conn.cursor()

        sql = f"INSERT INTO {nome_tabella} (nome, cognome, eta, sesso, nazione) VALUES (%s, %s,%s, %s,%s)"
        valori = (self.nome, self.cognome, self.eta, self.sesso, self.nazione)

        cursor.execute(sql, valori)
        conn.commit()

        print(f"{cursor.rowcount} record inserito nella tabella {nome_tabella} del database {nome_db}.")

        cursor.close()
        conn.close()

class Automobile:
    def __init__(self, targa, marchio, modello, tipo_veicolo, capienza, carburante, consumo):
        self.targa = targa
        self.marchio = marchio
        self.modello = modello
        self.tipo_veicolo = tipo_veicolo
        self.capienza = capienza
        self.carburante = carburante
        self.proprietario = None
        self.km_percorsi = 0
        self.consumo_ogni_100km = consumo

    def assegna_proprietario(self, propr):
        if not isinstance(propr, Persona):
            raise TypeError("Il proprietario deve essere un'istanza della classe Persona")
        self.proprietario = propr

    def stampa_dati(self):
        print("Modello:", self.modello)
        print("Marchio:", self.marchio)
        print("KM percorsi:", self.km_percorsi)
        print("Targa:", self.targa)

        if self.proprietario is not None:
            print("Proprietario:")
            self.proprietario.stampaDati()
        else:
            print("Nessun proprietario")

    def consumo_al_km(self):
        return self.consumo_ogni_100km / 100

    def aggiungi_km(self, km_p):
        self.km_percorsi += km_p

    def calcola_spesa_viaggio(self, partenza, arrivo):
        from supporto_mappe import calcola_distanza, calcola_prezzi_carburante, calcola_distanza2
        km_calcolati = calcola_distanza2(partenza.lower(), arrivo.lower())

        spesa_carburante = calcola_prezzi_carburante()[self.carburante]

        spesa_totale = (km_calcolati * self.consumo_al_km()) * spesa_carburante

        print(f"Per questo viaggio da {partenza} ad {arrivo} consumerai {spesa_totale:.2f}€")


class Garage:
    def __init__(self, nome, citta, capienza):
        self.nome = nome
        self.citta = citta
        self.capienza = capienza
        self.auto_parcheggiate = []
        self.incassi = {}


    def si_puo_parcheggiare(self):
        if len(self.auto_parcheggiate) < self.capienza:
            return True
        else:
            return False

    def posti_disponibili(self):
        return self.capienza - len(self.auto_parcheggiate)

    def aggiungi_auto(self, autom, data = None):

        if data is None:
            from datetime import datetime
            oggi = datetime.now()

            anno = str(oggi.year)
            mese = str(oggi.month)
            giorno = str(oggi.day)
            giorno_attuale = f"{giorno}-{mese}-{anno}"
        else:
            giorno_attuale = data

        costo = 11.99
        if not isinstance(autom, Automobile):
            raise TypeError("Puoi aggiungere solo automobili")

        if self.si_puo_parcheggiare():
            self.auto_parcheggiate.append(autom)
            print(f"Auto con targa {autom.targa} aggiunta al garage")

            if giorno_attuale not in self.incassi:
                self.incassi[giorno_attuale] = costo
            else:
                self.incassi[giorno_attuale] += costo
        else:
            print("Il parcheggio è pieno!")

    def stampa_dati(self):
        print("Parcheggio", self.nome)
        print("Capienza:", self.capienza)
        print("Posti disponibili:", self.posti_disponibili())

        print("Auto parcheggiate: ")

        for auto in self.auto_parcheggiate:
            auto.stampa_dati()

        print("Incassi:")
        print(self.incassi)




        # possibili implementazioni nella classe Garage

        # rimuovere un'auto
        # creare un menù da riga di comando per: creare auto, creare persone, assegnare proprietari, aggiungere auto nel garage
        # calcolare media dei km percorsi nelle auto parcheggiate -> calcola_km_medi()
        # contare quante auto sono a gpl, benzina, gasolio, metano
        # contare quante auto hanno targa italiana -> sfruttare una regex per capirlo
        # calcolare incassi giornalieri
        #








