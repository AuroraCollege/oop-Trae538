class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
       return (self.year, self.model, self.make)

leonard = Car('Toyota','Corolla',2007)
print(leonard.display_info())