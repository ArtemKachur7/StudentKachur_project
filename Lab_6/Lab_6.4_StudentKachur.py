def liters_100km_to_miles_gallon(liters): #Функція , яка конвертує витрату палива з літрів на 100 км в милі на галон
    km_in_miles = 100/1.609344
    miles_per_gallon = km_in_miles / (liters / 3.785411784)
    return miles_per_gallon
def miles_gallon_to_liters_100km(miles): #Функція , яка конвертує витрату палива з миль на галон у літри на 100 км
    liters_in_milles = 1.609344/3.785411784
    liters_per_100km = 100 / (miles * liters_in_milles)
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))