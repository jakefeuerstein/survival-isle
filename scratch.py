# from map import Map
#
# map = Map()
#
# print(map.get_player_loc())
#
# def f():
#     map.set_player_loc([1, 1])
#
# print(map.get_player_loc())

# Step 1: Create a class that defines a point in time, here are some basics for it, uncomment and fill in when you are ready:
# class my_point:
# 	def __init__(self, time: float, position: float): #added parameters time and position with type hints
# 		self.loc = [time, position] #create point as list
# 	def __str__(self):
# 		return f"{self.loc}"
#
#
# print(my_point(-1, 999))
#
# # Step 2: Create a list of points from the values above and print it.
# time = [0, 1, 2, 5]
# position = [0, 3, 1, 3]
# pts = []
# for i in range(len(time)):
#     pt = my_point(time[i], position[i])
#     pts.append(pt)
# print(pts)
#
# # Step 3: Finally, can you create a function that takes an input time and the points above and return an actuator position?
# def get_position(time: float, pts: list[my_point]):
#   for pt in pts:
#     if pt[0] == time:
#         return pt[1]
#
# get_position(1, pts)

i = 0
print(f"i can't be negative: {i}")
