MAX_THIRST = 3
MAX_HUNGER = 5
MAX_TEMP = 3
MAX_SLEEP = 1
MAX_WOOD = 3
MAX_FOOD = 1

class Player:

    def __init__(self):
        self.condition = {
            'thirst': "good",
            'hunger': "good",
            'temp': "good",
            'sleep': "good"
        }
        if self.condition['thirst'] == 0\
            or self.condition['hunger'] == 0\
            or self.condition['temp'] == 0 \
            or self.condition['sleep'] == 0:
            energy = 0
        else:
            energy = 3
        self.speed = 3 + energy
        self.items = {
            'wood': 0,
            'food': 0
        }

    def get_condition(self):
        return self.condition

    # Fill thirst by drinking from water source
    def fill_thirst(self):
        # Check if thirsty
        if self.condition['thirst'] < MAX_THIRST:
            # Fill thirst
            self.condition['thirst'] = MAX_THIRST

    # Fill hunger by eating carried food
    def fill_hunger(self):
        # Check if hungry
        if self.condition['hunger'] < MAX_HUNGER:
            # Deduct 1 food
            self.items['food'] -= 1
            # Add 1 hunger
            self.condition['hunger'] += 1

    # Fill energy by sleeping
    def fill_sleep(self):
        # Check if tired
        if self.condition['sleep'] < MAX_SLEEP:
            # Fill energy
            self.condition['sleep'] = MAX_SLEEP

    # Fill temp by day or with fire
    def fill_temp(self):
        # Check if cold
        if self.condition['temp'] < MAX_TEMP:
            # Fill energy
            self.condition['temp'] = MAX_TEMP
