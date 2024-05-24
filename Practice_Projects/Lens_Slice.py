toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(f'We sell {num_pizzas} different kinds of pizza!')

pizza_and_prices = []
for i in range(len(toppings)):
    pizza_and_prices.append([prices[i], toppings[i]])

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(4, [2.5, "peppers"])

three_cheapest = pizza_and_prices[:5]
print(three_cheapest)

