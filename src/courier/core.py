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
    try:
        choice = int(input("\nEnter a selection\n")) - 1
        if choice == 0:
            pass
        elif choice == 1:
            show_couriers(state)
            courier_menu(state)
        elif choice == 2:
            add_courier(state)
            courier_menu(state)
        elif choice == 3:
            update_courier(state)
            courier_menu(state)
        elif choice == 4:
            delete_courier(state)
            courier_menu(state)
    except:
        print("Invalid input, please try again")
        courier_menu(state)

def show_couriers(state):
    print(state["courier"])

def add_courier(state):
    try:
        print(state["courier"])
        new_name = input("Enter a new courier: ").strip().lower().title()
        availability = input("Enter the availability: ").strip().lower().title()
        courier = {"name":new_name, "available":availability}
        state["courier"].append(courier)
        update(conn, f"INSERT INTO courier (name, available) VALUES ('{new_name}','{availability}')")
    except Exception as e:
        input(f"{e}")
    
def delete_courier(state):
    for item,count in enumerate(state["courier"],1):
        print(f"{item} : {count}")
    sel = int(input("Enter an index to delete, or 0 to cancel: "))
    to_delete = state["courier"][sel-1]["name"]
    print(to_delete)
    if sel != 0:
        state["courier"].pop(sel-1)
        update(conn, f"DELETE FROM courier WHERE (name = '{to_delete}')")
        
def update_courier(state):
    for count, item in enumerate(state["courier"],1):
        print(count,item)
    index = int(input("Type index to update, or enter 0 to cancel "))
    if index != 0:
        to_update = state["courier"][index-1]["name"]
        print(to_update)
        new_name = str(input("Type new courier: "))
        new_availability = str(input("Type availability: "))
        state["courier"][index-1] = {"name":new_name, "available":new_availability}
        update(conn, f"UPDATE courier SET name = '{new_name}', available = '{new_availability}' WHERE (name = '{to_update}')")
    

#GET INPUT
#ADD TO STATE
#ADD TO DATABASE 