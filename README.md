# Mining-and-Trading-Game-1008

# Quick Background 

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

