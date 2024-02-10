from tile import LandTile, BeachTile, OceanTile
from css_writer import CSSWriter

WIDTH = 5
HEIGHT = 5

css_writer = CSSWriter()


class Map:
    def __init__(self):
        self.player_loc = [2, 2]
        self.layout = []
        self.build_initial_map()

    def build_initial_map(self):
        for x in range(WIDTH):
            col = []
            for y in range(HEIGHT):
                if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
                    tile = OceanTile()
                    # create border as OceanTile
                else:
                    tile = LandTile()
                    # create inner area as LandTile
                col.append({'tile': tile,
                            'is_vis': True,
                            'is_selectable': True
                            })
            self.layout.append(col)
            self.write_CSS()

    def write_CSS(self):
        css_writer.update(self.get_layout(), self.get_player_loc())

    def update(self):
        self.write_CSS()

    def get_layout(self):
        return self.layout

    def get_player_loc(self):
        return self.player_loc

    def set_player_loc(self, new_player_loc):
        self.player_loc = new_player_loc

    def access(self, tile_loc: list):
        x = tile_loc[1]
        y = tile_loc[0]
        return self.layout[x][y]
