DAYS_TO_RESCUE = 30
TURNS_PER_TIME = 3

class GameTime:

    def __init__(self):
        self.day = 1
        self.time = "early morning"
        self.turns = TURNS_PER_TIME

    def get_game_time(self, key: str):
        if key == 'day':
            return self.day
        elif key == 'time':
            return self.time
        elif key == 'turns':
            return self.turns

    def turn_step(self):
        if self.turns == 1:
            self.time_step()
            return
        self.turns -= 1

    def day_step(self):
        self.day += 1
        self.time = "early morning"
        self.turns = TURNS_PER_TIME

    def time_step(self):
        if self.time == "early morning":
            self.time = "late morning"
        elif self.time == "late morning":
            self.time = "early afternoon"
        elif self.time == "early afternoon":
            self.time = "late afternoon"
        elif self.time == "late afternoon":
            self.time = "night"
        elif self.time == "night":
            self.day_step()
        self.turns = TURNS_PER_TIME
        print("time step", self.turns)
