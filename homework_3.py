# Dla oprocentowania 7%
funds = 30_000
capitalize = funds
percentage = 1.075
print("Symulacja dla oprocentowania 7%:")
print("Środki początkowe:", funds, "Środki po pierwszej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Środki po drugiej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Środki po trzeciej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Finalny zysk:", round(capitalize - funds, 2), "PLN")
print()
# Dla oprocentowania 8%
funds = 30_000
capitalize = funds
percentage = 1.080
print("Symulacja dla oprocentowania 8%:")
print("Środki początkowe:", funds, "Środki po pierwszej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Środki po drugiej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Środki po trzeciej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Finalny zysk:", round(capitalize - funds, 2), "PLN")
print()
# Dla oprocentowania 8.25
funds = 30_000
capitalize = funds
percentage = 1.0825
print("Symulacja dla oprocentowania 8.25%:")
print("Środki początkowe:", funds, "Środki po pierwszej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Środki po drugiej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Środki po trzeciej kapitalizacji:", round(capitalize * percentage, 2))
capitalize *= percentage
print("Finalny zysk:", round(capitalize - funds, 2), "PLN")
