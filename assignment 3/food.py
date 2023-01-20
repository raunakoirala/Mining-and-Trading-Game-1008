from __future__ import annotations

from material import Material
from random_gen import RandomGen

# List of food names from https://github.com/vectorwing/FarmersDelight/tree/1.18.2/src/main/resources/assets/farmersdelight/textures/item
FOOD_NAMES = [
    "Apple Cider",
    "Apple Pie",
    "Apple Pie Slice",
    "Bacon",
    "Bacon And Eggs",
    "Bacon Sandwich",
    "Baked Cod Stew",
    "Barbecue Stick",
    "Beef Patty",
    "Beef Stew",
    "Cabbage",
    "Cabbage Leaf",
    "Cabbage Rolls",
    "Cabbage Seeds",
    "Cake Slice",
    "Chicken Cuts",
    "Chicken Sandwich",
    "Chicken Soup",
    "Chocolate Pie",
    "Chocolate Pie Slice",
    "Cod Slice",
    "Cooked Bacon",
    "Cooked Chicken Cuts",
    "Cooked Cod Slice",
    "Cooked Mutton Chops",
    "Cooked Rice",
    "Cooked Salmon Slice",
    "Dog Food",
    "Dumplings",
    "Egg Sandwich",
    "Fish Stew",
    "Fried Egg",
    "Fried Rice",
    "Fruit Salad",
    "Grilled Salmon",
    "Ham",
    "Hamburger",
    "Honey Cookie",
    "Honey Glazed Ham",
    "Honey Glazed Ham Block",
    "Horse Feed",
    "Hot Cocoa",
    "Melon Juice",
    "Melon Popsicle",
    "Milk Bottle",
    "Minced Beef",
    "Mixed Salad",
    "Mutton Chops",
    "Mutton Wrap",
    "Nether Salad",
    "Noodle Soup",
    "Onion",
    "Pasta With Meatballs",
    "Pasta With Mutton Chop",
    "Pie Crust",
    "Pumpkin Pie Slice",
    "Pumpkin Slice",
    "Pumpkin Soup",
    "Ratatouille",
    "Raw Pasta",
    "Rice",
    "Rice Panicle",
    "Roast Chicken",
    "Roast Chicken Block",
    "Roasted Mutton Chops",
    "Rotten Tomato",
    "Salmon Slice",
    "Shepherds Pie",
    "Shepherds Pie Block",
    "Smoked Ham",
    "Squid Ink Pasta",
    "Steak And Potatoes",
    "Stuffed Potato",
    "Stuffed Pumpkin",
    "Stuffed Pumpkin Block",
    "Sweet Berry Cheesecake",
    "Sweet Berry Cheesecake Slice",
    "Sweet Berry Cookie",
    "Tomato",
    "Tomato Sauce",
    "Tomato Seeds",
    "Vegetable Noodles",
    "Vegetable Soup",
]

class Food:
    
    def __init__(self, name: str, hunger_bars: int, price: int) -> None:
        """
        Initialises the constructor for Food

        Parameters:
                name(string): name of the food
                hunger_bars (int): amount of hunger bars it replenishes
                price (int): price of the food
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """

        self.name = name
        self.hunger_bars = hunger_bars
        self.price = price
    
    def __str__(self) -> str:
        """
        Returns the food details as a formatted string

        Returns:
                output (str): food name, hunger bars and price of the food

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        return f'({self.name},{self.hunger_bars},{self.price})'

    # Creates a Food type object with random parameters, range for price and hunger bars is 0 - 30 for both. 
    @classmethod
    def random_food(cls) -> Food:
        """
        Returns the food object randomly created

        Returns:
                Food

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """

        return Food(FOOD_NAMES[RandomGen.randint(0,len(FOOD_NAMES)-1)],RandomGen.randint(1,30),RandomGen.randint(1,30))

if __name__ == "__main__":
    for i in range(5):
        x = Food.random_food()
        print(x)
        print(type(x))
