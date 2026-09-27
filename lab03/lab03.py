print(f"""
Welcome to Your Shopping List!
 
Please make a selection from one of the following options:
 
1. Add an item to the shopping list.
2. Display the shopping list.
3. Display the item count.
4. Display the first item in the shopping list.
5. Display the last item in the shopping list.
6. Clear the shopping list.
""")

selection = input("Selection:")

grocery_list = []

if(selection == "1"):
    item = input("Item to add: ")
    grocery_list.append(item)

elif(selection == "2"):
     print(f"SHOPPING LIST: {grocery_list}")

elif(selection == "3"):
    print(f"ITEM COUNT: {len(grocery_list)}")

elif(selection == "4"):
    print(f"FIRST ITEM: {grocery_list[0]}")

elif(selection == "5"):
    print(f"LAST ITEM: {grocery_list[-1]}")

elif(selection == "6"):
    grocery_list = []
    print(f"The shopping list is now empty!")

else:
    print(f"You entered an invalid option.")
    print(f"Goodbye!")