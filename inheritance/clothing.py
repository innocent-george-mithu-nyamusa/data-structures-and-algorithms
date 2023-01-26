class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
        
    def change_price(self, price):
        self.price = price
        
    def calculate_discount(self, discount):
        return self.price * (1 - discount)
    
    def calculate_shipping(self, weight, rate):
        """
        Args:
            weight (float)
            rate (float)
            
        Attributes:
            weight representing the weight of the article of clothing
            rate representing the shipping weight
            
        return:
            weight * rate
        """
        self.weight = weight
        self.rate = rate
        return self.weight * self.rate
    

class Shirt(Clothing):
    
    def __init__(self, color, size, style, price, long_or_short):
        
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short
    
    def double_price(self):
        self.price = 2*self.price
    
class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):
        
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist
        
    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)
    
class Blouse(Clothing):
    """the Blouse class creates blouses clothing"""
    
    def __init__(self, color, size, style, price, country_of_origin):
        
        """
        initilaizes Blouse class
        
        Args:
            color (str)
            size (int)
            style (str)
            price (int)
            country_of_origin (str)
            
        Attributes:
            color: color of the blouse
            size: size of the blouse
            style: style of blouse 
            price: price of the blouse
            country_of_origin: country of origin for blouse 
        """
        self.country_of_origin = country_of_origin
        
    def triple_price(self):
        return self.price * 3
    
    