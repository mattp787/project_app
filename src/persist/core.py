import csv

def fetch_product_data(filename="data/products.csv"):
    try:
        products_data = []
        with open(filename,"r") as file:
            csvfile = csv.DictReader(file)
            for item in csvfile:
                products_data.append(item)
            return products_data
    except FileNotFoundError:
        print("File does not exist")  
        
def fetch_courier_data(filename="data/couriers.csv"):
    try:
        couriers_data = []
        couriers_file = open(filename,"r")
        return couriers_file.read().split()
    except FileNotFoundError:
        print("File does not exist")
    
def fetch_orders_data(filename="data/orders.csv"):
    try:
        orders_data = []
        with open(filename,"r") as file:
            csvfile = csv.DictReader(file)
            for item in csvfile:
                orders_data.append(item)
            return orders_data
    except FileNotFoundError:
        print("File does not exist")   
        
def save_product_data(state,filename:str="data/products.csv"):
    products_file = open(filename,"w")
    if state["product"]:
        fieldnames = ["item","price"]
        writer = csv.DictWriter(products_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in state["product"]:
            writer.writerow({"item":item.get("item"),"price":item.get("price")})
            print(item)
    else:
        products_file.writelines("")
        
def save_courier_data(state,filename:str="data/couriers.csv"):
    couriers_file = open(filename,"w")
    if state["courier"]:
        for item in state["courier"]:
            couriers_file.writelines(item+"\n")
    else:
        couriers_file.writelines("")
        
def save_orders_data(state,filename:str="data/orders.csv"):
    orders_file = open(filename,"w")
    if state["order"]:
        fieldnames = ["customer","address","phone number","courier","products","order status"]
        writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in state["order"]:
            writer.writerow({"customer":item.get("customer"),"address":item.get("address"),"phone number":item.get("phone number"),"courier":item.get("courier"),"products":item.get("products"), "order status":item.get("order status")            
            })
            print(item)
    else:
        orders_file.writelines("")
        
def save_exit(state):
    save_orders_data(state)
    save_product_data(state)
    save_courier_data(state)
    exit()