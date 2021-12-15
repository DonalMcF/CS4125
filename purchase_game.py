import load_files
import load_user
import discount_factory
import calc_discount

def purchase_menu(user_type):
    cart = []
    menu1 = True
    print()
    for obj in load_files.game_library:
        print("Name:", obj.name, sep = ' ')
        print("Genre:", obj.genre, sep = ' ')
        print("Price: €", obj.p_price, sep = '')
        print()
    while menu1 is True:
        user_input = input("what game would you like to add to your account \nsay 'end' when finished\n")
        if (user_input == "end") and not cart:
            print("Cart is empty, exiting store")
            menu1 = False
        elif user_input == "end" and cart:
            print("Proceding to checkout")
            checkout(user_type, cart)
            menu1 = False
        else:
            check = len(cart)
            check2 = False
            check3 = False
            for obj2 in load_user.user_library:
                if user_input == obj2.name:
                    check2 = True
            if check2 is True:
                print("You already own that game")
            for obj3 in cart:
                if user_input == obj3.name:
                    check3 = True
            if check3 is True:
                print("That game is already in your cart")
            for obj in load_files.game_library:
                if user_input == obj.name and check2 is False and check3 is False:
                    cart.append(obj)
                    print("Game added to cart")
            if check == len(cart) and check2 is False and check3 is False:
                print("Not a valid selection")
def checkout(user_type, cart):
    menu2 = True
    price = 0.0
    print("Current items in cart")
    for obj in cart:
        discount_factory.discount_factory.name = obj.name
        discount_factory.discount_factory.user_type = user_type
        discount_factory.discount_factory.genre = obj.genre
        discount_factory.discount_factory.load_release = obj.new_release
        discount_factory.discount_factory.price = obj.p_price
        calc_discount.calc_discount()
        price = price + float(discount_factory.discount_factory.total_discount)
    print ("Total price = €", price, sep = '')
    while menu2 is True:
        user_input = input("Would you like to procede with your purchase?\n")
        if user_input.lower() == "yes" or user_input.lower() == "y":
            print("Please input card details")
            print("Thank you for your purchase")
            load_user.user_library = load_user.user_library + cart
            menu2 = False
        elif user_input.lower() == "no" or user_input.lower() == "n":
            print("cancelling order")
            menu2 = False
        else:
            print("Invalid input")
