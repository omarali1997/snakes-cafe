def print_menu():
    print("***************************************\n**     welcome to the Snakes Cafe!   **\n**     Please see our menu below.    ** \n**                                   **\n** To quit at any time, type  'quit' **\n***************************************\nAppetizers\n----------\nwings\ncookies\nspring Rolls\n\nEntrees\n-------\nSalmon\nSteak\nMeat Torando\nA Literal Garden\n\nDesserts\n--------\nIce Cream\nCake\npie\n\nDrinks\n------\nCoffee\nTea\nUnicorn Tears")
    print("***********************************\n** What would you like to order? **\n***********************************")

print_menu()

menu=["wings","cookies","spring rolls","salmon","steak","meat torando","a literal garden","ice cream","cake","pie","coffee","tea","unicorn tears"]

def take_order():
    x=[]
    while True:
        order=input("> ")
        count = 0
        if order == "quit" :
            break
        
        if order.lower() in menu:
            x.append(order.lower())
            
            if order.lower() in x:

                for z in range(len(x)) :
                    if order.lower() == x[z]:
                        count+=1
                print(f"** {count} order of {order} have been added to your meal **")
            else:
                count+=1
                print(f"** {count} order of {order} have been added to your meal **")
        elif order.lower() not in menu:
            print(f"sorry, no {order} in our menu")
            # x.pop()
    print(f"you order is: {x}")
    # print(menu)
take_order()