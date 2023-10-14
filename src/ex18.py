"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(amount, price):
    free = amount//9
    paid = amount-free
    return paid*price
    pass

def get_cost_of_coffee_2(count, price):
    free = count//9
    paid = count-free
    return paid*price
    pass
