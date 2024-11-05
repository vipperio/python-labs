class Printer:  


    def __init__(self, name: str = "Printer", speed: int = 30, price: float = 3700.00, version: str = "Default", capacity: int = 2):
        self.__name = name
        self.__speed = speed 
        self.__price = price  
        self.version = version
        self.capacity = capacity

    def get_name(self):
        return self.__name
        
    def get_speed(self):
        return self.__speed
    
    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Printer(Name: {self.__name}, Speed: {self.__speed}, Price: {self.__price}, Version: {self.version}, Capacity: {self.capacity})"

    def __repr__(self):
         return f'Printer("{self.__name}", {self.__speed}, {self.__price}, "{self.version}", {self.capacity})'

    def __del__ (self):
        print("Deleting an object")

def main():
    epson = Printer("Epson", 12, 2500.00, "L355", 1)
    canon = Printer("Canon", 50, 7900.00, "M12", 5 )
    samsung = Printer("Samsung", 24, 4590.00, "L77-1", 3 )

    print(repr(epson))
    print(repr(canon))
    print(repr(samsung))

main()
