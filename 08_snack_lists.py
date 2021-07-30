# Component 7 snack lists

# Initialise snack lists
names = ['Dylan', 'Bob', 'Jill', 'Bill']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Orange Juice': orange_juice
    }

test_data = [
    [[1, 'Water'], [1, 'Pita Chips'], [1, 'M&Ms']],
    [[]],
    [[1, 'Pita Chips'], [1, 'Orange Juice'], [2, 'M&Ms']],
    [[1, 'Water']]
]

count = 0
for client_order in test_data:

    # Assume No snacks have been bought
    for item in snack_lists:
        item.append(0)

    # Print snack list

    # Get order hard coded for testing
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = snack_menu_dict[to_find]
            add_list[-1] = amount

print(snack_lists)
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips", snack_lists[2])
print("Water", snack_lists[3])
print("Orange Juice", snack_lists[4])
