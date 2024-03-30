from game_time import GameTime

gt = GameTime()

class Actions:

    def move(self, map, selected_tile_loc):
            # Format tile location from str to list
            selected_tile_loc = selected_tile_loc.split(',')
            for n in range(len(selected_tile_loc)):
                selected_tile_loc[n] = int(selected_tile_loc[n])
            # Get player location
            player_loc = map.get_player_loc()
            # Check if move is valid
            if (abs(selected_tile_loc[0] - player_loc[0]) <= 1 and
                abs(selected_tile_loc[1] - player_loc[1]) <= 1):
                # Valid move
                map.set_player_loc(new_player_loc=selected_tile_loc)
                map.update()
                # PLACEHOLDER: gt.turn_step()
            else:
                valid_move = False
                print("invalid move")

    def harvest(self, tile_loc, resource):
        tile = map.access(tile_loc)['tile']
        resource_qty = tile.get_resources()[resource]
        if resource_qty > 0:
            tile.harvest_resource(resource)
            print(f'{resource} harvested')
        elif resource_qty == 0:
            print(f'{resource} qty is 0')

    def build_fire(self, tile_loc):
        tile = map.access(tile_loc)['tile']
        if tile.resources["wood"] > 0 and tile.resources["flint"] > 0:
            # Fire can be built
            tile.create("fire")
            tile.harvest_resource("wood")
            # Fire built

    def build_shelter(self, tile_loc):
        tile = map.access(tile_loc)['tile']
        if tile.resources["wood"] > 0:
            # Shelter can be built
            tile.create("shelter")
            tile.harvest_resource("wood")
            # Shelter built
        else:
            print("resource count is 0")

    player_options = ["move (click tile)", "harvest resource", "build fire", "build shelter", "sleep"]