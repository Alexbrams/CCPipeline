def correctRowCount(rowcount):
    if rowcount >= 900:
        return True
    return False

def correctColumnCount(columncount):
    if columncount == 12:
        return True
    return False

def correctProperties(missing):
    if len(missing) == 0:
        return True
    return False

def failTest(number):
    if number > 2:
        return True
    return False

properties = [
    'Givenname', 
    'Surname', 
    'Streetaddress', 
    'City', 
    'Zipcode', 
    'Country',
    'CountryCode', 
    'NationalId', 
    'TelephoneCountryCode', 
    'Telephone',
    'Birthday', 
    'ConsentToContact'
    ]

# A arrange
# A act - anropar
# A assert - vi verifierar

# med enhetstester vill vi fånmga sk sidoeffekter

# while True:
#     age = int(input("Age"))
#     loc = input("Var är du")
#     c = canIBuyBeer(age,loc)
#     if c == True:
#         print("Yep")
#     else:
#         print("No")
