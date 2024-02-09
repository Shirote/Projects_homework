def no_duplicates(source):
    target = []
    for element in source:
        if element not in target:
            target.append(element)
    return tuple(target)


# Test
print(remove_duplicates([1, 3, 2, 4, 5, 7, 7, 5, 2, 9, 8, 14]))
print(remove_duplicates(["lew", "suseł", "kaczka", "wiewiórka", "szop", "kot", "kaczka", "szop", "kaczka", "szop"]))
