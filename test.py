# Define a dictionary with some key-value pairs
fruit_inventory = {'apples': 10, 'oranges': 7}

# Define a list of fruits that we want to check
fruits_to_check = ['apples', 'peaches', 'oranges', 'pineapples']

# Write a loop that iterates over each fruit in fruits_to_check. 
# If the fruit is in the inventory, print the fruit and its count.
# If it's not in the inventory, print that the fruit is not in stock.
def print_fruit_inventory():
    for fruit in fruits_to_check:
        if fruit in fruit_inventory:
            print(f"{fruit}: {fruit_inventory[fruit]}")
        else:
            print(f"{fruit} is not in stock")

print_fruit_inventory();

# Use the .get() method to get the count of 'bananas' in the inventory. 
# If it's not found, return 'No bananas in stock'.
print(fruit_inventory.get('bananas', 'No bananas in stock'))
fruit_inventory['banana'] = 5;
print()
fruits_to_check.insert(4,'banana')
print_fruit_inventory();