# Taking input for name
name = input("Enter name: ")

# Printing menu options
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Taking input for menu choice
choice = input(">>> ")

# Loop until choice not equals 'Q'
while choice != 'Q':

    # If choice is 'H' then printing "Hello" name
    if choice == 'H':
        print("Hello", name)

    # If choice is 'G' then printing "Goodbye" name
    elif choice == 'G':
        print("Goodbye", name)

    # If above two conditions are False then printing "Invalid choice"
    else:
        print("Invalid choice")

    # Printing menu options
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Taking input for menu choice
    choice = input(">>> ")

# Printing "Finished." message
print("Finished.")