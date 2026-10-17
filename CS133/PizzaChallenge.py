def pizza_cost_calculator(pizza, price):
    num_pizzas = int(input(f"How many {pizza} pizzas? "))
    cost_of_order = num_pizzas * price

    return cost_of_order


pizzas = ["Pepperoni", "Hawaiin", "Taco Style", "Meat Lovers",]
prices = [18, 20, 22, 23]

total_cost = 0

pizzas.append("Cheese")
prices.append(15)

for p in range(len(pizzas)):
    total_cost += pizza_cost_calculator(pizzas[p], prices[p])
print(f'The total comes to ${total_cost}')

