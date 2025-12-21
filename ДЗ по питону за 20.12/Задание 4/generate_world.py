import random


def generate_world(size, seed=None):
    if seed is not None:
        random.seed(seed)

    tiles = ["💧", "🌲", "⛰", "🏡"]
    world = []

    for _ in range(size):
        row = []
        for _ in range(size):
            tile = random.choice(tiles)
            row.append(tile)
        world.append(row)

    return world

def print_world(world):
    for row in world:
        print("".join(row))

j=generate_world(256)
print(j)