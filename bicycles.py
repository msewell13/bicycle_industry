class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __repr__(self):
        return "The bike model '{0}' weighs {1} lbs. and costs ${2} wholesale.".format(
            self.model, self.weight, self.cost)


class BikeShop(object):
    def __init__(self, shop_name, margin, inventory):
        self.shop_name = shop_name
        self.margin = margin
        self.inventory = inventory
        
        
        # self.profit = 0
        # init_inv = [('BMX', 3, 150), ('Huffy', 8, 250)]
        # if inventory == None:
        #     self.inventory = []
        # for item in init_inv:
        #     self.inventory.append(super(BikeShop, self).__init__(item[0], item[1], item[2]))
        
        # for bike in init_inv:
        #     print(bike)
        #     # bike.cost = bike[2]
        #     # bike.markup = bike.cost * self.margin / 100
        #     # bike.price = bike.cost + bike.markup


# Have an inventory of different bicycles
# Sell bicycles with a margin over their cost
# Can see how much profit they have made from selling bikes


class Customers(BikeShop):
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        
    def __repr__(self):
        return "{0} has ${1} available to buy a bicycle".format(
            self.name, self.funds)
    
    def bicycle(self, bike_name, retail_cost):
        self.bike_name = bike_name
        self.retail_cost = retail_cost
        self.funds = self.funds - self.retail_cost
            
            
            
            # print("Sorry {0}, you're too poor for this bicycle"format(self.name))
        
        
        