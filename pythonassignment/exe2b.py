def albums():
    names = []
    while True:
        name = input("Enter a name")
        if name.lower() == 'done':
            break
        names.append(name)
    
    # Remove duplicates by converting the list to a set, then back to a list
    unique_names = list(set(names))
    
    # Sort the list alphabetically
    unique_names.sort()
    
    return unique_names

# Run the function and print the sorted names
albums = albums()
print("Sorted names without duplicates:", albums)