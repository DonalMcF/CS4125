user_library = []
class user_library_format:
    def __init__(self, name, genre, new_release, p_price):
        self.name = name
        self.genre = genre
        self.new_release = new_release
        self.p_price = p_price

def load_user(current_user):
    try:
        file_name = current_user + "Library.txt"
        with open(file_name,'r') as fi_o:
            text_lines = fi_o.read_lines()
            for i in text_lines:
                line = i.split(", ")
                user_library.append(user_library_format(line[0],line[1],line[2],line[3].replace("\n","")))
            fi_o.close()
    except:
        file_name = current_user + "Library.txt"
        out_f = open(file_name, 'w')
        out_f.close()
    try:
        file_name = current_user + "Rental.txt"
        with open(file_name,'r') as fi_o:
            text_lines = fi_o.read_lines()
            user_rental = text_lines[0].replace("\n","")
            return user_rental
    except:
        file_name = current_user + "Rental.txt"
        out_f = open(file_name, 'w')
        out_f.close()
def update_user(current_user):
    file_name = current_user + "Library.txt"
    out_f = open(file_name, 'w')
    i = 0
    for obj in user_library:
        i = i + 1
        if i == len(user_library):
            new_line = obj.name + ", " + obj.genre + ", " + obj.new_release + ", " + obj.p_price
            out_f.write(new_line)
        else:
            new_line = new_line = obj.name + ", "
            + obj.genre + ", " + obj.new_release + ", " + obj.p_price + "\n"
            out_f.write(new_line)

def update_user_rent(current_user, user_rental):
    file_name = current_user + "Rental.txt"
    out_f = open(file_name, 'w')
    out_f.write(user_rental)
    out_f.close()
    
