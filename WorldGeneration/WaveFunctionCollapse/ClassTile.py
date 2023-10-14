import random
from Config import *


class Tile:

    def __init__(self, x, y):
        self.possibilities = list(tileRules.keys())
        self.entropy = len(self.possibilities)
        self.neighbours = dict()


    def addNeighbour(self, direction, tile):
        self.neighbours[direction] = tile


    def getNeighbour(self, direction):
        return self.neighbours[direction]


    def getDirections(self):
        return list(self.neighbours.keys())


    def getPossibilities(self):
        return self.possibilities


    def collapse(self):
        weights = [tileWeights[possibility] for possibility in self.possibilities]
        self.possibilities = random.choices(self.possibilities, weights=weights, k=1)
        self.entropy = 0


    def constrain(self, neighbourPossibilities, direction):
        reduced = False

        if self.entropy > 0:
            connectors = []
            for neighbourPossibility in neighbourPossibilities:
                connectors.append(tileRules[neighbourPossibility][direction])

            # check opposite side
            if direction == NORTH: opposite = SOUTH
            if direction == EAST:  opposite = WEST
            if direction == SOUTH: opposite = NORTH
            if direction == WEST:  opposite = EAST

            for possibility in self.possibilities.copy():
                if tileRules[possibility][opposite] not in connectors:
                    self.possibilities.remove(possibility)
                    reduced = True

            self.entropy = len(self.possibilities)

        return reduced
