def milk_bar():
    budget = float(input("What is your budget? $"))
    milkshakes = {
        1: {"flavor": "Chocolate", "price": 3.50},
        2: {"flavor": "Strawberry", "price": 4.00},
        3: {"flavor": "Vanilla", "price": 3.00}
    }
    
    while True:
        print("Available Milkshakes:")
        for number, shake in milkshakes.items():
            print(f"{number}. {shake['flavor']} - ${shake['price']}")
        
        order = input("What can I fix you? (Enter a number or Q to quit): ")
        
        if order.upper() == "Q":
            print("The barman wishes you well in your search for love.")
            break
        
        order = int(order)
        
        if order in milkshakes:
            if budget >= milkshakes[order]['price']:
                budget -= milkshakes[order]['price']
                print(f"You ordered {milkshakes[order]['flavor']} milkshake. Enjoy!")
            else:
                print("Sorry, you can't afford that milkshake. You're thrown out!")
                break
        else:
            print("Invalid input. Please enter a valid number or Q to quit.")

milk_bar()
