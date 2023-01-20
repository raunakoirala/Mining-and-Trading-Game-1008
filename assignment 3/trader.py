from __future__ import annotations

from abc import abstractmethod, ABC
from material import Material
from random_gen import RandomGen

# Generated with https://www.namegenerator.co/real-names/english-name-generator
TRADER_NAMES = [
    "Pierce Hodge",
    "Loren Calhoun",
    "Janie Meyers",
    "Ivey Hudson",
    "Rae Vincent",
    "Bertie Combs",
    "Brooks Mclaughlin",
    "Lea Carpenter",
    "Charlie Kidd",
    "Emil Huffman",
    "Letitia Roach",
    "Roger Mathis",
    "Allie Graham",
    "Stanton Harrell",
    "Bert Shepherd",
    "Orson Hoover",
    "Lyle Randall",
    "Jo Gillespie",
    "Audie Burnett",
    "Curtis Dougherty",
    "Bernard Frost",
    "Jeffie Hensley",
    "Rene Shea",
    "Milo Chaney",
    "Buck Pierce",
    "Drew Flynn",
    "Ruby Cameron",
    "Collie Flowers",
    "Waldo Morgan",
    "Winston York",
    "Dollie Dickson",
    "Etha Morse",
    "Dana Rowland",
    "Eda Ryan",
    "Audrey Cobb",
    "Madison Fitzpatrick",
    "Gardner Pearson",
    "Effie Sheppard",
    "Katherine Mercer",
    "Dorsey Hansen",
    "Taylor Blackburn",
    "Mable Hodge",
    "Winnie French",
    "Troy Bartlett",
    "Maye Cummings",
    "Charley Hayes",
    "Berta White",
    "Ivey Mclean",
    "Joanna Ford",
    "Florence Cooley",
    "Vivian Stephens",
    "Callie Barron",
    "Tina Middleton",
    "Linda Glenn",
    "Loren Mcdaniel",
    "Ruby Goodman",
    "Ray Dodson",
    "Jo Bass",
    "Cora Kramer",
    "Taylor Schultz",
]

class Trader(ABC):
    
    def __init__(self, name: str) -> None:
        """
        Initialises the constructor for Trader

        Parameters:
                name(string): name of the trader
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """

        self.name = name
        self.inventory = []
        self.deal = None
        
    @classmethod
    def random_trader(cls):
        """
        Returns the trader randomly created

        Returns:
                Trader

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """

        tradertype = RandomGen.randint(1,3)
        if tradertype == 1:
            return RandomTrader(TRADER_NAMES[RandomGen.randint(0,len(TRADER_NAMES)-1)])
        if tradertype == 2:
            return RangeTrader(TRADER_NAMES[RandomGen.randint(0,len(TRADER_NAMES)-1)])
        if tradertype == 3:
            return HardTrader(TRADER_NAMES[RandomGen.randint(0,len(TRADER_NAMES)-1)])
            
    def set_all_materials(self, mats: list[Material]) -> None:
        self.inventory = mats
    
    def add_material(self, mat: Material) -> None:
        """
        Adds the materials to the trader inventory

        Parameters:
                mat(Material): material to be added
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        self.inventory.append(mat)
    
    def is_currently_selling(self) -> bool:
        """
        Determines if the trader is currently selling

        Returns:
                true or false based on if they're currently selling

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        return not self.deal == None

    def current_deal(self) -> tuple[Material, float]:
        """
        Gets the current deal and the material for trader

        Returns:
                deal(tuple): returns deal

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        if self.deal == None:
            raise ValueError
        return self.deal
    
    @abstractmethod
    def generate_deal(self) -> None:
        """
        ABSTRACT METHOD
        """
        raise NotImplementedError()

    def stop_deal(self) -> None:
        """
        Stops the current deal for the trader

        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        self.deal = None
    
    def __str__(self) -> str:
        """
        Returns the trader details as a formatted string

        Returns:
                output(str): trader name and deal

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        dealString = 'No current deal'
        if self.deal != None:
            dealString = f"buying [{self.deal[0].name}: {self.deal[0].mining_rate}🍗/💎] for {self.deal[1]}💰"
        return f"<{self.__name__()}: {self.name} {dealString}>"

    def sort_inventory(self):
        list = self.inventory
        n = len(list)
        for mark in range(1,n):
            temp = list[mark]
            i = mark - 1
            while i >= 0 and list[i].mining_rate > temp.mining_rate:
                list[i+1] = list[i]
                i -= 1
            list[i+1] = temp
        return list

class RandomTrader(Trader):

    def __name__(self):
        """
        Returns random trader name
        """
        return str("RandomTrader")

    def generate_deal(self) -> None:
        """
        Creates and sets a random deal using a random material and a random buy price

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        if len(self.inventory) > 0:
            item = self.inventory[RandomGen.randint(0,len(self.inventory)-1)]
            price =  round(2 + 8 * RandomGen.random_float(), 2)
            self.deal = (item,price)
 
class RangeTrader(Trader):

    def __name__(self):
        """
        Returns range trader name
        """
        return str("RangeTrader")

    def generate_deal(self) -> None:
        """
        Creates and sets a deal by generating a list of all materials which are easy to mine, choose a random material and buy price

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        n = self.sort_inventory()
        if len(self.inventory) > 0:
            i = RandomGen.randint(0, len(self.inventory)-1)
            j = RandomGen.randint(i, len(self.inventory)-1)
            materialsInRange = n[i:j+1]
            item = materialsInRange[RandomGen.randint(0,max(len(materialsInRange)-1,0))]
            price =  round(2 + 8 * RandomGen.random_float(), 2)
            self.deal = (item,price)
   
    def materials_between(self, i: int, j: int) -> list[Material]:
        """
        Gets a list containing the materials which are somewhere between the ith and jth easiest to mine

        Parameters:
                i(int): ith easiest element to mine
                j(int): jth easiest element to mine
        Returns:
                inventory list of materials

        Worst case complexity:
        Best Case complexity:
        """
        self.sort_inventory() #idk what we're doing to sort the list by mining difficulty
        return self.inventory[i:j+1]


class HardTrader(Trader):
    
    def __name__(self):
        """
        Returns hard trader name
        """
        return str("HardTrader")

    def generate_deal(self) -> None:
        if len(self.inventory) > 0:
            price =  round(2 + 8 * RandomGen.random_float(), 2)
            self.sort_inventory()
            item = (self.inventory)[-1]
            self.deal = (item,price)
        else:
            return None
    
    pass

if __name__ == "__main__":
    trader = RangeTrader("Jackson")
    print(trader)
    trader.set_all_materials([
        Material("Coal", 4.5),
        Material("Diamonds", 3),
        Material("Redstone", 20),
        Material("test",234),
        Material("test2",1)
    ])

    trader.sort_inventory()
    for i in trader.inventory:
        print(i.mining_rate)


