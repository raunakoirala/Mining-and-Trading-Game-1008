from __future__ import annotations
from abc import abstractmethod

from player import Player
from trader import Trader
from material import Material
from cave import Cave
from food import Food
from random_gen import RandomGen
from hash_table import LinearProbeTable
from trader import HardTrader

class Game:

    MIN_MATERIALS = 5
    MAX_MATERIALS = 10

    MIN_CAVES = 5
    MAX_CAVES = 10

    MIN_TRADERS = 4
    MAX_TRADERS = 8

    MIN_FOOD = 2
    MAX_FOOD = 5

    @abstractmethod
    def __init__(self) -> None:
        """
        Instantiate the variable tables used to store data about the game

        Complexity: O(n) where n is the table size used
        """

        self.caves_table = LinearProbeTable(10)
        self.materials_table = LinearProbeTable(10)
        self.traders_table = LinearProbeTable(10)

    def initialise_game(self) -> None:
        """Initialise all game objects: Materials, Caves, Traders."""
        N_MATERIALS = RandomGen.randint(self.MIN_MATERIALS, self.MAX_MATERIALS)
        self.generate_random_materials(N_MATERIALS)
        print("Materials:\n\t", end="")
        print("\n\t".join(map(str, self.get_materials())))
        N_CAVES = RandomGen.randint(self.MIN_CAVES, self.MAX_CAVES)
        self.generate_random_caves(N_CAVES)
        print("Caves:\n\t", end="")
        print("\n\t".join(map(str, self.get_caves())))
        N_TRADERS = RandomGen.randint(self.MIN_TRADERS, self.MAX_TRADERS)
        self.generate_random_traders(N_TRADERS)
        print("Traders:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader]):
        self.set_materials(materials)
        self.set_caves(caves)
        self.set_traders(traders)

    def set_materials(self, mats: list[Material]) -> None:
        """
        Adds material objects to the hash table used to store them

        Inputs: List of material objects

        Returns: None

        Complextity: O(N) where N is the number of items added

        """
        for item in mats:
            self.materials_table[item.name] = item

    def set_caves(self, caves: list[Cave]) -> None:
        """
        Adds cave objects to the hash table used to store them

        Inputs: List of cave objects

        Returns: None

        Complextity: O(N) where N is the number of items added

        """
        for item in caves:
            self.caves_table[item.name] = item

    def set_traders(self, traders: list[Trader]) -> None:
        """
        Adds trader objects to the hash table used to store them

        Inputs: List of trader objects

        Returns: None

        Complextity: O(N) where N is the number of items added

        """
        for item in traders:
            self.traders_table[item.name] = item

    def get_materials(self) -> list[Material]:
        """
        Retreives all material items from the hash table

        Inputs: None

        Returns: List of material objects

        Complextity: O(S) where S is the size of the hash table

        """
        materials_list = []
        for item in self.materials_table.table:
            
            if item != None:
                materials_list.append(item[1])

        
        return materials_list

    def get_caves(self) -> list[Cave]:
        """
        Retreives all cave items from the hash table

        Inputs: None

        Returns: List of cave objects

        Complextity: O(S) where S is the size of the hash table

        """
        caves_list = []
        for item in self.caves_table.table:
            if item != None:
                caves_list.append(item[1])
        return caves_list

    def get_traders(self) -> list[Trader]:
        """
        Retreives all trader items from the hash table

        Inputs: None

        Returns: List of trader objects

        Complextity: O(S) where S is the size of the hash table

        """

        traders_list = []
        for item in self.traders_table.table:
            if item != None:
                traders_list.append(item[1])
        return traders_list

    def generate_random_materials(self, amount):
        """
        Generates <amount> random materials using Material.random_material
        Generated materials must all have different names and different mining_rates.
        (You may have to call Material.random_material more than <amount> times.)
        """
        table = LinearProbeTable(amount)
        
        while table.count < amount:
            material = Material.random_material()
            table[material.name] = material
            
        self.materials_table = table

    def generate_random_caves(self, amount):
        """
        Generates <amount> random caves using Cave.random_cave
        Generated caves must all have different names
        (You may have to call Cave.random_cave more than <amount> times.)
        """

        table = LinearProbeTable(amount)
        materials = self.get_materials()
        while table.count < amount:
            cave = Cave.random_cave(materials)
            table[cave.name] = cave
            
        self.caves_table = table

    def generate_random_traders(self, amount):
        """
        Generates <amount> random traders by selecting a random trader class
        and then calling <TraderClass>.random_trader()
        and then calling set_all_materials with some subset of the already generated materials.
        Generated traders must all have different names
        (You may have to call <TraderClass>.random_trader() more than <amount> times.)
        """
        table = LinearProbeTable(amount)
        materials_list = self.get_materials()
        while table.count < amount:
            trader = HardTrader("jeff")
            trader = trader.random_trader()
            materials_to_include = []
            for item in materials_list:
                if RandomGen.random_chance(0.5):
                    materials_to_include.append(item)
            trader.set_all_materials(materials_to_include)
            table[trader.name] = trader
        self.traders_table = table

    def finish_day(self):
        """
        DO NOT CHANGE
        Affects test results.
        """
        for cave in self.get_caves():
            if cave.quantity > 0 and RandomGen.random_chance(0.2):
                cave.remove_quantity(RandomGen.random_float() * cave.quantity)
            else:
                cave.add_quantity(round(RandomGen.random_float() * 10, 2))
            cave.quantity = round(cave.quantity, 2)

class SoloGame(Game):

    def initialise_game(self) -> None:
        super().initialise_game()
        self.player = Player.random_player()
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        super().initialise_with_data(materials, caves, traders)
        self.player = Player(player_names[0], emeralds=emerald_info[0])
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def simulate_day(self):
        # 1. Traders make deals
        for trader in self.get_traders():
            trader.generate_deal()

        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        food_num = RandomGen.randint(self.MIN_FOOD, self.MAX_FOOD)
        foods = []
        for _ in range(food_num):
            foods.append(Food.random_food())
        print("\nFoods:\n\t", end="")
        print("\n\t".join(map(str, foods)))
        self.player.set_foods(foods)
        # 3. Select one food item to purchase
        food, balance, caves = self.player.select_food_and_caves()
        print(food, balance, caves)
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(food, balance, caves)

    def verify_output_and_update_quantities(self, food: Food | None, balance: float, caves: list[tuple[Cave, float]]) -> None:
        """
        Retreives all material items from the hash table

        Inputs:
            Food: a food item
            Balance: a float
            Caves: a list of tuples of a cave object and a float

        Returns: None

        Complextity: O(T * C) T = number of traders, C = number of caves visited

        """

        #verify food purchasable
        assert food in self.player.foods_list or food == None, 'Food not purchasable'

        #verify quantity of materials mined are possible
        for item in caves:
            assert (item[0].quantity- item[1]) >= -0.0001, 'Player mined more then possible from a cave'

        #verify that materials can be sold
        for item in caves:
            found_item = False
            for trader in self.get_traders():
                if trader.deal[0] == item[0].material:
                    found_item = True
            assert found_item, 'Material mined cannot be sold'
        
        #verify more or equal emeralds then the starting value
        assert self.player.balance <= balance, 'Finished with less emeralds then started with'


        #update quantities
        for cave_visited in caves:
            cave_visited[0].remove_quantity(cave_visited[1])

        self.player.balance = balance






class MultiplayerGame(Game):

    MIN_PLAYERS = 2
    MAX_PLAYERS = 5

    def __init__(self) -> None:
        super().__init__()
        self.players = []

    def initialise_game(self) -> None:
        super().initialise_game()
        N_PLAYERS = RandomGen.randint(self.MIN_PLAYERS, self.MAX_PLAYERS)
        self.generate_random_players(N_PLAYERS)
        for player in self.players:
            player.set_materials(self.get_materials())
            player.set_caves(self.get_caves())
            player.set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def generate_random_players(self, amount) -> None:
        for _ in range(amount):
            self.players.append(Player.random_player())


    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        super().initialise_with_data(materials, caves, traders)
        for player, emerald in zip(player_names, emerald_info):
            self.players.append(Player(player, emeralds=emerald))
            self.players[-1].set_materials(self.get_materials())
            self.players[-1].set_caves(self.get_caves())
            self.players[-1].set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def simulate_day(self):
        # 1. Traders make deals
        for trader in self.get_traders():
            trader.generate_deal()

        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        offered_food = Food.random_food()
        print(f"\nFoods:\n\t{offered_food}")
        # 3. Each player selects a cave - The game does this instead.
        foods, balances, caves = self.select_for_players(offered_food)

        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(foods, balances, caves)

    def select_for_players(self, food: Food) -> tuple[list[Food|None], list[float], list[tuple[Cave, float]|None]]:
        """
        Calculates the best option for an amount of players

        Inputs:
            Food: a food object

        Returns:
            Tuple: A tuple containing:
                A list of food objects of None
                A list of floats
                A list of tuples containing a cave object and a float

        Complexity: O(C * T + P)
            C = Number of caves
            T = Number of traders
            P = Number of players

        
        This algorithm finds the caves that have materials that can be sold to traders, then calculates
        the net gain or loss from buying the available food and going to each cave. Then sorts the net
        gains and each player takes the best cave that hasnt already been taken, unless its a loss to do
        so then they dont go to any cave and dont buy any food.
        """
        hungerAvailable = food.hunger_bars

        #find the items being bought by traders
        items_sold = []
        for trader in self.players[0].traders_list:
            deal = trader.deal
            if deal != None:
                items_sold.append(deal)

        #finds the items that can be sold and are in caves
        for item in items_sold:
            item_in = False
            for cave in self.players[0].caves_list:
                if item[0] == cave.material:
                    item_in = True
            if not item_in:
                items_sold.remove(item)

        #calculates the expected profit or loss from each cave
        caves_with_value = []
        for cave in self.players[0].caves_list:
            mat_available = False
            for item in items_sold:
                if cave.material == item[0]:
                    mat_available = True
            if mat_available:
                item_price = 0
                for item in items_sold:
                    if item[0] == cave.material and item[1] > item_price:
                        item_price = item[1]
                cave_value = min((hungerAvailable/cave.material.mining_rate),cave.quantity)*item_price - food.price
                caves_with_value.append((cave,cave_value))
        
        #sorts the caves by their profit
        n = len(caves_with_value)
        for mark in range(1,n):
            temp = caves_with_value[mark]
            i = mark - 1
            while i >= 0 and caves_with_value[i][1] > temp[1]:
                caves_with_value[i+1] = caves_with_value[i]
                i -= 1
            caves_with_value[i+1] = temp
        caves_with_value = caves_with_value[::-1]


        #selects the option for each player and adds it to the return tuple
        food_return = []
        em_return = []
        caves_return = []
        for index in range(len(self.players)):
            
            if index < len(caves_with_value) and caves_with_value[index][1] > 0:
                food_return.append(Food)
                em_return.append(self.players[index].balance + caves_with_value[index][1])

                caves_return.append((caves_with_value[index][0],min(hungerAvailable/caves_with_value[index][0].material.mining_rate,caves_with_value[index][0].quantity)))
            else:
                food_return.append(None)
                em_return.append(self.players[index].balance)
                caves_return.append(None)
        return (food_return,em_return,caves_return)




        

    def verify_output_and_update_quantities(self, foods: list[Food | None], balances: list[float], caves: list[tuple[Cave, float]|None]) -> None:
        """
        Verifies the outputs of select_for_players

        Inputs:
            A list of food objects of None
            A list of floats
            A list of tuples containing a cave object and a float

        Returns:
            None

        Complexity: O(F * C)
            F = number of foods
            C = number of caves

        """


        for index in range(len(foods)):

            #verify quantity of materials mined are possible
            for item in caves:
                if item != None:
                    assert (item[0].quantity- item[1]) >= -0.0001, 'Player mined more then possible from a cave'

            #verify that materials can be sold
            for item in caves:
                if item != None:
                    found_item = False
                    for trader in self.get_traders():
                        if trader.deal[0] == item[0].material:
                            found_item = True
                    assert found_item, 'Material mined cannot be sold'
            
            #verify more or equal emeralds then the starting value
            assert self.players[index].balance <= balances[index], 'Finished with less emeralds then started with'

if __name__ == "__main__":
    game = MultiplayerGame()
    game.initialise_game()
    game.simulate_day()
    



    """
    game = Game()
    game.generate_random_materials(5)
    game.generate_random_traders(5)
    print(game.traders_table)
    for item in game.get_traders():
        print("NAME" ,item.name)
        for n in item.inventory:
            print(n)
        


    r = RandomGen.seed # Change this to set a fixed seed.
    RandomGen.set_seed(r)
    print(r)

    g = SoloGame()
    g.initialise_game()

    g.simulate_day()
    g.finish_day()

    g.simulate_day()
    g.finish_day()
    """