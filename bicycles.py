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


class Customers(object):
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
        
        
        