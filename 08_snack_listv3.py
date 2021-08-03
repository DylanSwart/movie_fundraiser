# Component 7v3 snack/ticket lists
import pandas

# initialise snack lists

all_names = ['Dylan', 'Bob', 'Jill', 'Bill', 'Jane']
all_tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data frames dictionary
movie_data_dict = {
    'Name': all_names,
    'Tickets': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}

# Cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'M&Ms': 3,
    'Pita Chips': 4.5,
    'Orange Juice': 3.25
}

test_data = [
[[1, 'Water'], [1, 'Pita Chips'], [1, 'M&Ms']],
[[]],
[[1, 'Pita Chips'], [1, 'Orange Juice'], [2, 'M&Ms']],
[[1, 'Water'], [1, 'Popcorn']],
[[1, 'M&Ms'], [1, 'Pita Chips']]
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
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# Create column called Sub Total
# Fill it with price of tickets and snacks

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice']

print(movie_frame)
