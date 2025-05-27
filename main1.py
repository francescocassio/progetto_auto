from progetto_auto.gestione_automobili import Automobile, Persona

if __name__ == '__main__':
    a1 = Automobile("FK345LP", "BMW", "X6", "SUV", 5, "Benzina", 12)
    a2 = Automobile("GA325LP", "Fiat", "Punto", "Utilitaria", 5, "GPL", 7)

    p = Persona("mario", "rossi", 45, "M", "Italiana")

    try:
        a1.assegna_proprietario(p)
    except TypeError as t:
        print("hai passato un valore errato come proprietario")

    a1.stampa_dati()

    a1.aggiungi_km(1345)

    a1.stampa_dati()

    a1.aggiungi_km(4000)

    a1.stampa_dati()

    a2.calcola_spesa_viaggio("Bari", "New York")