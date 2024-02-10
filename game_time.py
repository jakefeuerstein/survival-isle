class GameTime:

    def __init__(self):
        self.day = 1
        self.time = "early morning"
        self.turns = 3

    def turn_step(self):
        self.time_step()
        self.turns -= 1

    def day_step(self):
        self.day += 1
        self.time == "early morning"
        self.turns = 3

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
