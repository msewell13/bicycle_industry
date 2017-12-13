from bicycles import *

bikes = [Bicycle('BMX', 3, 150), Bicycle('Huffy', 8, 250), Bicycle('Schwinn', 10, 300),
Bicycle('Classic Flyer', 7, 75), Bicycle('Diamondback', 12, 400), Bicycle('Mongoose', 9, 350)]

customers = [Customers('Mark', 200), Customers('Chris', 500), Customers('Juan', 1000)]

shop = BikeShops('The Bike Shop', 20, bikes)


if __name__ == '__main__':
    