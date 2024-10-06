def albums():
    names = []
    while True:
        name = input("Enter a name (type 'done' to finish): ")
        if name.lower() == 'done':
            break
        names.append(name)

    total = len(names)
    unique_names = list(set(names))
    unique_names.sort()

    return unique_names, total

albums, total = albums()

print("Sorted names without duplicates:", albums)
print("Total number of names entered:", total)
