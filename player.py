# Max attribute values
MAX_THIRST = 9
MAX_HUNGER = 9
MAX_TEMP = 3
MAX_SLEEP = 10

# Max item values
MAX_WATER = 3
MAX_FOOD = 1
MAX_WOOD = 5
MAX_FLINT = 1


class Player:

    def __init__(self):
        self.condition = {
            'thirst': MAX_THIRST,  # 3 days to GO * 3 req water per day
            'hunger': MAX_HUNGER,  # 3 days to GO * 3 req water per day
            'temp': MAX_TEMP,  # 3 days to GO
            'sleep': MAX_SLEEP  # 10 days to GO
        }
        self.prev_update = {
            'thirst': "early morning",
            'hunger': "early morning",
            'temp': 0,
            'sleep': 0
        }
        # Concept: energy for speed
        # if self.condition['thirst'] == 0\
        #     or self.condition['hunger'] == 0\
        #     or self.condition['temp'] == 0 \
        #     or self.condition['sleep'] == 0:
        #     energy = 0
        # else:
        #     energy = 3
        # self.speed = 3 + energy
        self.items = {
            'water': [0, 3],
            'food': [0, 1],
            'wood': [0, 5],
            'flint': [0, 1]
        }

    # Return current condition
    def get_condition(self):
        return self.condition

    # Update for every time step
    def update(self, gt):
        # Thirst: automatically restores if water available
        if gt.time != self.prev_update['thirst']:
            # Restore
            if self.items['water']:
                self.items['water'] -= 1
                self.condition['thirst'] = MAX_THIRST
            # Dec
            else:
                self.dec_attr('thirst')
                self.prev_update['thirst'] = gt.time
        # Hunger: automatically restores if food available
        if gt.time != self.prev_update['hunger']:
            # Restore
            if self.items['food']:
                self.items['food'] -= 1
            # Dec
            self.dec_attr('hunger')
            self.prev_update['hunger'] = gt.time
        # Temp: restores with fire
        if gt.time == 'night' and self.prev_update['temp'] != gt.day and gt.turns == 1:
            if True:  # Fix1: create fire functionality, i.e. check for fire access
                self.dec_attr('temp')
                self.prev_update['temp'] = gt.day
        # Sleep: restores with sleep
        if gt.time == 'night' and self.prev_update['sleep'] != gt.day and gt.turns == 1:
            self.dec_attr('sleep')
            self.prev_update['sleep'] = gt.day

    # Decrease condition attribute
    def dec_attr(self, attr):
        self.condition[attr] -= 1
        if self.condition[attr] == 0:
            print("Game over")

    # Restore condition attribute
    def restore(self, attr):
        # Restore temp with fire, Phase2: restore temp by day or with fire
        if attr == 'temp':
            self.condition['temp'] += 1
        # Restore sleep by sleeping
        elif attr == 'sleep':
            self.condition['sleep'] += 1

    def get_items(self):
        return self.items

    def inc_item(self, item):
        if item == 'water':
            self.items['water'] == MAX_WATER
        else:
            self.items[item][0] += 1
            if self.items[item][0] > self.items[item][1]:
                self.items[item][0] = self.items[item][1]

    def dec_item(self, item):
        self.items[item] -= 1