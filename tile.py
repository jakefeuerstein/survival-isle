# from player import Player
import random

LAND_FOOD_PROB = [0, 0, 0, 1, 2]
LAND_WATER_PROB = [0, 0, 0, 0, 1]
LAND_WOOD_PROB = [0, 0, 1, 2]
BEACH_FOOD_PROB = [0, 0, 0, 1, 2]
BEACH_WOOD_PROB = [0, 0, 1, 2]

class Tile:
    def __init__(self):
        self.color = None
        self.resources = {
            "food": 0,
            "water": 0,
            "wood": 0,
            "flint": 0
        }
        self.creations = {
            "shelter": False,
            "fire": False
        }

    def get_color(self):
        return self.color

    def check_resources(self):
        available_resources = {}
        for resource, value in self.resources.items():
            if value:
                available_resources[resource] = value
        return available_resources

    def check_creations(self):
        possible_resources = {}
        for creation, value in self.resources.items():
            if value:
                available_resources[resource] = value
        return self.creations

    def harvest_resource(self, resource):
        if resource == 'water': return
        # reduce resource by 1
        self.resources[resource] -= 1

    def create(self, creation):
        self.creations[creation] = True


class LandTile(Tile):

    def __init__(self):
        super().__init__()
        self.color = "green"
        self.resources['food'] = random.choice(LAND_FOOD_PROB)
        self.resources['water'] = random.choice(LAND_WATER_PROB)
        self.resources['wood'] = random.choice(LAND_WOOD_PROB)


class BeachTile(Tile):

    def __init__(self):
        super().__init__()
        self.color = "beige"
        self.resources['food'] = random.choice(BEACH_FOOD_PROB)
        self.resources['wood'] = random.choice(BEACH_WOOD_PROB)


class OceanTile(Tile):

    def __init__(self):
        super().__init__()
        self.color = "blue"
        self.resources = None
        self.creations = None


# class StreamTile(Tile):
#
#     def __init__(self):
#         super().__init__()
#         self.color = "green"
