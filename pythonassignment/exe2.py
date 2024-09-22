def albums():
    names = []
    while True:
        name = input("Enter a name")
        if name.lower() == 'done':
            break
        names.append(name)
    return names

# Run the function and print the names
albums = albums()
print("Names you entered:", albums)