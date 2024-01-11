# Suma początkowa
suma_parzyste = 0
suma_nieparzyste = 0
print("Podaj liczby całkowite, które chcesz sprawdzić.Aby zakończyć wprowadzanie liczb wprowadź znak:" + " / \n")
while True:
    number = input("Twoja liczba to: ")
    if number == "/":
        break
    elif number == "":
        break
    else:
        if int(number) % 2 == 0:
            suma_parzyste += int(number)
        else:
            suma_nieparzyste += int(number)

print("Suma liczba parzystych wynosi: ", suma_parzyste)
print("Suma liczba nieparzystych wynosi: ", suma_nieparzyste)
