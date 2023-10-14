import random
from ClassTile import Tile
from ClassStack import Stack
from Config import *


class World:

    def __init__(self, sizeX, sizeY):
        self.cols = sizeX
        self.rows = sizeY

        self.tileRows = []
        for y in range(sizeY):
            tiles = []
            for x in range(sizeX):
                tile = Tile(x, y)
                tiles.append(tile)
            self.tileRows.append(tiles)

        for y in range(sizeY):
            for x in range(sizeX):
                tile = self.tileRows[y][x]
                if y > 0:
                    tile.addNeighbour(NORTH, self.tileRows[y - 1][x])
                if x < sizeX - 1:
                    tile.addNeighbour(EAST, self.tileRows[y][x + 1])
                if y < sizeY - 1:
                    tile.addNeighbour(SOUTH, self.tileRows[y + 1][x])
                if x > 0:
                    tile.addNeighbour(WEST, self.tileRows[y][x - 1])


    def getEntropy(self, x, y):
        return self.tileRows[y][x].entropy


    def getType(self, x, y):
        return self.tileRows[y][x].possibilities[0]


    def getLowestEntropy(self):
        lowestEntropy = len(list(tileRules.keys()))
        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy
                if tileEntropy > 0:
                    if tileEntropy < lowestEntropy:
                        lowestEntropy = tileEntropy
        return lowestEntropy


    def getTilesLowestEntropy(self):
        lowestEntropy = len(list(tileRules.keys()))
        tileList = []

        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy
                if tileEntropy > 0:
                    if tileEntropy < lowestEntropy:
                        tileList.clear()
                        lowestEntropy = tileEntropy
                    if tileEntropy == lowestEntropy:
                        tileList.append(self.tileRows[y][x])
        return tileList


    def waveFunctionCollapse(self):

        tilesLowestEntropy = self.getTilesLowestEntropy()

        if tilesLowestEntropy == []:
            return 0

        tileToCollapse = random.choice(tilesLowestEntropy)
        tileToCollapse.collapse()

        stack = Stack()
        stack.push(tileToCollapse)

        while(stack.is_empty() == False):
            tile = stack.pop()
            tilePossibilities = tile.getPossibilities()
            directions = tile.getDirections()

            for direction in directions:
                neighbour = tile.getNeighbour(direction)
                if neighbour.entropy != 0:
                    reduced = neighbour.constrain(tilePossibilities, direction)
                    if reduced == True:
                        stack.push(neighbour)    # When possibilities were reduced need to propagate further

        return 1