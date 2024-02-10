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

# MODIFY: placeholder variable assignments
game_time = [1, "early morning"]
num_moves = 3
player_options = ["move (click tile)", "harvest resource", "build fire", "build shelter", "sleep"]
valid_move = None

@app.route("/", methods=['GET', 'POST'])
def game():

    if gt.turns > 0:
        # Button was clicked
        if request.method == "POST":
            tile_loc = map.get_player_loc()
            # harvest action
            if request.form.get('harvest'):
                print("harvest button clicked")
                actions.harvest(tile_loc)
            # Move button
            if request.form.get('move'):
                print("move button clicked")
                selected_tile_loc = request.form.get('submit')
                # Facilitate move
                actions.move(selected_tile_loc)
            # build fire action
            elif request.form.get('build_fire'):
                print("build fire button clicked")
                actions.build_fire(tile_loc)
            # build shelter action
            elif request.form.get('build_shelter'):
                print("build shelter button clicked")
                actions.build_shelter(tile_loc)

        return render_template("game.html")

@app.route("/home")
def home():
    return render_template("home.html")

def display(element):

    # Return desired element
    if element == "game_title":
        return "Survival Isle"
    elif element == "game_time":
        return game_time
    elif element == "player_condition":
        return player.get_condition()
    elif element == "num_moves":
        return num_moves
    elif element == "player_options":
        return player_options
    elif element == "move_dialogue":
        print(valid_move)
        if valid_move == None:
            return ""
        if valid_move:
            return "Move to this tile?"
        elif valid_move == False:
            return "You must move to an adjacent tile"
    elif element == "move_buttons":
        if valid_move:
            return True
        else:
            return False

# Allow display function to be accessed with Jinja
app.jinja_env.globals.update(display=display)


if __name__ == "__main__":
    app.run(debug=True)