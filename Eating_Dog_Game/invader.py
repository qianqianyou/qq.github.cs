import js
p5 = js.window

# import the code from sprite.py:
from sprite import *  

# class definition for the Invader object
# as a child of Sprite object:
class Invader(Sprite):
  def __init__(self, x = 150, y = 150):
    self.x = x  
    self.y = y
    self.timer = p5.millis()
    self.img1 = p5.loadImage('data/attack_dog.png');  
    self.img2 = p5.loadImage('data/defence_dog.png');   
  
  def update(self):
    if(p5.millis() > self.timer + 500):
      if(self.x < p5.width - self.img1.width/2):
        self.x -= 5
      else:
        self.x = self.img1.width/2
      self.timer = p5.millis()

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    if(p5.millis() % 1000 < 500):
      p5.image(self.img1, 0, 0)
    else:
      p5.image(self.img2, 0, 0)
    p5.pop()