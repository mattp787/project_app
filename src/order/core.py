from db.core import update, connection, query, update_values
import uuid
import json
from os import system
from tabulate import tabulate

conn = connection()

def orders_menu(state):
    print(
"""
-----------------------------------
Select from the following options:
[1] to return to main menu
[2] to show orders
[3] to add new order
[4] to update order status
[5] to update order
[6] to delete order
-----------------------------------
"""
    )
    state['order'] = query(conn, f"SELECT transaction_id as id, customer_name as customer, customer_address as address, customer_phone as phone, courier, product, created_on FROM transaction INNER JOIN basket ON transaction.id = basket.transaction_id;")
    choice = int(input("\nEnter a selection\n")) - 1
    system('clear')
    if choice == 0:
        pass
    elif choice == 1:
        system('clear')
        show_orders(state)
        orders_menu(state)
    elif choice == 2:
        system('clear')
        add_order(state)
        orders_menu(state)
    elif choice == 3:
        system('clear')
        update_order_status(state)
        orders_menu(state)
    elif choice == 4:
        system('clear')
        update_order(state)
        orders_menu(state)
    elif choice == 5:
        system('clear')
        show_orders(state)
        delete_order(state)
        orders_menu(state)
    
def show_orders(state):
    print(tabulate(state['order'], headers="keys", showindex=True, tablefmt="fancy_grid"))

def add_order(state):
    customer = input("Enter the name of the customer: ").strip()
    address = input("Enter the address: ").strip()
    phone_number = input("Enter the phone number: ").strip()
    
    products = select_products(state)
    
    print(tabulate(state['courier'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    courier = state["courier"][int(input("\nSelect an index for the courier: "))]
    
    identifier = uuid.uuid4()
    update(conn, f"INSERT INTO transaction (id, customer_name, customer_address, customer_phone, courier, created_on) VALUES ('{identifier}', '{customer}', '{address}', '{phone_number}', '{courier['id']}', NOW())")
    for product in products:
        update(conn, f"INSERT INTO basket (transaction_id, product) VALUES ('{identifier}', '{product['id']}')")
        system('clear')

def update_order_status(state):
    print(tabulate(state['order'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    index = int(input("Select an index to modify ")) 
    state["order"][index]["order status"] = input("Enter the new order status ")

def update_order(state):
    print(tabulate(state['order'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    idx = int(input("Select an index to update: ")) 
    order = state['order'][idx]
    
    name = input("Type new name, or enter to skip: ")
    if name:
        order['customer'] = name
        
    address = input("Type new address, or enter to skip: ")
    if address:
        order['address'] = address
    
    phone = input("Type new phone, or enter to skip: ")
    if phone:
        order['phone'] = phone
        
    products = select_products(state)
    
    
    
    old_product = order['product']
    print(tabulate(state['courier'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    order['courier'] = state["courier"][int(input("Select an index for the courier: "))]['id']
    
    update_values(conn, "UPDATE transaction SET customer_name = %s WHERE id = %s", (order['customer'], order['id']))
    update_values(conn, "UPDATE transaction SET customer_address = %s WHERE id = %s", (order['address'], order['id']))
    update_values(conn, "UPDATE transaction SET customer_phone = %s WHERE id = %s", (order['phone'], order['id']))
    update_values(conn, "UPDATE transaction SET courier = %s WHERE id = %s", (order['courier'], order['id']))

    update(conn, f"DELETE FROM basket WHERE transaction_id = '{order['id']}'")
    for product in products:
        update(conn, f"INSERT INTO basket (transaction_id, product) VALUES ('{order['id']}', '{product['id']}');")

def select_products(state):
    products = []
    print(tabulate(state['product'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    sel = input(("Enter index of product, press enter to end: ")).strip()
    while sel != "":
        index = int(sel)
        products.append(state["product"][index])
        sel = input(("Enter index of product, press enter to end: ")).strip()
    return products
    
def delete_order(state):
    print(tabulate(state['order'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    index = int(input("Select an index to delete: "))
    to_delete = state['order'][index]
    print(to_delete)
    update(conn, f"DELETE FROM transaction WHERE id = '{to_delete['id']}'")
    update(conn, f"DELETE FROM basket WHERE transaction_id = '{to_delete['id']}'")
    
    
