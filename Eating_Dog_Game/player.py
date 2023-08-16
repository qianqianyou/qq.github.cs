import js
p5 = js.window

# class definition for the Player object:
class Player():  
  def __init__(self):
    self.img = p5.loadImage('data/player.png')
    self.x = 20
    self.y = 150
  
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0)
    p5.pop()