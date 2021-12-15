import load_files 
import load_user
import log_in
import register
import purchase_game
import rent_game
import add_game

user_type = ""
user_rental = ""

print("New releases this week")
for obj in load_files.game_library:
    if obj.new_release == "yes":
        print(obj.name)
print("\n")

menu1 = True
while menu1 == True:
    user_input = input("What would you like to do? \n1) Register an account\n2) Log in\n3) Exit\n")
    if user_input == "1":
        register.register()
    elif user_input == "2":
        current_user, current_password = log_in.log_in()
        if current_user:
            print("Welcome,", current_user, sep = ' ')
            for obj in load_files.accounts:
                if current_user == obj.name:
                    user_type = obj.account_type
                    user_rental = load_user.load_user(current_user)
                    menu2 = True 
                    while menu2 == True:
                        if user_type == "user":
                            user_input = input("What would you like to do? \n1) Purchase game\n2) Subscribe to membership\n3) Log out\n")
                        elif user_type == "member":
                            user_input = input("What would you like to do? \n1) Purchase game\n2) Cancel membership\n3) Rent Game\n4) Return Game\n5) Log out\n")
                        elif user_type == "admin":
                            user_input = input("What would you like to do? \n1) Purchase game\n2) Add game\n3) Log out\n")
                  
                        #user commands
                        if user_input == "1":
                            purchase_game.purchase_menu(user_type)
                            load_user.update_user(current_user)
                        elif user_input == "2" and (user_type == "user" or user_type == "member"):
                            user_type = load_files.update_membership(current_user, user_type)
                        elif user_input == "3" and user_type == "user":
                            print("Goodbye", current_user, sep = ' ')
                            menu2 = False
                      
                        #member commands
                        elif user_input == "3" and user_type == "member":
                            user_rental = rent_game.rent_game(user_rental)
                            load_user.update_user_rent(current_user, user_rental)
                        elif user_input == "4" and user_type == "member":
                            user_rental = rent_game.return_game(user_rental)
                            load_user.update_user_rent(current_user, user_rental)
                        elif user_input == "5" and user_type == "member":
                            print("Goodbye", current_user, sep = ' ')
                            menu2 = False
                                    
                        #admin commands
                        elif user_input == "2" and user_type == "admin":
                            add_game.add_game()
                        elif user_input == "3" and user_type == "admin":
                            print("Goodbye", current_user, sep = ' ')
                            current_user = ""
                            current_password = ""
                            user_type = ""
                            user_rental = ""
                            load_user.user_library.clear()
                            menu2 = False
                                    
                        else:
                            print("invalid input, please select the number of the action you wish to take")

    elif user_input == "3":
        menu1 = False
    else:
        print("invalid input, please select the number of the action you wish to take")
