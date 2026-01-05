class Mobile:
    title : str
    price : int
    brand : str
    feature : str 
    def __init__(self,title,price,brand,feature):
        self.title=title
        self.price=price
        self.brand=brand
        self.feature=feature
    def display(self):
        print(f"title:{self.title} brand{self.brand} price{self.price} feature{self.feature}")
mob_instance1=Mobile("mv","redmi",23000,"dhjd")
mob_instance1.display()