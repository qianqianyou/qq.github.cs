import js
p5 = js.window

# class definition for the Bullet object:
class Bullet:  
  def __init__(self, x = 150, y = 250):
    self.x = x  
    self.y = y  

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.fill(255, 0, 127)
    p5.rect(0, 0, 4, 8)
    p5.pop()
  
  def update(self):
    self.x += 2