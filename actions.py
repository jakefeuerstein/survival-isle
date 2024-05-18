class Actions:

    def move(self, map, selected_tile_loc, gt):
        # Format tile location from str to list
        selected_tile_loc = selected_tile_loc.split(',')
        for n in range(len(selected_tile_loc)):
            selected_tile_loc[n] = int(selected_tile_loc[n])
        # Get player location
        player_loc = map.get_player_loc()
        # Check if move is valid
        if (abs(selected_tile_loc[0] - player_loc[0]) <= 1 and
            abs(selected_tile_loc[1] - player_loc[1]) <= 1):
            gt.turn_step()
            # Valid move
            map.set_player_loc(new_player_loc=selected_tile_loc)
            map.update()
            # PLACEHOLDER: gt.turn_step()
        else:
            valid_move = False
            print("invalid move")

    def harvest(self, map, tile_loc, resource, player, gt):
        gt.turn_step()
        tile = map.access(tile_loc)['tile']
        resource_qty = tile.check_resources()[resource]
        if resource_qty > 0:
            print(f'{resource} harvested')
            tile.harvest_resource(resource)
            player.inc_item(resource)
        elif resource_qty == 0:  # May be unnecessary
            print(f'{resource} qty is 0')

    def fire_possible(self, player_tile):  # May be unnecessary
        # Fire can be built
        if player_tile.resources["wood"] > 0 and player_tile.resources["flint"] > 0:
            return True
        return False

    def build_fire(self, tile_loc, gt):
        tile = map.access(tile_loc)['tile']
        # Fire can be built
        if tile.resources["wood"] > 4 and tile.resources["flint"] > 0:
            gt.turn_step()
            tile.create("fire")
            tile.harvest_resource("wood")
            # Fire built

    def build_shelter(self, tile_loc, gt):
        tile = map.access(tile_loc)['tile']
        # Shelter can be built
        if tile.resources["wood"] > 0:
            gt.turn_step()
            tile.create("shelter")
            tile.harvest_resource("wood")
            # Shelter built
        else:
            print("resource count is 0")

    player_options = ["move (click tile)", "harvest resource", "build fire", "build shelter", "sleep"]