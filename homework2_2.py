import random

numbers = []

min_value = int(input("Minimalna losowana wartość: "))
max_value = int(input("Maksymalna losowana wartość: "))
elements = int(input("Podaj ilość liczb do wylosowania z podanego zakresu: "))
series = int(input("Podaj ilość serii liczb do wylosowania z podanego zakresu: "))

for i in range(1, series + 1):
    series = []
    numbers.append(series)
    for j in range(elements):
        number = random.randint(min_value, max_value)
        series.append(number)
    print(i, " seria liczb: ", series)
