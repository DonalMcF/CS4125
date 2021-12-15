import load_files
def add_game():
    loop = True
    loop2 = True
    check = False
    check = False
    game_genre = ""
    game_input = input('What game is being added\n')
    for obj in load_files.game_library:
        if obj.name == game_input:
            print("Game has already been added")
            check = True
    if check is False:
        while loop is True:
            admin_input = input('What genre is it?\n1)Childrens\n2)Teens\n')
            if admin_input == "1":
                game_genre = "childrens"
                loop = False
            elif admin_input == "2":
                game_genre = "teens"
                loop = False
            else:
                print("invalid option")
        while loop2 is True:
            game_price = input('What is the games base price\n')
            try:
                check = float(game_price)
                loop2 = False
            except:
                print("input must be a number")
        text_line = "\n" + game_input + ", " + game_genre + ", yes, " + game_price
        out_f = open('gameLibrary.txt', 'a')
        out_f.write(text_line)
        load_files.game_library.append(load_files.game_library_format(game_input,game_genre,"yes",game_price.replace("\n","")))
        print("Game has been created")
        
