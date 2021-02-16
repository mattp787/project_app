from os import system
from db.core import update, connection

insert_new_product = "INSERT INTO product (name,price) VALUES ('orange',2)"
conn = connection()


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
    except Exception as e:
        input(f"ERROR: {e}")
        print("Invalid input, please try again")
        product_menu(state)

def show_products(state):
    # system("clear")
    for item in state["product"]:
        print(f"Item: {item['name']}      \tPrice: £{item['price']};")
    print("\n")
    
def add_product(state):
    item = input("enter the item name ").strip().lower().title()
    price = float(input("enter the price of the item "))
    product = {'name':item,"price":price}
    state["product"].append(product)
    update(conn, f"INSERT INTO product (name,price) VALUES ('{item}',{price});")
    
def update_product(state):
    for count, item in enumerate(state["product"],1):
        print(count,f"Item: {item['name']},   Price: {item['price']}")
    index = int(input("type index to update "))-1
    new_name = input("update product ").strip().lower().title()
    new_price = float(input("update price "))
    old_name = state["product"][index]["name"]
    update(conn, f"UPDATE product SET name = '{new_name}', price = {new_price} WHERE name = '{old_name}'")
    state["product"][index]["name"] = new_name
    state["product"][index]["price"] = new_price
    
    
def delete_product(state):
    for count, item in enumerate(state["product"],1):
        print(count,f"Item: {item['name']},   Price: {item['price']}")
    index = int(input("type index to delete "))-1
    to_delete = state["product"][index]["name"]
    update(conn, f"DELETE FROM product WHERE name = '{to_delete}'")
    state["product"].remove(state["product"][index])