def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword)>= 6:
        return True
    else:
        return False

oud = input('Geef uw oude wachtwoord op: ')
nieuw = input ('Geef uw nieuwe wachtwoord op: ')

uitkomst = new_password(oud , nieuw)

print(uitkomst)
