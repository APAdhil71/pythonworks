class Car:
    name: str
    price:int
    colour:str
    brand:str

    def set_attributes(self,name,price,colour,brand):
        self.name=name
        self.price=price
        self.colour=colour
        self.brand=brand

    def display(self):
        print("car name:",self.name)
        print("price:",self.price)
        print("colour:",self.colour)
        print("brand:",self.brand)
        
car_instance1=Car()
car_instance1.set_attributes("bmw",300000,"black","bmw")
car_instance1.display()
