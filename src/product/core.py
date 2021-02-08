from os import system

def product_menu(state):
    print(
"""
Select from the following options:
[1] to return to main menu
[2] to show products
[3] to add new product
[4] to update product
[5] to delete product
"""
    )

    try:
        choice = int(input("\nEnter a selection\n")) - 1
        if choice == 0:
            pass
        elif choice == 1:
            show_products(state)
            product_menu(state)
        elif choice == 2:
            add_product(state)
            product_menu(state)
        elif choice == 3:
            update_product(state)
            product_menu(state)
        elif choice == 4:
            delete_product(state)
            product_menu(state)
    except:
        print("Invalid input, please try again")
        product_menu(state)
        
        
def show_products(state):
    # system("clear")
    for item in state["product"]:
        print(f"Item: {item['item']},   Price: {item['price']}")
    print("\n")
    
def add_product(state):
    item = input("enter the item name ").strip().lower().title()
    price = float(input("enter the price of the item "))
    product = {"item":item,"price":price}
    state["product"].append(product)
    
def update_product(state):
    for count, item in enumerate(state["product"]):
        print(count,f"Item: {item['item']},   Price: {item['price']}")
    index = int(input("type index to update "))
    state["product"][index]["item"] = input("update product ").strip().lower().title()
    state["product"][index]["price"] = float(input("update price "))
    
def delete_product(state):
    for count, item in enumerate(state["product"],1):
        print(count,f"Item: {item['item']},   Price: {item['price']}")
    index = int(input("type index to delete "))
    state["product"].remove(state["product"][index-1])