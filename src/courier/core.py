from db.core import update, connection, query
from tabulate import tabulate
from os import system

conn = connection()
def courier_menu(state):
    print(
"""
-----------------------------------
Select from the following options:
[1] to return to main menu
[2] to show couriers
[3] to add new courier
[4] to update courier
[5] to delete courier
-----------------------------------
"""
    )
    state["courier"] = query(conn, f"SELECT * FROM courier")
    choice = int(input("\nEnter a selection\n")) - 1
    system('clear')
    if choice == 0:
        pass
    elif choice == 1:
        system('clear')
        show_couriers(conn, state)
        courier_menu(state)
    elif choice == 2:
        system('clear')
        try:
            add_courier(state)  
        except:
            print("Failed to add courier")
        courier_menu(state)
    elif choice == 3:
        system('clear')
        try:
            update_courier(state, select_courier)
        except:
            print("Failed to update courier")
        courier_menu(state)
    elif choice == 4:
        system('clear')
        try:
            delete_courier(state, select_courier)
        except:
            print("Failed to delete courier")
        courier_menu(state)
    
        

def show_couriers(conn, state):
    state["courier"] = query(conn, f"SELECT * FROM courier")
    print(tabulate(state['courier'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    

def add_courier(state):
    new_name = input("Enter a new courier: ").strip().lower().title()
    availability = input("Enter the availability: ").strip().lower().title()
    courier = {"name":new_name, "available":availability}
    update(conn, f"INSERT INTO courier (name, available) VALUES ('{new_name}','{availability}')")

    
def select_courier(state):
    print(tabulate(state['courier'], headers="keys", showindex=True, tablefmt="fancy_grid"))
    index = int(input("Enter an index or enter to cancel: "))
    return index
    
def delete_courier(state, select_courier):
    sel = select_courier(state)
    to_delete = state["courier"][sel]["name"]
    if sel != 0:
        state["courier"].pop(sel-1)
        update(conn, f"DELETE FROM courier WHERE (name = '{to_delete}')")
        
def update_courier(state, select_courier):
    index = select_courier(state)
    if index != None:
        to_update = state["courier"][index]["name"]
        new_name = str(input("Type new courier: "))
        new_availability = str(input("Type availability: "))
        state["courier"][index] = {"name":new_name, "available":new_availability}
        update(conn, f"UPDATE courier SET name = '{new_name}', available = '{new_availability}' WHERE (name = '{to_update}')")
    
