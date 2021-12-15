import discount_factory
def calc_discount():
    temp_name = discount_factory.discount_factory.name
    temp_user_type = discount_factory.discount_factory.user_type
    user_genre = discount_factory.discount_factory.genre
    temp_new_release = discount_factory.discount_factory.new_release
    temp_price = float(discount_factory.discount_factory.price)
    temp_discount = 0.0
    if(temp_user_type == "member" or temp_user_type == "admin") and not temp_new_release == "yes" and user_genre == "teens":
        print("Applying member discount of 25% for teens game")
        temp_discount = temp_price * 0.75
    elif(temp_user_type == "member" or temp_user_type == "admin") and not temp_new_release == "yes" and user_genre == "childrens":
        print("Applying member discount of 35% for childrens game")
        temp_discount = temp_price * 0.65
    elif(temp_user_type == "member" or temp_user_type == "admin") and temp_new_release == "yes" and user_genre == "teens":
        print("Applying member discount of 15% for new teens game")
        temp_discount = temp_price * 0.85
    elif(temp_user_type == "member" or temp_user_type == "admin") and temp_new_release == "yes" and user_genre == "childrens":
        print("Applying member discount of 25% for new childrens")
        temp_discount = temp_price * 0.75
    if temp_discount == temp_price:
        print(temp_name, ", €", temp_price, sep = '')
        
    else:
        print(temp_name, ", Original price €", temp_price, ", Discounted Price €", temp_discount, sep = '')
    discount_factory.discount_factory.total_discount = temp_discount
