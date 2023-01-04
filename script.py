# list days of the week
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# keywords used in menu items selection
# meat, poultry, fish, seafood, vegetarian, dessert
# define test customer: name, day, selection criteria
test_customer = ['Anna Wild', 'Monday', ['vegetarian', 'dessert']]

# get index of menu day
def get_day_index(day):
    day_index = week_days.index(day)
    return day_index

# test case 1: get index of week_days(day)
# print(get_day_index('Wednesday'))

# get customer current day
def get_customer_current_day(customer):
    current_day = customer[1]
    current_day_index = get_day_index(current_day)
    return current_day_index

# test case 2: check if customer's current day matches the week_days index
# test_current_day_index = get_customer_current_day(test_customer)
# print(test_current_day_index)





