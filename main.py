from re import match
from termcolor import colored
from tabulate import tabulate
menu = {}
orders = {}
reviewOrders = []
viewMenu = []

def add():
    id = str(len(menu) + 1)
    if id not in menu :
        id = str(len(menu) + 1)
    else :
        id = str(len(menu))
    name = input(colored("Enter Dish name: ", "blue"))
    price = input(colored("Enter Dish price: ", "blue"))
    if not match(r'^\d+$', price) :
        print(colored("Price can be numbers only!", "red"))
        return add()
    stock = input(colored("Enter quantity: ", "blue"))
    if not match(r'^\d+$', stock) :
        print(colored("Stock can be numbers only!", "red"))
        return add()
    
    menu[id] = {
        "name": name,
        "price": int(price),
        "stock": int(stock)
    }
    viewMenu.append({
        "id":id,
        "name": name,
        "price": int(price),
        "stock": int(stock)
    })

    print(colored(f"{name} has been added!", "green"))

def remove():
    print("Enter the Dish ID to remove")
    dish = input(colored("Enter Dish ID","blue"))
    if (dish not in menu) :
        print(colored("Please enter valid ID!","red"))
        return remove()
    print(colored(f"{menu[dish]['name']} has been removed!","green"))
    del menu[dish]
    viewMenu.pop(int(dish)-1)

def update():
    print("Enter the Dish ID to update quantity")
    dish = input(colored("Enter Dish ID","blue"))
    if (dish not in menu) :
        print(colored("Please enter valid ID!","red"))
        return update()
    quantity = input(colored("Enter updated quantity", "blue"))
    if not match(r'^\d+$', quantity) :
        print(colored("Stock can be numbers only!", "red"))
        return update()
    
    menu[dish]["stock"] = int(quantity)
    print(colored("Stock has been updated!","green"))
    viewMenu[int(dish)-1]['stock'] = int(quantity)

def order():
    print("Enter the Dish ID to order")
    dish = input(colored("Enter Dish ID","blue"))
    if (dish not in menu) :
        print(colored("Please enter valid ID!","red"))
        return order()
    quantity = input(colored("Enter Quantity","blue"))
    if int(quantity) > menu[dish]['stock'] :
        print(colored(f"Only {menu[dish]['stock']} pcs of {menu[dish]['name']} is available","red"))
        return order()
    id = str(len(orders) + 1)
    orders[id] = {
        "name": menu[dish]['name'],
        "price": menu[dish]['price'],
        "quantity": int(quantity),
        "status": "Received"
    }
    reviewOrders.append({
        "id":id,
        "name": menu[dish]['name'],
        "price": menu[dish]['price'],
        "quantity": int(quantity),
        "status": "Received"
    })
    menu[dish]['stock'] -= int(quantity)
    viewMenu[int(dish)-1]['stock'] -= int(quantity)
    print(colored("Order has been placed!","green"))

def updateStatus():
    print("Enter the order ID to update status")
    order = input(colored("Enter Order ID","blue"))
    if (order not in orders) :
        print(colored("Please enter valid ID!","red"))
        return updateStatus()
    print("1. Preparing")
    print("2. Ready for pickup")
    print("3. Delivered")
    status = {
        "1":"Preparing",
        "2":"Ready for pickup",
        "3":"Delivered"
    }
    userInput = input(colored("Choose an option: ","blue"))
    orders[order]["status"] = status[userInput]
    reviewOrders[int(order)-1]["status"] = status[userInput]
    print(colored("Order Status has been updated!","green"))

def review() :
    if len(reviewOrders) == 0 :
        print(colored("No orders has been placed", "red"))
        return operation()
    headers = reviewOrders[0].keys()
    table = tabulate([[row[col] for col in headers] for row in reviewOrders], headers, tablefmt="grid")
    print(table)

def menuu() :
    if len(viewMenu) == 0 :
        print(colored("No Dishes in menu!", "red"))
        return operation()
    headers = viewMenu[0].keys()
    table = tabulate([[row[col] for col in headers] for row in viewMenu], headers, tablefmt="grid")
    print(table)

def operation() :
    while True:
        print("1. Add Dish")
        print("2. Remove Dish")
        print("3. Update Dish availability")
        print("4. New Order")
        print("5. Update Order Status")
        print("6. Review Orders")
        print("7. View Menu")
        print(colored("0. Exit", "red"))
        userInput = input(colored("Choose an option: ", "blue"))

        if userInput == "1" :
            add()
        elif userInput == "2":
            remove()
        elif userInput == "3" :
            update()
        elif userInput == "4":
            order()
        elif userInput == "5":
            updateStatus()
        elif userInput == "6":
            review()
        elif userInput == "0":
            print(colored("Thanks for visiting!","cyan"))
            return
        elif userInput == "7" :
            menuu()
        else :
            print(colored("Please enter valid Input", "red"))
            break

operation()
