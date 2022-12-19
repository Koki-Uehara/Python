days = ['monday', 'tuesday', 'wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'bear']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)