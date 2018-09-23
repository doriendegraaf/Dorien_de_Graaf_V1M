def new_password(oldpassword, newpassword):
    cijfer = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'

    getalgevonden = False

    for getal in cijfer:
        if getal in newpassword:
            getalgevonden = True

    if newpassword != oldpassword and len(newpassword) >= 6 and getalgevonden == True:
        return True
    else:
        return False

oud = input('Geef uw oude wachtwoord op: ')
nieuw = input ('Geef uw nieuwe wachtwoord op: ')

uitkomst = new_password(oud , nieuw)

print(uitkomst)
