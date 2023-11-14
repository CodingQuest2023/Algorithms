from perlin_noise import PerlinNoise
from config import *


class World():

    def __init__(self, size_x, size_y, random_seed):
        self.generate_noisemap(size_x, size_y, random_seed)

        # Get min and max noise values
        flat_list = [item for sublist in self.noise_map for item in sublist]
        self.min_value = min(flat_list)
        self.max_value = max(flat_list)


    def generate_noisemap(self, size_x, size_y, random_seed):
        self.noise_map = []

        noise1 = PerlinNoise(octaves=3, seed=random_seed)
        noise2 = PerlinNoise(octaves=6, seed=random_seed)
        noise3 = PerlinNoise(octaves=12, seed=random_seed)
        noise4 = PerlinNoise(octaves=24, seed=random_seed)

        xpix, ypix = size_x + 1, size_y + 1
        for j in range(ypix):
            row = []
            for i in range(xpix):
                noise_val = noise1([i/xpix, j/ypix])
                noise_val += 0.5 * noise2([i/xpix, j/ypix])
                noise_val += 0.25 * noise3([i/xpix, j/ypix])
                noise_val += 0.125 * noise4([i/xpix, j/ypix])
                row.append(noise_val)
            self.noise_map.append(row)


    def get_noise_map(self):
        return self.noise_map


    def get_tiled_map(self, weights):
        total_weights = sum(weights)
        total_range = self.max_value - self.min_value

        # calculate maximum height for each terrain type, based on weight values
        max_terrain_heights = []
        previous_height = self.min_value
        for terrain_type in ALL_TERRAIN_TYPES:
            height = total_range * (weights[terrain_type] / total_weights) + previous_height
            max_terrain_heights.append(height)
            previous_height = height
        max_terrain_heights[SNOW] = self.max_value

        map_int = []

        for row in self.noise_map:
            map_row = []
            for value in row:
                for terrain_type in ALL_TERRAIN_TYPES:
                    if value <= max_terrain_heights[terrain_type]:
                        map_row.append(terrain_type)
                        break

            map_int.append(map_row)

        return map_int
