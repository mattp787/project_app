

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
    (state["courier"]).append(input("Enter a new courier: "))

def delete_courier(state):
    for item,count in enumerate(state["courier"],1):
        print(f"{item} : {count}")
    sel = int(input("Enter an index to delete, or 0 to cancel: "))
    if sel != 0:
        state["courier"].pop(sel-1)
        
def update_courier(state):
    for count, item in enumerate(state["courier"],1):
        print(count,item)
    index = int(input("Type index to update, or enter 0 to cancel "))
    if index != 0:
        state["courier"][index-1] = str(input("Type new courier: "))
    
