# list days of the week
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# define test customer: name, day, selection criteria
test_customer = ['Karolina', 'Monday', ['vegetarian', 'dessert']]

# get index of menu day
def get_week_day_index(week_day):
    week_day_index = week_days.index(week_day)
    return week_day_index

# test case 1: get index of week_days(day)
# print(get_week_day_index('Wednesday'))

# get current day for customer
def get_current_day(customer):
    current_day = customer[1]
    customer_current_day_index = get_week_day_index(current_day) 
    return customer_current_day_index

# test case 2: check if customer's current day matches the week_days index
# test_current_day_index = get_current_day(test_customer)
# print(test_current_day_index)

# list of menu items for every day of week_days
menu_items = []
for week_day in week_days:
    menu_items.append([])

# add menu items for each day of week
def add_menu_item(week_day, menu_item):
    try:
        week_day_index = get_week_day_index(week_day)
        menu_items_on_week_day = menu_items[week_day_index].append(menu_item)
    except SyntaxError:
        return

add_menu_item('Monday', ["Slow Cooker Texas Pulled Pork", ['meat']])
add_menu_item('Tuesday', ["Quick Beef Stir-Fry", ['meat', 'veggies']])
add_menu_item('Thursday', ["Slow-Cooker Corned Beef and Cabbage", ['meat', 'veggies']])
add_menu_item('Saturday', ["Chef John's Perfect Prime Rib", ['meat']])

add_menu_item('Monday', ["Chicken Stir-Fry", ['poultry', 'veggies']])
add_menu_item('Wednesday', ["Frito Chicken Casserole", ['poultry']])
add_menu_item('Friday', ["Cast Iron Roast Chicken and Potatoes", ['poultry']])
add_menu_item('Sunday', ["Broccoli Chicken Divan", ['poultry', 'veggies']])

add_menu_item('Tuesday', ["Easy Paella", ['fish', 'seafood']])
add_menu_item('Monday', ["Baked Haddock with side veggies", ['fish', 'veggies']])
add_menu_item('Saturday', ["The Best Thai Coconut Soup", ['fish', 'seafood']])

add_menu_item('Monday', ["Vegetarian Pasta Salad", ['vegetarian', 'salad']])
add_menu_item('Tuesday', ["Vegetarian Curry", ['vegetarian']])
add_menu_item('Friday', ["Pub-Style Vegetarian Chili", ['vegetarian']])
add_menu_item('Saturday', ["Avocado Watermelon Salad", ['vegetarian', 'veggies']])

add_menu_item('Thursday', ["Best Chicken Salad", ['salad', 'poultry']])
add_menu_item('Saturday', ["Beet Salad with Goat Cheese", ['salad', 'vegetarian']])

add_menu_item('Friday', ["Addictive Chocolate Truffles", ['dessert', 'chocolate']])
add_menu_item('Saturday', ["Raspberry Icebox Cake", ['dessert', 'fruit']])
add_menu_item('Sunday', ["Raspberry Ice-cream", ['dessert', 'fruit']])
add_menu_item('Monday', ["Chocolate ice-cream", ['dessert', 'chocolate']])
add_menu_item('Tuesday', ["Fresh fruit bowl", ['dessert', 'fruit']])
add_menu_item('Wednesday', ["American chocolate chip cookies", ['dessert', 'chocolate']])
add_menu_item('Thursday', ["Fruit mix ice-cream", ['dessert', 'fruit']])

print(menu_items)

# find menu items, available on a particular day and match with customer interests
def find_menu_items(week_day, interests):
    week_day_index = get_week_day_index(week_day)
    menu_items_on_week_day = menu_items[week_day_index]
    menu_items_matching_interest = []

    for menu_item in menu_items_on_week_day:
        # temp variable possible_menu_item
        possible_menu_item = menu_item
        menu_item_tags = menu_item[1]

        for interest in interests:
            if interest in menu_item_tags:
                menu_items_matching_interest.append(possible_menu_item[0])

    return menu_items_matching_interest

# test case: check if function call returns correct results
dessert = find_menu_items('Tuesday', ['dessert'])
friday_meal = find_menu_items('Friday', ['fish'])
veggies = find_menu_items('Monday', ['veggies'])
print(dessert)
print(friday_meal)
print(veggies)