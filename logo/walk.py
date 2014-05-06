from tealight.logo import (move, turn,
                           pen_down, pen_up,
                           show_turtle, hide_turtle,
                           color, speed)

from random import random

i = 0

while i < 10000:
  move(random()*10)
  turn(random()*360)
  print i
  color("hsl(%d,60%%,50%%)" % i)
  i += 1