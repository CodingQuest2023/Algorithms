from world import World
from world_drawer import *
from config import *


def test_generate_world(weights, random_seed):
    world_drawer = WorldDrawer()
    world = World(WORLD_X, WORLD_Y, random_seed)
    tile_map = world.get_tiled_map(weights)
    world_drawer.draw(tile_map, wait_for_key = True)


def test_emerge(target_weights, random_seed):
    world_drawer = WorldDrawer()
    world = World(WORLD_X, WORLD_Y, random_seed)
    weights = [target_weights[OCEAN3] - 1, 0, 0, 0, 0, 0, 0]
    done = False

    while not done:
        tile_map = world.get_tiled_map(weights)
        world_drawer.draw(tile_map, wait_for_key = False)

        if weights[OCEAN3] < target_weights[OCEAN3]:
            weights[OCEAN3] += 1
        elif weights[OCEAN2] < target_weights[OCEAN2]:
            weights[OCEAN2] += 1
        elif weights[OCEAN1] < target_weights[OCEAN1]:
            weights[OCEAN1] += 1
        elif weights[BEACH] < target_weights[BEACH]:
            weights[BEACH] += 1
        elif weights[GRASS] < target_weights[GRASS]:
            weights[GRASS] += 1
        elif weights[MOUNTAIN] < target_weights[MOUNTAIN]:
            weights[MOUNTAIN] += 1
        elif weights[SNOW] < target_weights[SNOW]:
            weights[SNOW] += 1
        else:
            done = True

    done = False
    target_weights = [weights[OCEAN3] - 1, 0, 0, 0, 0, 0, 0]

    while not done:
        tile_map = world.get_tiled_map(weights)
        world_drawer.draw(tile_map, wait_for_key = False)

        if weights[SNOW] >= target_weights[SNOW] and weights[SNOW] > 0:
            weights[SNOW] -= 1
        elif weights[MOUNTAIN] >= target_weights[MOUNTAIN] and weights[MOUNTAIN] > 0:
            weights[MOUNTAIN] -= 1
        elif weights[GRASS] >= target_weights[GRASS] and weights[GRASS] > 0:
            weights[GRASS] -= 1
        elif weights[BEACH] >= target_weights[BEACH] and weights[BEACH] > 0:
            weights[BEACH] -= 1
        elif weights[OCEAN1] >= target_weights[OCEAN1] and weights[OCEAN1] > 0:
            weights[OCEAN1] -= 1
        elif weights[OCEAN2] >= target_weights[OCEAN2] and weights[OCEAN2] > 0:
            weights[OCEAN2] -= 1
        elif weights[OCEAN3] >= target_weights[OCEAN3] and weights[OCEAN3] > 0:
            weights[OCEAN3] -= 1
        else:
            done = True
