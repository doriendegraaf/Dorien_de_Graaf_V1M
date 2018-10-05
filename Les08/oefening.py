kluizenbestand = open('Geregistreerde kluizen.txt', 'r')
bestand = kluizenbestand.read().splitlines()
kluizenbestand.close

    #Geeft weer hoeveel kluizen er nog beschikbaar zijn
def toon_aantal_kluizen_vrij():
    totaalaantalkluizen = 12
    res = totaalaantalkluizen - (len(bestand))
    return res

    #Kluis geristreren
def nieuwe_kluis():
    maximaalkluizen = 12
    vrijekluizenlijst = list(range(1, maximaalkluizen + 1))
    if toon_aantal_kluizen_vrij() <= 0:
        print("Er zijn geen kluizen vrij.")

    if toon_aantal_kluizen_vrij() > 0:
        for kluis in bestand:
            vrijekluizenlijst.remove(int(kluis.split(';')[0]));
        nieuwe_kluis = vrijekluizenlijst[0]
        print("U heeft kluisnummer " + str(nieuwe_kluis))
        wachtwoord = input("Kies een wachtwoord: ")
        bestand.append(str(nieuwe_kluis) + ';' + str(wachtwoord))
        print('De kluis is geregistreerd!')
        save(bestand)

    #Haalt de kluis op
def magkluisopen(kluisnummer, wachtwoord, kluis):
        return (str(kluisnummer) + ";" + str(wachtwoord) == kluis

def kluisopenen():
    kluisnummer = input("Uw kluisnummer: ")
    wachtwoord = input("Wachtwoord: ")
    gevonden = false:
    for kluis in bestand:
        gevonden =  gevonden or magkluisopen(kluisnummer, wachtwoord, kluis)

    if gevonden:
        print("Uw kluis is nu open!")
    else:
        print("Uw wachtwoord of kluisnummer is niet juist.")


    #Levert de kluis in zodat iemand anders deze kan registreren
def kluis_teruggeven():
    kluisnummer = input("Uw kluisnummer: ")
    wachtwoord = input("Wachtwoord: ")
    for kluis in bestand:
        if magkluisopen(kluisnummer, wachtwoord, kluis):
            bestand.remove(kluis)
            save(bestand)
            print('Uw kluis is open en wordt vrijgegeven')
            return

    print("Uw wachtwoord of kluisnummer is niet juist.")

#Bestand overschrijven
def save(bestand):
    kluizenBestand = open("Geregistreerde kluizen.txt","w")
    for line in bestand:
        kluizenBestand.write(line)
        kluizenBestand.write('\n')

    kluizenBestand.close()

def display_menu():
    while True:
        print('\n'
            'Kies een van de volgende opties:\n'
            '1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
            '2: Ik wil een nieuwe kluis\n'
            '3: Ik wil iets uit mijn kluis halen\n'
            '4: Ik geef mijn kluis terug\n'
            '\n')
        keuze = input('Geef uw optie:')

        if keuze == '1':
            print('Aantal kluizen vrij:' + ' ' + str(toon_aantal_kluizen_vrij()))
        elif keuze == '2':
            nieuwe_kluis()
        elif keuze == '3':
            kluis_openen()
        elif keuze == '4':
            kluis_teruggeven()
        else:
            print('Maak een geldige keuze.')