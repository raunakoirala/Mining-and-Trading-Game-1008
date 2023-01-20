
from random_gen import RandomGen

# Material names taken from https://minecraft-archive.fandom.com/wiki/Items
RANDOM_MATERIAL_NAMES = [
    "Arrow",
    "Axe",
    "Bow",
    "Bucket",
    "Carrot on a Stick",
    "Clock",
    "Compass",
    "Crossbow",
    "Exploration Map",
    "Fire Charge",
    "Fishing Rod",
    "Flint and Steel",
    "Glass Bottle",
    "Dragon's Breath",
    "Hoe",
    "Lead",
    "Map",
    "Pickaxe",
    "Shears",
    "Shield",
    "Shovel",
    "Sword",
    "Saddle",
    "Spyglass",
    "Totem of Undying",
    "Blaze Powder",
    "Blaze Rod",
    "Bone",
    "Bone meal",
    "Book",
    "Book and Quill",
    "Enchanted Book",
    "Bowl",
    "Brick",
    "Clay",
    "Coal",
    "Charcoal",
    "Cocoa Beans",
    "Copper Ingot",
    "Diamond",
    "Dyes",
    "Ender Pearl",
    "Eye of Ender",
    "Feather",
    "Spider Eye",
    "Fermented Spider Eye",
    "Flint",
    "Ghast Tear",
    "Glistering Melon",
    "Glowstone Dust",
    "Gold Ingot",
    "Gold Nugget",
    "Gunpowder",
    "Ink Sac",
    "Iron Ingot",
    "Iron Nugget",
    "Lapis Lazuli",
    "Leather",
    "Magma Cream",
    "Music Disc",
    "Name Tag",
    "Nether Bricks",
    "Paper",
    "Popped Chorus Fruit",
    "Prismarine Crystal",
    "Prismarine Shard",
    "Rabbit's Foot",
    "Rabbit Hide",
    "Redstone",
    "Seeds",
    "Beetroot Seeds",
    "Nether Wart Seeds",
    "Pumpkin Seeds",
    "Wheat Seeds",
    "Slimeball",
    "Snowball",
    "Spawn Egg",
    "Stick",
    "String",
    "Wheat",
    "Netherite Ingot",
]

class Material:
    """
        Creates a material with a name and mining rate 
            Name is used to identify the material
            Mining rate is amount of hunger needed to mine 

            Name and mining rate are either input or chosen at random

    """
    
    def __init__(self, name: str, mining_rate: float) -> None:
        """
        Initialises the constructor for Material

        Parameters:
                name(string): name of the material
                mining_rate (float): rate of mining within the cave
        Returns:
                None

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """

        self.name = name
        self.mining_rate = mining_rate
    
    def __str__(self) -> str:
        """
        Returns the material details as a formatted string

        Returns:
                output (str): material name and mining rate

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        return f'({self.name},{self.mining_rate})'
        
    # Just chose 30 to be the max hunger cost cuase i dont know what else
    # feels like we need something to determine the hunger cost based on the material cause harder materials like iron should take more to mine than wheat
    @classmethod
    def random_material(cls):
        """
        Returns the material randomly created

        Returns:
                Material

        Worst case complexity: O(1)
        Best Case complexity: O(1)
        """
        return Material(RANDOM_MATERIAL_NAMES[RandomGen.randint(0,len(RANDOM_MATERIAL_NAMES)-1)],RandomGen.randint(1,30))

if __name__ == "__main__":
    print(Material("Coal", 4.5))
    print(Material.random_material())

