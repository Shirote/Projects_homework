# Dla oprocentowania 7%
funds = 30_000
percentage = 7.5
capitalize = round(percentage/4,2) #kapitalizacja 4 razy w roku
print("Symulacja dla oprocentowania 7,5%:")
print("Oprocentowanie kwartalne:", capitalize,"%.")
print("Środki początkowe:", funds)
print("Saldo po pierwszej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po drugiej kapitalizacji:", round(funds * (1 + capitalize/ 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po trzeciej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po czwartej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
profit_1year = funds - 30_000
print("Finalny zysk:", round(profit_1year, 2), "PLN")
print("Finalny saldo:", round(profit_1year+30_000, 2), "PLN")
print()
# Dla oprocentowania 8%
funds = 30_000
percentage = 8.0
capitalize = round(percentage/4,2)
print("Symulacja dla oprocentowania 8%:")
print("Oprocentowanie kwartalne:", capitalize,"%.")
print("Środki początkowe:", funds)
print("Saldo po pierwszej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po drugiej kapitalizacji:", round(funds * (1 + capitalize/ 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po trzeciej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po czwartej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
profit_1year = funds - 30_000
print("Finalny zysk:", round(profit_1year, 2), "PLN")
print("Finalny saldo:", round(profit_1year+30_000, 2), "PLN")
print()
# Dla oprocentowania 8.25
funds = 30_000
percentage = 8.25
capitalize = round(percentage/4,2)
print("Symulacja dla oprocentowania 8.25%:")
print("Oprocentowanie kwartalne:", capitalize,"%.")
print("Środki początkowe:", funds)
print("Saldo po pierwszej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po drugiej kapitalizacji:", round(funds * (1 + capitalize/ 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po trzeciej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
print("Saldo po czwartej kapitalizacji:", round(funds * (1 + capitalize / 100), 2))
funds *= (1 + capitalize / 100)
profit_1year = funds - 30_000
print("Finalny zysk:", round(profit_1year, 2), "PLN")
print("Finalny saldo:", round(profit_1year+30_000, 2), "PLN")