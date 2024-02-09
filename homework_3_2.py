def cans_for_level(level):
    if level <= 0:
        return "Błąd: Poziom wieży musi być liczbą dodatnią."
    elif level == 1:
        return 1
    else:
        return level + cans_for_level(level - 1)


def levels(cans, level=1):
    if cans < 0:
        return "Błąd: Ilość puszek nie może być ujemna."
    elif cans < level:
        return level - 1
    else:
        return levels(cans - level, level + 1)


if __name__ == "__main__":
    try:
        cans_input = int(input("Podaj ilość dostępnych puszek: "))
        if cans_input < 0:
            raise ValueError("Błąd: Podana ilość puszek nie może być ujemna.")

        levels_possible = levels(cans_input)
        print(f"Z podanej ilości puszek można zbudować maksymalnie {levels_possible} poziomową wieżę.")

        cans_needed = cans_for_level(levels_possible)
        print(f"Aby zbudować {levels_possible} poziomową wieżę potrzeba {cans_needed} puszek.")
    except ValueError as ve:
        print("Podano niepoprawną wartość!")
