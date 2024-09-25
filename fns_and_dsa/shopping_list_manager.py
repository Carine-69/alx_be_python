shopping_list = []


while True:
    items = input("What do you want do : view  items / add items / remove items / exit: ")
    if items == "view items":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    
    elif items == "add items":
        newItems = input("what do you want to add to the list: ")
        shopping_list.append(newItems)
        print(f"{newItems} has been added to your shopping list")

    
    elif items == "remove items":
        removed_items = input("what do you want to remove: ")
        if removed_items in shopping_list:
            shopping_list.remove(removed_items)
            print(f"{removed_items} have been removed from your shopping list")
        else:
            print(f"{removed_items} not found in shopping list, try again")

    elif items == "exit":
        print("Exiting the shopping list")
        exit()
    else:
        print("invalid choie, try again")





