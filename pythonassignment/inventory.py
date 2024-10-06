#python program to create an inventory system
inventory = {}

def add_or_update_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"Updated {item_name}: New Quantity = {inventory[item_name]}")
    else:
        inventory[item_name] = quantity
        print(f"Added {item_name}: Quantity = {quantity}")

def get_item_info(item_name):
    if item_name in inventory:
        print(f"{item_name}: Quantity = {inventory[item_name]}")
    else:
        print(f"{item_name} not found in inventory.")

def total_quantity():
    total = sum(inventory.values())
    print(f"Total quantity of all items: {total}")

def main():
    while True:
        print("\nInventory System")
        print("1. Add/Update Item")
        print("2. Retrieve Item Info")
        print("3. Total Quantity")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_or_update_item(item_name, quantity)
        elif choice == "2":
            item_name = input("Enter item name: ")
            get_item_info(item_name)
        elif choice == "3":
            total_quantity()
        elif choice == "4":
            print("Exiting the inventory system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
