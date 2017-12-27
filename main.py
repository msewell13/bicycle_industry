from bicycles import *
import random

bikes = [Bicycle('BMX', 3, 150), Bicycle('Huffy', 8, 250), Bicycle('Schwinn', 10, 300),
Bicycle('Classic Flyer', 7, 75), Bicycle('Diamondback', 12, 400), Bicycle('Mongoose', 9, 350)]


# Create three customers. One customer has a budget of $200, the second $500, 
# and the third $1000.
customers = [Customers('Mark', 200), Customers('Chris', 500), Customers('Juan', 1000)]


# Create a bicycle shop that has 6 different bicycle models in stock. The shop 
# should charge its customers 20% over the cost of the bikes.
shop = BikeShop('The Bike Shop', 20, bikes)


# Print the initial inventory of the bike shop for each bike it carries.
print("\n welcome to {}. Here is a list of our current inventory:\n".format(shop.shop_name))
for item in shop.inventory:
    print(item)


# Print the name of each customer, and a list of the bikes offered by the bike 
# shop that they can afford given their budget. Make sure you price the bikes in 
# such a way that each customer can afford at least one.
for customer in customers:
    print('\n')
    print(customer, 'and can afford the following bikes:')
    for bike in shop.inventory:
        retail_price = int(bike.cost + (bike.cost * shop.margin / 100))
        if retail_price <= customer.funds:
            print('{0}: ${1}'.format(bike.model, retail_price))


#Have each of the three customers purchase a bike then print the name 
# of the bike the customer purchased, the cost, and how much money they 
# have left over in their bicycle fund.
for customer in customers:
    choose_bike = random.choice(shop.inventory)
    retail_price = int(choose_bike.cost + (choose_bike.cost * shop.margin / 100))
    while retail_price > customer.funds:
        choose_bike = random.choice(shop.inventory)
        retail_price = int(choose_bike.cost + (choose_bike.cost * shop.margin / 100))
    bike_purchase = customer.bicycle(choose_bike.model, retail_price)
    print("\n{0} purchased a {1} for ${2}".format(customer.name, 
    choose_bike.model, retail_price))
    print("{0} has ${1} remaining in their bike fund\n".format(customer.name, customer.funds))
    shop.inventory.remove(choose_bike)
    
    # After each customer has purchased their bike, the script should print out 
    # the bicycle shop's remaining inventory for each bike, and how much profit 
    # they have made selling the three bikes.
    print("\n Remaining inventory:")
    for bike in shop.inventory:
        print(bike)
    print("\n {0} has made a profit of {1}".format(shop.shop_name, retail_price - choose_bike.cost))
    
        
        

