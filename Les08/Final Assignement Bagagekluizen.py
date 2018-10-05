def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()
    aantalkluizen = len(regels)
    aantalvrij = 12 - aantalkluizen
    print(aantalvrij)

def nieuwe_kluis():
    kluisnummers = []
    for i in range(1, 13):
        kluisnummers.append(i)
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()

    for regel in regels:
        kluisinfo = regel.split(';')
        nummer = int(kluisinfo[0])
        kluisnummers.remove(nummer)
    if len(kluisnummers) > 0:
        kluisnummer = kluisnummers[0]
        print('Je kluisnummer is {}'.format(kluisnummer))
        code = input('Wat is je code: ')
        outfile = open('kluizen.txt','a')
        outfile.write('{};{}\n'.format(kluisnummer,code))
        outfile.close()
    else:
        print('Er is geen kluis meer vrij')

def kluis_openen():
    kluisnummer = input('wat is je nummer:')
    kluiscode = input('wat is je code:')
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()
    gegevenscorrect = False

    for regel in regels:
        kluisinfo = regel.split(';')
        nummer = kluisinfo[0]
        code = kluisinfo[1].strip()
        if (kluisnummer == nummer) and (kluiscode == code):
            gegevenscorrect = True
            if gegevenscorrect:
                print('De kluis is open! ')
    if gegevenscorrect is False:
        print('Uw wachtwoord of kluisnummer is niet correct:')




print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil iets uit mijn kluis halen')

keuze = int(input('Geef uw optie:'))

if keuze == 1:
    toon_aantal_kluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
elif keuze == 3:
    kluis_openen()
else:
    print('Keuze niet juist, kies opnieuw.')



