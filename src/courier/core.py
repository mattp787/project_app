from db.core import update, connection

conn = connection()
def courier_menu(state):
    print(
"""
Select from the following options:
[1] to return to main menu
[2] to show couriers
[3] to add new courier
[4] to update courier
[5] to delete courier
"""
    )

    choice = int(input("\nEnter a selection\n")) - 1
    if choice == 0:
        pass
    elif choice == 1:
        show_couriers(state)
        courier_menu(state)
    elif choice == 2:
        try:
            add_courier(state)  
        except:
            print("Failed to add courier")
        courier_menu(state)
    elif choice == 3:
        try:
            update_courier(state, select_courier)
        except:
            print("Failed to update courier")
        courier_menu(state)
    elif choice == 4:
        try:
            delete_courier(state, select_courier)
        except:
            print("Failed to delete courier")
        courier_menu(state)
    
        

def show_couriers(state):
    for x in range(len(state["courier"])):
        print(
            f"""Name: {state["courier"][x]["name"]} \t Available: {state["courier"][x]["available"]}""")

def add_courier(state):
    print(state["courier"])
    new_name = input("Enter a new courier: ").strip().lower().title()
    availability = input("Enter the availability: ").strip().lower().title()
    courier = {"name":new_name, "available":availability}
    state["courier"].append(courier)
    update(conn, f"INSERT INTO courier (name, available) VALUES ('{new_name}','{availability}')")

    
def select_courier(state):
    for item,count in enumerate(state["courier"],1):
        print(f"{item} : {count}")
    index = int(input("Enter an index or 0 to cancel: "))
    return index
    
def delete_courier(state, select_courier):
    sel = select_courier(state)
    to_delete = state["courier"][sel-1]["name"]
    if sel != 0:
        state["courier"].pop(sel-1)
        update(conn, f"DELETE FROM courier WHERE (name = '{to_delete}')")
        
def update_courier(state, select_courier):
    index = select_courier(state)
    if index != 0:
        to_update = state["courier"][index-1]["name"]
        new_name = str(input("Type new courier: "))
        new_availability = str(input("Type availability: "))
        state["courier"][index-1] = {"name":new_name, "available":new_availability}
        update(conn, f"UPDATE courier SET name = '{new_name}', available = '{new_availability}' WHERE (name = '{to_update}')")
    
