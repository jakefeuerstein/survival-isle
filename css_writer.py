TILE_WIDTH = 50


class CSSWriter:

    def __init__(self):
        self.layout = []

    def update_layout(self, map_layout, player_loc):
        new_layout = []
        for x in range(len(map_layout)):
            col = []
            for y in range(len(map_layout[0])):
                if map_layout[x][y]['is_vis']:
                    # tile is visible
                    color = map_layout[x][y]['tile'].get_color()
                else:
                    # tile is not visible
                    color = "black"
                if map_layout[x][y]['is_selectable']:
                    # tile is selectable
                    hover = True
                else:
                    hover = False
                col.append({'id': f'{x}{y}',
                            'color': color,
                            'hover': hover
                            })
                # build grid element
            new_layout.append(col)
            self.layout = new_layout
            self.update_css(player_loc)

    def update_css(self, player_loc):
        with open("static/styles/styles_game.css", 'r+') as styles_file:
            # Convert styles_file to list of lines
            styles_text = styles_file.readlines()
            # Extract static section of styles_file
            for i, row in enumerate(styles_text):
                # Find breakpoint
                if row.find("break") != -1:
                    # Slice styles_text up to breakpoint
                    styles_text = styles_text[:i+1]
                    # Convert styles_text to string
                    styles_text = "".join(styles_text)
            addition = "\n"
            # Generate variable section of styles file with layout elems
            for x in range(len(self.layout)):
                for y in range(len(self.layout[0])):
                    elem = self.layout[x][y]
                    # Create CSS element
                    css_elem = f'#tile{elem["id"]} {{' \
                               f'\n   left: {TILE_WIDTH*y}px;' \
                               f'\n   top: {TILE_WIDTH*x}px;' \
                               f'\n   background-color: {elem["color"]};' \
                               f'\n}}\n\n'
                    css_hover_elem = ""
                    # Create CSS hover element
                    if elem['hover']:
                        css_hover_elem = f'#tile{elem["id"]}:hover {{' \
                                   f'\n   background-color: gray;' \
                                   f'\n}}\n\n'
                    # Add each CSS element
                    addition += css_elem + css_hover_elem
            # Update player CSS
            player_elem = f'.player {{' \
                          f'\n    position: absolute;' \
                          f'\n    transform: translate(-50%, -50%);' \
                          f'\n    width: {TILE_WIDTH}px;' \
                          f'\n    height: {TILE_WIDTH}px;' \
                          f'\n    border: 2px solid yellow;' \
                          f'\n    left: {TILE_WIDTH * player_loc[1]}px;'\
                          f'\n    top: {TILE_WIDTH * player_loc[0]}px;'\
                          f'\n}}\n\n'
            addition += player_elem
            # Position at beginning of styles_file
            styles_file.seek(0)
            styles_file.write(styles_text + addition)

            # Copy new content to CSS file
            # with open("static/styles/styles_game.css", 'w') as f2:
            #     print("writing to CSS file")
            #     styles_file.seek(0)
            #     f2.write(styles_file.read())