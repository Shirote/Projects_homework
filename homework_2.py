x = 13 * 1024 * 1024  # Przekształcenie 13TB na MB
y = x / 194  # Ilość plików o rozmiarze 194 MB w 13 TB
b = y * 5  # Oblicz łączny czas pobierania w sekundach
c = b / 3600  # Czas pobierania plików w godzinach
final = round(c)

print("Dane o rozmiarze 13 TB (", x, "MB) zostaną pobrane w ciągu", final, "godzin")
