import csv
import uuid
# from src.product.core import product_menu, show_products, add_product, delete_product
from src.product.core import product_menu, show_products, delete_product, get_new_product, add_product_db, add_product_cache
from src.courier.core import courier_menu, show_couriers, add_courier, delete_courier
from src.order.core import orders_menu, show_orders, add_order, delete_order
from src.persist.core import fetch_courier_data,fetch_orders_data,fetch_product_data,save_courier_data,save_orders_data,save_product_data,save_exit
from db.core import connection, query, update

global state
state = {"order":[],"courier":[],"product":[]}

# STRUCTURE OF STATE VARIABLES
# product = [{"item":"lemon","price":0.20},{"item":"lime","price":0.35}]
# order = [{"customer":"Matt","address":"Castle Street","phone number":197,"courier":"Deliveroo","products":product,"order status":"preparing order"}]
# courier = ["Deliveroo", "Just Eat"]
# state = [order, courier, product]
# state = {"order":LISTOFORDERS, "courier":LISTOFCOURIERS,"product":LISTOFPRODUCTS}

conn = connection()

select_all_products = "SELECT * FROM product"
select_all_couriers = "SELECT * FROM courier"


def main_menu(state):
    print(
"""
Select from the following options:
[1] to save and exit
[2] to show product menu
[3] to show courier menu
[4] to show order menu
"""
    )

    try:
        choice = int(input("\nEnter a selection\n")) - 1
    except:
        print("Invalid input, please try again")
        main_menu(state)

    if choice == 0:
        save_exit(state)
    elif choice == 1:
        product_menu(state)
    elif choice == 2:
        courier_menu(state)
    elif choice == 3:
        orders_menu(state)
    else:
        print("Invalid input, please try again")
        main_menu(state)   




# main_menu(state)
# add_courier(state)
# add_courier(state)
# show_couriers(state)
# delete_courier(state)
# show_couriers(state)

state["product"] = list(fetch_product_data(conn,select_all_products))
state["courier"] = list(fetch_courier_data(conn,select_all_couriers))
state["order"] = list(fetch_orders_data())

print(uuid.uuid4())
# print(query(conn,"SELECT id FROM product WHERE name = 'test3'")[0]["id"])
# print([(x["id"], x["name"]) for x in query(conn,"SELECT * FROM product")])


while True:
    main_menu(state)


