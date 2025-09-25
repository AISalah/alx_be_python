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
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input("Enter the item to add: "))
            print("Item added.")
        elif choice == '2':
            item = input("Enter the item to remove: ")
            
            if item in shopping_list:
                shopping_list.remove(item)
                print("Item removed.")
            else:
                print("Item not found in the list.")
        elif choice == '3':
            shopping_list.sort()
            print(f"Shopping List contains: {shopping_list}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()