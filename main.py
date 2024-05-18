from flask import Flask, render_template, request
from map import Map
from actions import Actions
from player import Player
from game_time import GameTime

# Instantiations
map = Map()
app = Flask(__name__)
actions = Actions()
player = Player()
gt = GameTime()

# valid_move = None  delete if unused

@app.route("/", methods=['GET', 'POST'])
def game():

    if gt.turns > 0:
        # Button was clicked
        if request.method == "POST":
            tile_loc = map.get_player_loc()
            # Move action
            if request.form.get('move'):
                print("main: move button clicked")
                selected_tile_loc = request.form.get('move')
                # Facilitate move
                actions.move(map, selected_tile_loc, gt)
            # Harvest action
            elif request.form.get('harvest'):
                print("harvest button clicked")
                resource = request.form.get('harvest')
                actions.harvest(map, tile_loc, resource, player, gt)
            # Build fire action
            elif request.form.get('build_fire'):
                print("build fire button clicked")
                actions.build_fire(tile_loc, gt)
            # Build shelter action
            elif request.form.get('build_shelter'):
                print("build shelter button clicked")
                actions.build_shelter(tile_loc, gt)

    player.update(gt)
    return render_template("game.html", map=map, actions=actions)

@app.route("/home")
def home():
    return render_template("home.html")

def display(element):

    # Return desired element
    if element == "game_title":
        return "Survival Isle"
    elif element == "game_day":
        return gt.get_game_time('day')
    elif element == "game_time":
        return gt.get_game_time('time')
    elif element == "player_condition":
        return player.get_condition()
    elif element == "num_moves":
        return gt.get_game_time('turns')
    elif element == "items":
        return player.get_items()


# Allow display function to be accessed with Jinja
app.jinja_env.globals.update(display=display)


if __name__ == "__main__":
    app.run(debug=True)