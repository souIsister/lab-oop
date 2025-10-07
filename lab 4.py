menu = {
    "bread": 10.00,
    "eggnog": 10.00,
    "ehips": 15.00,
    "piatos": 15.00,
    "twigs": 80.00,
    "lays": 65.00,
    "noodles": 18.00,
    "cheezy": 10.00,
    "condom": 150.00,
    "dildo": 50.00,
}

orders = []
prices = []

print("---------- MENU ----------")
for item, price in menu.items():
    print(f"{item}\t\t : ₱{price:.2f}")
print("--------------------------")

while True:
    choice = input("Select an item (q to quit): ").lower()
    if choice == 'q':
        break
    elif choice in menu:
        price = menu[choice]
        orders.append(choice)
        prices.append(price)
    else:
        print(f"{choice} not available. Only input item on the menu.")

print("---------- YOUR ORDER ----------")
for order in orders:
    print(f"- {order}")

total = sum(prices)
print(f"\nTotal is: ₱{total:.2f}")
