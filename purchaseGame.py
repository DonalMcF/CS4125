import loadFiles
import loadUser
import discountFactory
import calcDiscount

def purchaseMenu(currentUser, userType):
    cart = []
    menu1 = True
    print()
    for obj in loadFiles.gameLibrary:
        print("Name:", obj.name, sep = ' ')
        print("Genre:", obj.genre, sep = ' ')
        print("Price: €", obj.pPrice, sep = '')
        print()
    while menu1 == True:
        userInput = input("what game would you like to add to your account \nsay 'end' when finished\n")
        if userInput == "end" and not cart:
            print("Cart is empty, exiting store")
            menu1 = False
        elif userInput == "end" and cart:
            print("Proceding to checkout")
            checkout(currentUser, userType, cart)
            menu1 = False
        else:
            check = len(cart)
            check2 = False
            check3 = False
            for obj2 in loadUser.userLibrary:
                    if userInput == obj2.name:
                        check2 = True
            if check2 == True:
                print("You already own that game")
            for obj3 in cart:
                if userInput == obj3.name:
                    check3 = True
            if check3 == True:
                print("That game is already in your cart")        
            for obj in loadFiles.gameLibrary:
                if userInput == obj.name and check2 == False and check3 == False:
                    cart.append(obj)
                    print("Game added to cart")
            if check == len(cart) and check2 == False and check3 == False:
                print("Not a valid selection")
        
def checkout(currentUser, userType, cart):
    menu2 = True
    price = 0.0
    print("Current items in cart")
    tempPrice = 0.0
    for obj in cart:
        discountFactory.discountFactory.name = obj.name
        discountFactory.discountFactory.userType = userType
        discountFactory.discountFactory.genre = obj.genre
        discountFactory.discountFactory.newRelease = obj.newRelease
        discountFactory.discountFactory.price = obj.pPrice
        calcDiscount.calcDiscount()
        price = price + float(discountFactory.discountFactory.totalDiscount)
    print ("Total price = €", price, sep = '')
    while menu2 == True:
        userInput = input("Would you like to procede with your purchase?\n")
        if userInput.lower() == "yes" or userInput.lower() == "y":
            print("Please input card details")
            print("Thank you for your purchase")
            loadUser.userLibrary = loadUser.userLibrary + cart
            menu2 = False
        elif userInput.lower() == "no" or userInput.lower() == "n":
            print("cancelling order")
            menu2 = False
        else:
            print("Invalid input")