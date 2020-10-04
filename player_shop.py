# This is the list of items available in the shop.
# Each item is a string, and is broken down into several fields, separated by '/'s.
# The fields are: Item name, price, quantity, and description, respectively.
items = [
    "NAME / COST / AMOUNT / DESCRIPTION",
    "NAME / COST / AMOUNT / DESCRIPTION",
        ]

items = [
    "Hockey Stick / 75.99 / 3 / It's wrapped with way too much hockey tape.",
    "Chewed Gum / 0.01 / 2 / Why would you want this?",
    "Grappling Hook / 49.99 / 1 / Great for turning off lights and saving the day.",
    "Mana Potion / 3.50 / 7 / An excellent choice for any mage.",
    "Apple / 1 / 12 / It keeps the doctors away!",
    "Unholy Water / 6 / 6 / The water is pure black. You're actually not sure if it is water."
]

# items = [
#     ["Hockey Stick", 75.99, 3, "It's wrapped with way too much hockey tape."],
#     ["Chewed Gum", 0.01, 2, "Why would you want this?"],
#     ["Grappling Hook", 49.99, 1, "Great for turning off lights and saving the day."],
#     ["Mana Potion", 3.50, 7, "An excellent choice for any mage."],
#     ["Apple", 1, 12, "It keeps the doctors away!"],
#     ["Unholy Water", 6, 6, "The water is pure black. You're actually not sure if it is water."],
# ]

# In an ideal game the player has a budget!
player_money = 200.00


def format_fields(item):
    # First objective is to nicely break up the item strings
    # Name/Cost/Quantity/Description -> Name, Cost, Quantity, Description

    # Note how string.strip() works here:
    # Example: print("   <-Here, but not inside this->   ".strip())
    # The above prints '<-Here, but not inside this->'
    # So string.strip() should only be used AFTER the string is split up at the `/`s

    # itemNoSpaces = item.replace(" ", "")
    # The above works, but removes ALL spaces, including the space between-
    # some of the item names Example: Hockey Stick -> HockeyStick
    # print(itemNoSpaces)  # Debug

    # Splits up the item string into a list with the different fields
    # ['Name ',' Cost ',' Quantity ',' Description']
    item_field_list = item.split("/")

    # Remove the excess spaces from the fields
    for i in range(0, len(item_field_list)):
        item_field_list[i] = item_field_list[i].strip()

    return item_field_list


# Returns an updated string after a change was made to one of the fields
def set_field(formatted_list, change_index, change):
    # Changes a field in `item_list` at position `change_index` with `change`
    formatted_list[change_index] = change

    # Concatenate everything in the formatted_list back into a string with the `/` included
    return "{0} / {1} / {2} / {3}".format(formatted_list[0], formatted_list[1], formatted_list[2], formatted_list[3])


def print_menu():
    # This print statement is just an optional design choice.
    # It might require some experimentation to line everything up properly. (My solution was kinda hacky)
    print()
    print("| {0:^23} | {1:^9} | {2:^6} |".format("Name", "Price", "Amount"))
    print("|" + "-" * 25 + "|" + "-" * 11 + "|" + "-" * 8 + "|")

    # Loops through the items list, ultimately printing out a menu interface for the player.
    # As it goes through the list, it also 'enumerates',
    # -which basically counts through the items in the list, increasing-
    # -the itemNumber variable as it moves to the next item in the list.
    for item_number, item in enumerate(items):
        formatted_list = format_fields(item)

        # Nicely prints the menu, spacing out different fields
        print("| {0}: {1:<20} | ${2:<8} | x{3:<5} |"
              .format(item_number + 1, formatted_list[0], formatted_list[1], formatted_list[2]))
    print()
    print("Select an item to purchase by typing its number.")
    print("You have ${} available to spend.".format(player_money))
    print("Type 0 to leave the shop.")


# This is just a series of print statements to inspire some creativity and set up the context of the shop.
print("\nYou stumble upon a small shop made out of a tree stump in the woods.")
print("A bell jingles as you open the door and step inside.")
print("You find a small frog with a fancy purple hat sitting behind the counter of the shop.")
print("You greet him, but he says nothing. He is a frog.")
print("There is a large selection of items spread across the counter in front of the frog.")
print("You take a look around...")

# Printing the menu each time versus printing it once is a design choice.
# Include it in the while True loop in the get_input() function
# if you want it printed each time the input is wrong
print_menu()

# # Sets up a variable to interact with player input
# player_input = "-"
while True:
    # Get the written input of the player
    player_input = input("Your Selection: ")

    # If the input is NOT numerical
    # OR
    # the number is not within the range of the items
    # then go back to the beginning
    if not player_input.isnumeric() or len(items) < int(player_input):
        print("\tThat is not a valid number.")
        continue

    # Player input should be a string, so make sure to wrap that to an int to check
    # Could also `if player_input == "0"`
    if int(player_input) == 0:
        print("\nYou leave the shop with ${} left in your pocket.".format(player_money))
        print("You hear the bell again on your way out.")
        break

    # Find the item the user is looking for
    else:
        # Don't forget to -1 to get the right index position!
        item_list = format_fields(items[int(player_input) - 1])
        print("\nYou select the {0}. {1}".format(item_list[0], item_list[3]))
        print("How many would you like to buy? (Type 0 to browse the other items) ")
        while True:
            amount_to_buy = input("Amount: ")
            # We need to check for several conditions.
            # 1. The input is numeric (and an integer)
            # 2. There is enough of the item in stock
            # 3. We are buying at least 1 or more
            # 4. We can afford it
            if amount_to_buy.isnumeric() and int(amount_to_buy) >= 0:  # 1. and 3.

                if int(amount_to_buy) == 0:
                    print_menu()
                    break
                elif int(amount_to_buy) > int(item_list[2]):  # 2.
                    print("\tThere is not enough of this item in stock!")
                elif int(amount_to_buy) * float(item_list[1]) > player_money:  # 4.
                    print("\tYou do not have enough money!")
                else:
                    cost = int(amount_to_buy) * float(item_list[1])
                    print(
                        "Buying {0} of these will cost ${1}.".format(amount_to_buy, cost))
                    confirmation = input("Type 0 to confirm or anything else to change the amount: ")
                    # The way the input is formatted doesn't really matter.
                    # There are tons of options for how to do this. (Instead of 0 for example)
                    if confirmation.isnumeric() and int(confirmation) == 0:
                        # When buying something, we need to do two things:
                        # 1. Subtract the cost of the purchase from `player_money`
                        # 2. Change the amount the shop has in stock to reflect the purchase

                        player_money -= int(amount_to_buy) * float(item_list[1])  # 1.
                        print("You now have ${} remaining.".format(player_money))

                        # We're updating the player's selected item with the stock after the purchase
                        items[int(player_input) - 1] = set_field(item_list, 2,
                                                                 int(item_list[2]) - int(amount_to_buy))  # 2.

                        print_menu()
                        break
                    else:
                        continue
            else:
                print("\tYou must enter a valid number!")
