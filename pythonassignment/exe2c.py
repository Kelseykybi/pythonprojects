def albums():
    names = []
    while True:
        name = input("Enter a name: ")
        if name.lower() == 'done':
            break
        names.append(name)
    
    # Count the total number of names entered (before removing duplicates)
    total = len(names)
    
    # Remove duplicates by converting the list to a set, then back to a list
    allign = list(set(names))
    
    # Sort the list alphabetically
    allign.sort()
    
    return allign, total
# Run the function and get the results
albums, total = albums()

# Display the results
print("Sorted names without duplicates:", albums)
print("Total number of names entered:", total)
