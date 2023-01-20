from __future__ import annotations

from cave import Cave
from material import Material
from random_gen import RandomGen
from trader import RandomTrader, Trader
from food import Food

# List taken from https://minecraft.fandom.com/wiki/Mob
PLAYER_NAMES = [
    "Steve",
    "Alex",
    "ɘᴎiɿdoɿɘH",
    "Allay",
    "Axolotl",
    "Bat",
    "Cat",
    "Chicken",
    "Cod",
    "Cow",
    "Donkey",
    "Fox",
    "Frog",
    "Glow Squid",
    "Horse",
    "Mooshroom",
    "Mule",
    "Ocelot",
    "Parrot",
    "Pig",
    "Pufferfish",
    "Rabbit",
    "Salmon",
    "Sheep",
    "Skeleton Horse",
    "Snow Golem",
    "Squid",
    "Strider",
    "Tadpole",
    "Tropical Fish",
    "Turtle",
    "Villager",
    "Wandering Trader",
    "Bee",
    "Cave Spider",
    "Dolphin",
    "Enderman",
    "Goat",
    "Iron Golem",
    "Llama",
    "Panda",
    "Piglin",
    "Polar Bear",
    "Spider",
    "Trader Llama",
    "Wolf",
    "Zombified Piglin",
    "Blaze",
    "Chicken Jockey",
    "Creeper",
    "Drowned",
    "Elder Guardian",
    "Endermite",
    "Evoker",
    "Ghast",
    "Guardian",
    "Hoglin",
    "Husk",
    "Magma Cube",
    "Phantom",
    "Piglin Brute",
    "Pillager",
    "Ravager",
    "Shulker",
    "Silverfish",
    "Skeleton",
    "Skeleton Horseman",
    "Slime",
    "Spider Jockey",
    "Stray",
    "Vex",
    "Vindicator",
    "Warden",
    "Witch",
    "Wither Skeleton",
    "Zoglin",
    "Zombie",
    "Zombie Villager",
    "H̴͉͙̠̥̹͕͌̋͐e̸̢̧̟͈͍̝̮̹̰͒̀͌̈̆r̶̪̜͙̗̠̱̲̔̊̎͊̑̑̚o̷̧̮̙̗̖̦̠̺̞̾̓͆͛̅̉̽͘͜͝b̸̨̛̟̪̮̹̿́̒́̀͋̂̎̕͜r̸͖͈͚̞͙̯̲̬̗̅̇̑͒͑ͅi̶̜̓̍̀̑n̴͍̻̘͖̥̩͊̅͒̏̾̄͘͝͝ę̶̥̺̙̰̻̹̓̊̂̈́̆́̕͘͝͝"
]

class Player():

    DEFAULT_EMERALDS = 50

    MIN_EMERALDS = 14
    MAX_EMERALDS = 40

    def __init__(self, name, emeralds=None) -> None:
        """
        Initialises the constructor for Player

        Parameters:
                name(string): name of the player
                emeralds (int): amount of emeralds player has
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """

        self.name = name

        self.balance = self.DEFAULT_EMERALDS if emeralds is None else emeralds

    def set_traders(self, traders_list: list[Trader]) -> None:
        """
        Sets the traders for the player

        Parameters:
                traders_list(list): list of traders
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        self.traders_list = traders_list

    def set_foods(self, foods_list: list[Food]) -> None:
        """
        Sets the food for the player

        Parameters:
                foods_list(list): list of food
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        self.foods_list = foods_list

    @classmethod
    def random_player(cls) -> Player:
        """
        Returns the Player randomly created

        Returns:
                Player

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        return Player(PLAYER_NAMES[RandomGen.randint(0, len(PLAYER_NAMES)-1)], RandomGen.randint(14, 40))

    def set_materials(self, materials_list: list[Material]) -> None:
        """
        Sets the materials for the player

        Parameters:
                materials_list(list): list of materials
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        self.materials_list = materials_list

    def set_caves(self, caves_list: list[Cave]) -> None:
        """
        Sets the caves for the player

        Parameters:
                caves_list(list): list of caves
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        self.caves_list = caves_list

    def select_food_and_caves(self) -> tuple[Food | None, float, list[tuple[Cave, float]]]:


        """
        Method:
            This aproach calculates the most efficent materials to mine each day based on their mining rate and
            their sell price. Then orders the materials by their efficency. 
            Then it loops through each food item and calculates the max gain from mining the materials in order from
            most to least efficent, and stores the best food and cave combination to do so.

        Example:
            Given an example with three traders, three foods, and three caves. The method extracts the materials available
            and calculates their efficencies. For example a result could look like:
            [('Eye of ender', 0.58) , ('Blaze Rod', 0.79) , ('Glass Bottle', 2.86)], where the float is the hunger required to
            gain one emerald of value. This means that the Eye of ender is the most efficent material to go for as it generates
            the most profit for the least hunger used.

            The algorithm then checks the hunger gained from each food and calculates how much can be mined, prefering the most
            efficent materials first. In this case any caves with Eyes of ender would be mined first, and if any hunger remained
            then the Blaze Rods, and finally the Glass Bottles. Mining the materials in order of efficency ensures that the maximum
            emerald gain is achieved


        Inputs: None
        
        Returns: A tuple containing:
            A food objects
            A floats
            A list of tuples containing a cave object and a float

        O(M + T + F * C )
        """

        #Finds the items that can be sold to traders
        # O(T)
        items_sold = []
        for trader in self.traders_list:
            deal = trader.deal
            if deal != None:
                items_sold.append(deal)

        #Find the items that are sellable and in caves
        # O(C)
        for item in items_sold:
            item_in = False
            for cave in self.caves_list:
                if item[0] == cave.material:
                    item_in = True
            if not item_in:
                items_sold.remove(item)

        #Find the hunger required to get one emerald of value from each material
        # O(T)
        hunger_per_em = []
        for item in items_sold:
            hunger_per_em.append(((item[0],(item[1]/item[0].mining_rate))))

        #Sort the materials by the emeralds per hunger
        # O(T**2)
        n = len(hunger_per_em)
        for mark in range(1,n):
            temp = hunger_per_em[mark]
            i = mark - 1
            while i >= 0 and hunger_per_em[i][1] > temp[1]:
                hunger_per_em[i+1] = hunger_per_em[i]
                i -= 1
            hunger_per_em[i+1] = temp
        hunger_per_em = hunger_per_em[::-1]


        #For each food, calculate the best outcome from using all hunger, or mining the best materials in order
        #Calculates the best food by comparing the results from each food.
        # O(F * C)
        return_tuple = (None,self.balance,[])
        max_ending_emeralds = self.balance

        #iterate though each food available
        for food in self.foods_list:
            if food.price > self.balance:
                continue
            ending_emeralds = self.balance - food.price
            hunger = food.hunger_bars
            temp_em_list = hunger_per_em[:]

            #while the player still has hunger, keep visiting caves
            while hunger > 0 and len(temp_em_list) > 0:
                material_to_mine = temp_em_list[0]
                temp_em_list.remove(material_to_mine)
                caves_visited = []

                #Visit and mine each cave with the next most efficent matierial to mine and calculate total gain
                for cave in self.caves_list:
                    if cave.material == material_to_mine[0]:
                        max_mine = hunger/material_to_mine[0].mining_rate
                        actual_mined = min(max_mine,cave.quantity)
                        hunger_used = actual_mined * material_to_mine[0].mining_rate
                        ending_emeralds += hunger_used * material_to_mine[1]
                        hunger -= hunger_used
                        caves_visited.append((cave,actual_mined))

            #if the total gain is the best so far, store it and save what occured to get it
            if ending_emeralds > max_ending_emeralds:
                max_ending_emeralds = ending_emeralds
                return_tuple = (food,max_ending_emeralds,caves_visited)
        
        return return_tuple




        
    def __str__(self) -> str:
        """
        Returns the player details as a formatted string

        Returns:
                output (str): player name and balance

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        return f'{self.name}, {str(self.balance)}'


if __name__ == "__main__":
    a = Player('bob',30)