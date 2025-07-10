class vehicle:
    def navigate(self):
        pass
class car(vehicle):
    def navigate(self):
        print('navigate Car')
class truck(car):
    def navigate(self):
        print('navigate Truck')
v=truck()
v.navigate()
