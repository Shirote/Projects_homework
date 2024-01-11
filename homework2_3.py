number = int(input("Podaj liczbę całkowitą: "))

bin_number = bin(number)[2:]  # Pominięcie prefiksu "0b"
ones = bin_number.count('1')

print("Twoja liczba w systemie binarnym to: " + str(
    bin_number) + " Liczba jedynek w binarnej reprezentacji liczby: " + str(ones))
