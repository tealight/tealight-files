from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 2
  for i in range(0, edges):
    move(size)
    square(decoration)
    turn(angle)

turn(-90)
waterwheel(12,75)
