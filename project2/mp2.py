from datetime import datetime

users={"john":"git123" , "alex":"4444"}

logged_user_basket = dict()

johnsBasket = dict()
alexsBasket = dict()

basket_sub_menu={1:"Update amount", 2:"Remove an item", 3:"Check out", 4:"Go back to main menu"}

inventory={'asparagus':[10,5],'broccoli':[15,6],'carrots':[18,7],
           'apples':[20,5],'banana':[10,8],'berries':[30,3], 'eggs':[50,2],'mixed fruit juice':[0,8],
           'fish sticks':[25,12], 'ice cream':[32,6], 'apple juice':[40,7], 'orange juice':[30,8],
           'grape juice':[10,9]}



compare_inventory={'asparagus':[10,5],'broccoli':[15,6],'carrots':[18,7],
           'apples':[20,5],'banana':[10,8],'berries':[30,3], 'eggs':[50,2],'mixed fruit juice':[0,8],
           'fish sticks':[25,12], 'ice cream':[32,6], 'apple juice':[40,7], 'orange juice':[30,8],
           'grape juice':[10,9]}


def online_commerce():
    print("****Welcome to Git Online Market****")
    print("Please log in by providing your user credentials:")

    logged_user = input("Username: ")
    logged_password = input("Password: ")

    while logged_user not in users.keys() or logged_password != users[logged_user]:
        print("Your user name and/or password is not correct. Please try again!")
        logged_user = input("Username: ")
        logged_password = input("Password: ")

    print("Successfully logged in!")
    print("Welcome, {}! Please choose one of the following options by entering the corresponding menu number.".format(
        logged_user))

    if logged_user=="john":
        logged_user_basket = johnsBasket

    else:
        logged_user_basket = alexsBasket

    return main_menu(logged_user, logged_user_basket)


def main_menu(current_user, logged_user_basket):

    menu = [("Search for a product", 1), ("See Basket", 2), ("Check Out", 3), ("Logout", 4), ("Exit", 5)]
    for word, number in menu:
        print(str(number), ".", str(word))

    choice = int(input("Your choice: "))
    while choice>5 or choice<=0:
        print("Invalid menu number!")
        choice = int(input("Your choice: "))

    return menus(current_user, choice, logged_user_basket)


def menus(current_user, choice, logged_user_basket):
    if choice == 1:
        search_term = input("What are you searching for? Enter 0 for main menu.").lower()
        if search_term == str(0):
            main_menu(current_user, logged_user_basket)

        tuple_inventory = inventory.items()
        itemCount = 0
        itemList = []
        num = 1

        for key, number in tuple_inventory:
            if search_term in key and number[0]>0:
                itemCount += 1
                itemList.append(key)

        print("{} similar items found.".format(itemCount))

        if itemCount == 0:
            print("No item found! Please search for another term.")
            main_menu(current_user, logged_user_basket)

        for itm in itemList:
            print(str(num), ".", str(itm), " ", inventory[itm][1], "$")
            num+=1

        choice1 = int(input("Please select the item number to add the item to your basket (Enter 0 for main menu):"))
        if choice1 == 0:
            main_menu(current_user, logged_user_basket)

        while choice1 not in range(itemCount+1):
            print("Invalid item number!")
            choice1 = int(input("Please select the item number to add the item to your basket (Enter 0 for main menu):"))
            if choice1 == 0:
                main_menu(current_user, logged_user_basket)

        print("Adding ", itemList[choice1-1], " to the basket!")

        amount = int(input("Please enter the amount of the product: "))

        product = itemList[choice1-1]

        while amount > inventory[product][0]:
            print("Sorry! The amount exceeds the limit, Please try again with smaller amount!(Enter 0 for main menu)")
            amount = int(input("Please enter the amount of the product: "))
            if amount == str(0):
                main_menu(current_user, logged_user_basket)

        if current_user not in logged_user_basket:
            logged_user_basket[current_user] = {}

        if product in logged_user_basket[current_user].keys():
            logged_user_basket[current_user][product] += amount
            inventory[product][0] -= amount
            main_menu(current_user, logged_user_basket)
        else:
            logged_user_basket[current_user][product] = amount
            inventory[product][0] -= amount
            main_menu(current_user, logged_user_basket)


    elif choice == 2:
        basket(current_user, logged_user_basket)

    elif choice==3:
        print("Redirecting checkout...")
        checkout(current_user, logged_user_basket)

    elif choice ==4:
        print("Logging out...")
        if current_user == "john":
            johnsBasket = logged_user_basket
        else:
            alexsBasket = logged_user_basket

        online_commerce()
    elif choice==5:
        exit()


def checkout(current_user, logged_user_basket):
    print("Processing your receipt...\n******* Git Online Market ********\n************************************\n"
          "www.github.com\n------------------------------------")

    basket_contents(current_user, logged_user_basket)

    print("------------------------------------")
    print(datetime.today())
    print("------------------------------------")
    print("Thank You for using Git Market!")
    main_menu(current_user, logged_user_basket)


def basket_contents(current_user, logged_user_basket):
    if len(logged_user_basket) == 0:
        print("Your basket is empty! \n Total amount is: 0$")
        basket_sub(current_user, logged_user_basket)
    num = 1
    total = 0
    new = {}

    for i in logged_user_basket.values():
        new = i

    for key, value in new.items():
        print(str(num), ".", key, "price=", inventory[key][1], "$", "amount=", value, "total=", value*inventory[key][1])
        total += int(value*inventory[key][1])
        num+=1

    print("Total amount: ", str(total), "$")
    return new


def basket(current_user, logged_user_basket):
    basket_contents(current_user, logged_user_basket)
    basket_sub(current_user, logged_user_basket)


def basket_sub(current_user, logged_user_basket):
    sub_menu =[("Update amount", 1), ("Remove an item", 2), ("Check Out", 3), ("Go back to main menu", 4)]
    for word, number in sub_menu:
        print(str(number), ".", str(word))

    option = int(input("Please choose an option: "))
    while option>4 or option<=0:
        print("Please provide a valid option!")
        option = int(input("Please choose an option: "))

    if option==1:
        new = basket_contents(current_user, logged_user_basket)
        updateItem = input("Please select the item you want to update the amount: (Enter 0 for basket menu)")
        if updateItem == str(0):
            basket_sub(current_user, logged_user_basket)

        while updateItem not in new.keys():
            print("No such item in your basket!")
            updateItem = input("Please type the name of the item you want to update the amount: ")

        updateAmount = int(input("Please enter new amount: "))
        while updateAmount<=0 or updateAmount >compare_inventory[updateItem][0] + 1:
            print("Invalid amount to update!")
            updateAmount = int(input("Please enter new amount: "))

        inventory[updateItem][0] += new[updateItem]
        new[updateItem] = updateAmount
        inventory[updateItem][0] -= updateAmount
        basket_contents(current_user, logged_user_basket)
        basket_sub(current_user, logged_user_basket)

    elif option==2:
        new = basket_contents(current_user, logged_user_basket)
        removeItem = input("Please select the item to be removed: (Enter 0 for basket menu)")
        if removeItem==str(0):
            basket_sub(current_user, logged_user_basket)

        while removeItem not in new.keys():
            print("No such item in your basket!")
            removeItem = input("Please select the item to be removed: ")

        re_amount = new[removeItem]
        inventory[removeItem][0] += re_amount
        del new[removeItem]
        basket_contents(current_user, logged_user_basket)
        basket_sub(current_user, logged_user_basket)

    elif option==3:
        checkout(current_user, logged_user_basket)

    elif option==4:
        main_menu(current_user, logged_user_basket)


online_commerce()
