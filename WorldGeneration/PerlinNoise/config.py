TILESHEET_PATH = "../../Assets/SpriteSheets/PunyWorld/punyworld-overworld-tileset-perlin.png"

WINDOW_WIDTH    = 1920
WINDOW_HEIGHT   = 1080
TILESIZE        = 16       # tile width/height in pixels in tilesheet
WORLD_X         = (WINDOW_WIDTH + TILESIZE - 1) // TILESIZE
WORLD_Y         = (WINDOW_HEIGHT + TILESIZE - 1) // TILESIZE


# Terrain types
OCEAN3 = 0
OCEAN2 = 1
OCEAN1 = 2
BEACH = 3
GRASS = 4
MOUNTAIN = 5
SNOW = 6


# List of all terrain type, ordered from lower height to higher height
ALL_TERRAIN_TYPES = [OCEAN3, OCEAN2, OCEAN1, BEACH, GRASS, MOUNTAIN, SNOW]


# All tiles in the tilesheet, for each terrain type in ALL_TERRAIN_TYPES
TERRAIN_TILES = [
    # Ocean depth level 3 tiles
    [
        (0, 0),  #
        (352, 160),  ## bottom-right
        (384, 160),  ## bottom-left
        (368, 160),  ## bottom side
        (352, 192),  ## top-right
        (352, 176),  ## right side
        (400,144),  ## TR, BL
        (400, 160),  ## TR, BL, BR
        (384, 192),  ## top-left
        (416, 144),  ## TL, BR
        (384, 176),  ## left side
        (416, 208),  ## TL + BL + BR
        (368, 192),  ## top side
        (368, 176),  ## TL + TR + BR
        (416, 224),  ## TL + TR + BL
        (368, 176),  ## all sides
    ],
    # Ocean depth level 2 tiles
    [
        (0, 0),  #
        (272, 160),  ## bottom-right
        (304, 160),  ## bottom-left
        (288, 160),  ## bottom side
        (272, 192),  ## top-right
        (272, 176),  ## right side
        (336, 144),  ## TR, BL
        (320, 160),  ## TR, BL, BR
        (304, 192),  ## top-left
        (352, 144),  ## TL, BR
        (304, 176),  ## left side
        (336, 160),  ## TL + BL + BR
        (288, 192),  ## top side
        (320, 176),  ## TL + TR + BR
        (336, 176),  ## TL + TR + BL
        (288, 176),  ## all sides
    ],
    # Ocean depth level 1 tiles
    [
        (0, 0),  #
        (192, 160),  ## bottom-right
        (224, 160),  ## bottom-left
        (208, 160),  ## bottom side
        (192, 192),  ## top-right
        (192, 176),  ## right side
        (288, 144),  ## TR, BL
        (240, 160),  ## TR, BL, BR
        (224, 192),  ## top-left
        (304, 144),  ## TL, BR
        (224, 176),  ## left side
        (256, 160),  ## TL + BL + BR
        (208, 192),  ## top side
        (240, 176),  ## TL + TR + BR
        (256, 176),  ## TL + TR + BL
        (208, 176),  ## all sides
    ],
    # Beach level tiles
    [
        (0, 0),  #
        (352, 0),  ## bottom-right
        (192, 0),  ## bottom-left
        (176, 0),  ## bottom side
        (160, 32),  ## top-right
        (160, 16),  ## right side
        (400, 32),  ## TR, BL
        (208, 0),  ## TR, BL, BR
        (192, 32),  ## top-left
        (416, 32),  # TR, BL
        (192, 16),  ## left side
        (224, 0),  ## TL + BL + BR
        (176, 32),  ## top side
        (208, 16),  ## TL + TR + BR
        (224, 16),  ## TL + TR + BL
        (176, 16),  ## all sides
    ],
    # Grass level tiles
    [
        (0, 0),  #
        (64, 80),  ## bottom-right
        (48, 80),  ## bottom-left
        (16, 96),  ## bottom side
        (64, 64),  ## top-right
        (32, 80),  ## right side
        (48, 96),  ## TR, BL
        (32, 96),  ## TR, BL, BR
        (48, 64),  ## top-left
        (64, 96),  ## TL, BR
        (0, 80),  ## left side
        (0, 96),  ## TL + BL + BR
        (16, 64),  ## top side
        (32, 64),  ## TL + TR + BR
        (0, 64),  ## TL + TR + BL
        (32, 32),  ## all sides
    ],
    # Mountain level tiles
    [
        (0, 0),  #
        (368, 112),  ## bottom-right
        (352, 112),  ## bottom-left
        (320, 128),  ## bottom side
        (368, 96),  ## top-right
        (336, 112),  ## right side
        (352, 128),  ## TR, BL
        (336, 128),  ## TR, BL, BR
        (352, 96),  ## top-left
        (368, 128),  ## TL, BR
        (304, 112),  ## left side
        (304, 128),  ## TL + BL + BR
        (320, 96),  ## top side
        (336, 96),  ## TL + TR + BR
        (304, 96),  ## TL + TR + BL
        (320, 112),  ## all sides
    ],
    # Snow level tiles
    [
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (0, 0),  #
        (400, 112),  ## all sides
    ]
]
