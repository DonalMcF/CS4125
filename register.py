import load_files
def register():
    loop = True
    check = False
    while loop is True:
        check = False
        username_input = input('Choose a username\n')
        for obj in load_files.accounts:
            if obj.name == username_input:
                print("Username has been taken, please select another")
                check = True
        if check is False:
            loop = False
    password_input = input('Choose a password\n')
    text_line = "\n" + username_input + ", " + password_input + ", user"
    out_f = open('accounts.txt', 'a')
    out_f.write(text_line)
    load_files.accounts.append(load_files.accounts_format(username_input,password_input,"user"))
    print("Account has been created")
