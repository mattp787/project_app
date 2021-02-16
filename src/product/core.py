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
    
    choice = int(input("\nEnter a selection\n")) - 1
    if choice == 0:
        pass
    
    elif choice == 1:
        show_products(state)
        product_menu(state)
        
    elif choice == 2:
        item, price = get_new_product()
        try:
            add_product_cache(state, item, price)
            add_product_db(item, price, conn)
        except:
            print("Failed to add product")
        product_menu(state)
            
    elif choice == 3:
        try:
            update_product(state, select_product)
        except:
            print("Failed to update product")
        product_menu(state)
            
    elif choice == 4:
        try:
            delete_product(state)
        except:
            print("Failed to delete product")
        product_menu(state)



def show_products(state):
    # system("clear")
    for item in state["product"]:
        print(f"Item: {item['name']}      \tPrice: £{item['price']}")
    print("\n")
    

def get_new_product():
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    return item, price

def add_product_cache(state, item, price):
    product = {"name":item, "price":price}
    state["product"].append(product)

def add_product_db(item, price, conn):
    update(conn, f"INSERT INTO product (name,price) VALUES ('{item}',{price});")
    

def select_product(state):
    for count, item in enumerate(state["product"],1):
        print(count,f"Item: {item['name']},   Price: {item['price']}")
    index = int(input("type index to update "))-1
    return index

def update_product(state, select_product):
    index = select_product(state)
    new_name = input("Enter new name: ").strip().lower().title()
    new_price = float(input("Enter new price "))
    old_name = state["product"][index]["name"]
    state["product"][index]["name"] = new_name
    state["product"][index]["price"] = new_price
    update(conn, f"UPDATE product SET name = '{new_name}', price = {new_price} WHERE name = '{old_name}'")


def delete_product(state):
    index = select_product(state)
    to_delete = state["product"][index]["name"]
    state["product"].remove(state["product"][index])
    update(conn, f"DELETE FROM product WHERE name = '{to_delete}'")