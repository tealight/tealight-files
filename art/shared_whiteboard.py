from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send

lastx = 0
lasty = 0

color("blue")
connect("shared_whiteboard")

def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    line(lastx, lasty, x, y)
    send({"x1": lastx, "y1": lasty, "x2": x, "y2": y})
    lastx = x
    lasty = y
  
def handle_message(message):
  line(message["x1"], message["y1"], message["x2"], message["y2"])