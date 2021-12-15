import load_files

def rent_game(user_rental):
    if not user_rental:
        menu = True
        while menu is True:
            check = False
            for obj in load_files.game_library:
                print("Name:", obj.name, sep = ' ')
                print("Genre:", obj.genre, sep = ' ')
                print()
            user_input = input("what game would you like to rent?\n'exit' to cancel\n")
            if user_input == "exit":
                menu = False
            for obj in load_files.game_library:
                if user_input == obj.name:
                    check = True
            if check is True:
                user_rental = user_input
                print("You have rented" ,user_input, sep = ' ')
                menu = False
            elif check is False and menu is True:
                print("Not a valid Option")
        return user_rental
    else:
        print("Please return rented game before renting another")
        return user_rental

def return_game(user_rental):
    if user_rental:
        print("You have returned your rented game")
        user_rental = ""
        return user_rental
    else:
        print("You do not currently have any games rented")
        return user_rental
