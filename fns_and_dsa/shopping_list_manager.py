def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))  # Convert input to integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add an item to the shopping list
            item = input("Enter the name of the item to add: ").strip()
            if not item:
                print("Invalid input. Item name cannot be empty.")
            elif item.isdigit():  # Check if the input is purely numeric
                print("Invalid input. Numbers are not allowed as item names.")
            else:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")

        elif choice == 2:
            # Remove an item from the shopping list
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == 3:
            # Display the current shopping list
            if shopping_list:
                print("\nShopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")

        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
