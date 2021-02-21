from os import system
from db.core import update, connection, query
from tabulate import tabulate

conn = connection()


def product_menu(state):
    print(
"""
-----------------------------------
Select from the following options:
[1] to return to main menu
[2] to show products
[3] to add new product
[4] to update product
[5] to delete product
-----------------------------------
"""
    )
    state['product'] = query(conn, f"SELECT * FROM product")
    choice = int(input("\nEnter a selection\n")) - 1
    system('clear')
    if choice == 0:
        pass
    
    elif choice == 1:
        system('clear')
        show_products(state)
        product_menu(state)
        
        
    elif choice == 2:
        system('clear')
        item, price = get_new_product()
        try:
            # add_product_cache(state, item, price)
            add_product_db(item, price, conn)
        except:
            print("Failed to add product")
        system('clear')
        product_menu(state)
        
    elif choice == 3:
        system('clear')
        try:
            update_product(state, select_product)
        except Exception as e:
            print("Failed to update product")
        
        product_menu(state)
            
    elif choice == 4:
        
        try:
            delete_product(state)
        except:
            print("Failed to delete product")
        system('clear')
        product_menu(state)



def show_products(state):
    state['product'] = query(conn, f"SELECT * FROM product")
    print(tabulate(state['product'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    

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
    print(tabulate(state['product'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    index = int(input("Type index to update or enter to skip: "))
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