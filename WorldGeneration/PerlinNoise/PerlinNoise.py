from test_generate_world import *


# The order of weight values for each terrain type:
#WEIGHTS = [WEIGHT_OCEAN3, WEIGHT_OCEAN2, WEIGHT_OCEAN1, WEIGHT_BEACH, WEIGHT_GRASS, WEIGHT_MOUNTAIN, WEIGHT_SNOW]
WEIGHTS1 = [70, 20, 20, 12, 35, 30, 0]      # Islands
WEIGHTS2 = [35, 20, 20, 15, 30, 30, 25]     #
WEIGHTS3 = [20, 15, 15, 15, 50, 35, 45]     # Lakes


test_generate_world(WEIGHTS1, random_seed = 21)
test_generate_world(WEIGHTS1, random_seed = 28)
test_generate_world(WEIGHTS2, random_seed = 7)
test_generate_world(WEIGHTS2, random_seed = 8)
test_generate_world(WEIGHTS3, random_seed = 16)
test_generate_world(WEIGHTS3, random_seed = 14)


test_emerge(WEIGHTS1, random_seed = 21)
test_emerge(WEIGHTS2, random_seed = 7)
test_emerge(WEIGHTS3, random_seed = 16)
test_emerge(WEIGHTS1, random_seed = 28)
test_emerge(WEIGHTS2, random_seed = 8)
test_emerge(WEIGHTS3, random_seed = 14)
