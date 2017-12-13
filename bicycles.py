class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class BikeShops(Bicycle):
    def __init__(self, name, margin, bikes):
        self.name = name
        self.margin = margin
        self.profit = 0
        self.inventory = {}
            
    def sell_bike(self, margin, model, cost):
        
        cost * margin / 100
        # update inventory
        
    def profit(self):
        pass


# Have an inventory of different bicycles
# Sell bicycles with a margin over their cost
# Can see how much profit they have made from selling bikes


class Customers(BikeShops):
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
    
    def buy_bicycle(self, model, weight, cost):
        if cost <= self.funds:
            super(Customers, self).__init__(model, weight, cost)
            self.funds = self.funds - cost
        else:
            print("Sorry {0}, you're too poor for this bicycle".format(self.name))
        
        
        
# Shop should have 6 different bicycles in stock
# 3 customers with the following budgets 200, 500, 1000