from db.core import update, connection, query
import uuid

conn = connection()

def orders_menu(state):
    print(
"""
Select from the following options:
[1] to return to main menu
[2] to show orders
[3] to add new order
[4] to update order status
[5] to update order
[6] to delete order
"""
    )

    # try:
    #     choice = int(input("\nEnter a selection\n")) - 1
    #     if choice == 0:
    #         pass
    #     elif choice == 1:
    #         show_orders(state)
    #         orders_menu(state)
    #     elif choice == 2:
    #         add_order(state)
    #         orders_menu(state)
    #     elif choice == 3:
    #         update_order_status(state)
    #         orders_menu(state)
    #     elif choice == 4:
    #         show_orders(state)
    #         update_order(state)
    #         orders_menu(state)
    #     elif choice == 5:
    #         show_orders(state)
    #         delete_order(state)
    #         orders_menu(state)
    # except:
    #     print("Invalid input, please try again")
    #     orders_menu(state)
    
    choice = int(input("\nEnter a selection\n")) - 1
    if choice == 0:
        pass
    elif choice == 1:
        show_orders(state)
        orders_menu(state)
    elif choice == 2:
        add_order(state)
        orders_menu(state)
    elif choice == 3:
        update_order_status(state)
        orders_menu(state)
    elif choice == 4:
        show_orders(state)
        update_order(state)
        orders_menu(state)
    elif choice == 5:
        show_orders(state)
        delete_order(state)
        orders_menu(state)
    
def show_orders(state):
    # state = parse_state(state)
    for idx in range(len(state["order"])):
        print(f"""
customer : {state["order"][idx]["customer"]}
address : {state["order"][idx]["address"]}
phone number : {state["order"][idx]["phone number"]}
courier : {state["order"][idx]["courier"]}
products : {state["order"][idx]["products"]}
order status : {state["order"][idx]["order status"]}
            """
            )
            

def add_order(state):
    #GET ORDER
    customer = input("enter the name of the customer ").strip()
    address = input("enter the address ").strip()
    phone_number = input("enter the phone number ").strip()
    ##### THIS IS FOR CACHED DATA
    products = []
    sel = 1
    while sel != "0":
        for item, count in enumerate(state["product"]):
            print(item, count)
        products.append(state["product"][int(input("select an index to add a product: "))].get("name"))
        sel = input(("Press enter to add more products, press 0 to finish adding products ")).strip()
        
    for item, count in enumerate(state["courier"]):
        print(item, count)
    courier = state["courier"][int(input("select an index for the courier: "))]
    order = {"customer":customer,"address":address,"phone number":phone_number,"courier":courier,"products":products,"order status":"preparing"}
    state["order"].append(order)
    ######
    courier_name = courier["name"]
    courier_id = query(conn,f"SELECT id FROM courier WHERE name = '{courier_name}'")[0]["id"]
    print(products)
    for product in products:
        identifier = uuid.uuid4()
        # print(product)
        product_id = query(conn,f"SELECT id FROM product WHERE name = '{product}'")[0]["id"]
        
        # print(f"INSERT INTO transaction (id, customer_name, customer_address, customer_phone, courier) VALUES ('{identifier}', '{customer}', '{address}', '{phone_number}', {courier_id});")
        # print(f"INSERT INTO basket (transaction_id, product) VALUES ('{identifier}', '{product_id}');")
        update(conn, f"INSERT INTO transaction (id, customer_name, customer_address, customer_phone, courier) VALUES ('{identifier}', '{customer}', '{address}', '{phone_number}', {courier_id});")
        # [x["name"] for x in state["product"]]
        update(conn, f"INSERT INTO basket (transaction_id, product) VALUES ('{identifier}', '{product_id}');")
    
    
def update_order_status(state):
    for idx, order in enumerate(state["order"],1):
        print(idx, order)
    index = int(input("Select an index to modify ")) - 1
    state["order"][index]["order status"] = input("Enter the new order status ")
    
def update_order(state):
    for idx, order in enumerate(state["order"],1):
        print(idx, order)
    idx = int(input("Select an index to update ")) - 1
    customer = input("enter the name of the customer or enter to skip ").strip() 
    if customer == "":
        customer = state["order"][idx]["customer"]
    address = input("enter the address or enter to skip ").strip()
    if address == "":
        address = state["order"][idx]["address"]
    phone_number = input("enter the phone number or enter to skip ").strip()
    if phone_number == "":
        phone_number = state["order"][idx]["phone number"]
    #####
    products = []
    sel = 1
    while sel != "0":
        for item, count in enumerate(state["product"]):
            print(item, count)
        products.append(state["product"][int(input("select an index to add a product: "))].get("name"))
        sel = input(("Press enter to add more products, press 0 to finish adding products ")).strip()
    #####
    for item, count in enumerate(state["courier"]):
        print(item, count)
    courier = str(state["courier"][int(input("select an index for the courier: "))])
    order = {"customer":customer,"address":address,"phone number":phone_number,"products":products,"courier":courier,"order status":"preparing"}
    state["order"][idx] = order
    
def delete_order(state):
    for idx, order in enumerate(state["order"],1):
        print(idx, order)
    state["order"].pop(int(input("Select an index to delete "))-1)
    
def to_list(to_parse):
    parsed = to_parse.replace("[", "").replace("]", "").split(", ")
    parsed = [x for x in parsed]
    return parsed

def parse_state(state):
    for order in state['order']:
        order['products'] = to_list(order['products'])
    return state