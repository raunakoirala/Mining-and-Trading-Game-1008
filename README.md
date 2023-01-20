# Mining-and-Trading-Game-1008

#Quick Background 

After some hard fought pokemon battles, you find yourself transported to a world made of
differently-textured cubes, and your arms feel so strong you could punch a tree. It seems
you’ve been transported to some other game, where you can Mine blocks and Craft items, I
forget the name of it.

The game contains long-nosed characters called Traders, which trade certain materials with
you for emeralds. You’d love to get as many emeralds as possible, so you set off on an
adventure to collect materials to sell to these Traders. However! The materials all take
hunger (and therefore food) to collect, and so you need to choose your materials wisely!

Materials
A Material has two bits of important information:
● Name: Used to identify the material
● Mining Rate: Specifies how many hunger points are needed to mine a single unit of
the material (can be a fractional number)

Caves
A Cave is where we can mine materials. A cave has three bits of important information:
● Name: Used to identify the cave
● Material: The material stored within this cave. Each cave houses exactly 1 material
● Quantity: The amount of the material which is currently mineable in the cave.

Trader
A Trader will only ever buy 1 material at a time, this material changes day by day. The way in
which the Trader selects this material, and how many emeralds they are willing to buy it for,
is covered in more detail later in the assessment. Traders have a name and type, which
again will be talked about more later.

Food
Food has three properties:
● Name: Used to identify the food.
● Hunger bars: The number of bars of hunger this food will give you when eaten. This
can be used to mine materials.
● Cost: The emerald cost of the food. This is fixed.

The Game
The game starts off by generating caves, materials, players, and traders randomly. The
player starts off with a certain amount of emeralds. From here, each day of the game plays
out like follows:

1. The traders decide on what materials they will buy today, and for how many emeralds
2. A number of randomly generated food items are offered to the player
3. The player can select one and only one food item to purchase, filling up their hunger
points
4. The player can go mining for the day, using their hunger to collect materials, and then
the player sells all of their materials for emeralds
5. The quantities of materials in each cave is updated, and the cycle repeats.


Here, the player can purchase the Cooked Chicken Cuts for 19 emeralds, and receive 424
hunger bars.
Current Emeralds: 50 - 19 = 31
From here, they can first visit Castle Karstaag Ruins, and mine 4 Netherite Ingots. This takes
4 * 20.95 hunger bars. These 4 Netherite Ingots sell for 9.78 emeralds with Ruby Goodman.
Current Emeralds: 31 + 4 * 9.78 = 70.12
From here, the player can then visit Red Eagle Redoubt, mining all 3 Fishing Rods. This
takes 3 * 26.93 hunger bars. These 3 Fishing Rods sell for 7.44 emeralds with Waldo
Morgan.
Current Emeralds: 70.12 + 3 * 7.44 = 92.44
From here, the player can then visit Glacial Cave, mining all 3 Gold Nuggets. This takes 3 *
27.24 hunger bars. These 3 Gold Nuggets sell for 7.7 emeralds with Orson Hoover.
Current Emeralds: 92.44 + 3 * 7.7 = 115.54
From here, the player can then visit Boulderfall Cave, mining all 10 Prismarine Crystals. This
takes 10 * 11.48 hunger bars. These 10 Prismarine Crystals sell for 7.63 emeralds with Lea
Carpenter.
Current Emeralds: 115.54 + 10 * 7.63 = 191.84
From here, the player can then visit Orotheim, mining ~2.3353 Fishing Rods. This takes
~2.3353 * 26.93 hunger bars. These 2.3353 Fishing Rods sell for 7.44 emeralds with Waldo
Morgan.
Current Emeralds: 191.84 + 2.3353 * 7.44 = 209.2147
If the game continued, the quantities within each cave would be updated based on the
player's choices. After this, some random amount of each material would be added to caves
(see functions mentioned later in the spec)
Note that there are other possible solutions, this one has just been highlighted. Any solution
which allows the player to end with ~209.2147 emeralds is optimal. Hunger bars used in
previous days cannot be saved for subsequent ones.
