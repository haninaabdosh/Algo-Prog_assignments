# Grocery List Manager Program
print("Grocery List Manager")

# Creating the grocery list
grocery_list = ["apples", "bananas", "carrots", "milk", "bread", "oranges"]

# Function to display the list
def display_items():
    if not grocery_list:
        print("Your grocery list is empty.")
    else:
        print("Your current grocery list:")
        for item in grocery_list:
            print(item)

# Main loop for selecting options
while True:
    # Displaying options
    print("Choose an option:")
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Exit")
    
    # Taking input from user
    choice = input("Enter your choice (1/2/3/4): ")

    # Option 1: Add an item
    if choice == '1':
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(f"{item} added to the list.")
    
    # Option 2: View the list
    elif choice == '2':  # Check if the user's input is '2'
        display_items()    # If true, the display_items function shows the grocery list
    
    # Option 3: Remove an item
    elif choice == '3':
        if grocery_list:
            display_items()
            item_to_remove = input("Enter the name of the item to remove: ")
            if item_to_remove in grocery_list:
                grocery_list.remove(item_to_remove)
                print(item_to_remove, "removed from the list.")
            else:
                print(item_to_remove, "is not in the list.")
        else:
            print("Your grocery list is empty, nothing to remove.")
    
    # Option 4: Exit the program
    elif choice == '4':
        print("Bye!")
    
    # Invalid choice
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

# code works well, very nice with input validation and error handling, it would be better to add lines or spaces between the menu and items so the user is not confused. also it is better to start with an empty list instead of already filled. overall still good :D
