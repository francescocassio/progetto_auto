from progetto_auto.gestione_automobili import Automobile, Persona, Garage

if __name__ == '__main__':
    a1 = Automobile("FK345LP", "BMW", "X6", "SUV", 5, "Benzina", 12)
    a2 = Automobile("GA325LP", "Fiat", "Punto", "Utilitaria", 5, "GPL", 7)

    p = Persona("mario", "rossi", 45, "M", "Italiana")

    a1.assegna_proprietario(p)

    #creaiamo il garage
    mioGarage = Garage("Parcheggio CLAITA", "Roma", 200)

    mioGarage.aggiungi_auto(a1)
    mioGarage.aggiungi_auto(a2)

    mioGarage.stampa_dati()
