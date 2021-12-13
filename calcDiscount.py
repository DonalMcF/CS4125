import discountFactory
def calcDiscount():
    tempName = discountFactory.discountFactory.name
    tempUserType = discountFactory.discountFactory.userType
    tempGenre = discountFactory.discountFactory.genre
    tempNewRelease = discountFactory.discountFactory.newRelease
    tempPrice = float(discountFactory.discountFactory.price)
    tempDiscount = 0.0
    if(tempUserType == "member" or tempUserType == "admin") and not tempNewRelease == "yes" and tempGenre == "teens":
        print("Applying member discount of 25% for teens game")
        tempDiscount = tempPrice * 0.75
    elif(tempUserType == "member" or tempUserType == "admin") and not tempNewRelease == "yes" and tempGenre == "childrens":
        print("Applying member discount of 35% for childrens game")
        tempDiscount = tempPrice * 0.65
    elif(tempUserType == "member" or tempUserType == "admin") and tempNewRelease == "yes" and tempGenre == "teens":
        print("Applying member discount of 15% for new teens game")
        tempDiscount = tempPrice * 0.85
    elif(tempUserType == "member" or tempUserType == "admin") and tempNewRelease == "yes" and tempGenre == "childrens":
        print("Applying member discount of 25% for new childrens")
        tempDiscount = tempPrice * 0.75
    if tempDiscount == tempPrice:
        print(tempName, ", €", tempPrice, sep = '')
        
    else:
        print(tempName, ", Original price €", tempPrice, ", Discounted Price €", tempDiscount, sep = '')
    discountFactory.discountFactory.totalDiscount = tempDiscount