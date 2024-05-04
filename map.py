from tile import LandTile, BeachTile, OceanTile
from css_writer import CSSWriter

WIDTH = 5
HEIGHT = 5

css_writer = CSSWriter()


class Map:
    def __init__(self):
        self.player_loc = [2, 2]  # Initial player location, center of map (Phase-1)
        self.layout = []  # Matrix of hashmap elems consisting of: tile object, is_vis (T/F), is_selectable (T/F)
        self.build_initial_map()

    def build_initial_map(self):
        """Generate and assemble tiles into map layout,
        set visibility and selectability, write to CSS"""

        # Generate tiles for all map layout positions
        for x in range(WIDTH):
            col = []
            for y in range(HEIGHT):
                # Generate OceanTiles at inner map boundary (Phase-1)
                if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
                    tile = OceanTile()
                # Generate LandTiles elsewhere (Phase-1)
                else:
                    tile = LandTile()
                # Set tile selectability based on player loc
                if abs(x - self.player_loc[0]) <= 1 and abs(y - self.player_loc[1]) <= 1:
                    is_selectable = True
                else:
                    is_selectable = False
                # Populate map layout position
                col.append({'tile': tile,
                            'is_vis': True,
                            'is_selectable': is_selectable
                            })
            self.layout.append(col)
        self.write_CSS()

    def write_CSS(self):
        css_writer.update_layout(self.get_layout(), self.get_player_loc())

    def update(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if abs(x - self.player_loc[0]) <= 1 and abs(y - self.player_loc[1]) <= 1:
                    self.layout[x][y]['is_selectable'] = True
                else:
                    self.layout[x][y]['is_selectable'] = False

        self.write_CSS()

    def get_layout(self):
        return self.layout

    def get_player_loc(self):
        return self.player_loc

    def get_player_tile(self):
        return self.layout[self.player_loc[0]][self.player_loc[1]]['tile']

    def set_player_loc(self, new_player_loc):
        self.player_loc = new_player_loc

    def access(self, tile_loc: list):
        x = tile_loc[1]
        y = tile_loc[0]
        return self.layout[x][y]
