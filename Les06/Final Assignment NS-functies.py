def standaardprijs(afstandkm):
    kosten_per_kilometer = 0.80
    result = 0

    if afstandkm > 50:
        result = 15.00
        result = (50 * kosten_per_kilometer) + result
        afstandkm = afstandkm - 50
        kosten_per_kilometer = 0.60

    elif afstandkm < 0:
        afstandkm = 0

        result = (afstandkm + kosten_per_kilometer)+ result

    return result

def ritprijs(leeftijd, weekendrit, afstand):
    tarief = standaardprijs(afstand)

    if leeftijd < 12 or leeftijd >= 65:
        korting = 30
        if weekendrit:
            korting = 35

    else:
        korting = 0
        if weekendrit:
            korting = 40

    result = (tarief / 100) * (100 - korting)

    return result

leeftijd = int(input('Wat is je leeftijd? '))
weekendrit = input('Is het weekend? J/N ')
afstand = float(input('Hoeveel km was de reis? '))

weekendrit = True if weekendrit == 'J' else False

print('Je betaalt voor deze rit ' + str(ritprijs(leeftijd, weekendrit, afstand)))



