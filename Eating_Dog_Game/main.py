import js
p5 = js.window

# Import the code from following files
from sprite import *
from bullet import *
from invader import *
from player import *

# create (instantiate) the Player object:
player = Player()  
# instantiate the Bullet object:
bullet = Bullet(150, 0) 

# list of invader objects:
invader_list = []

background_img = p5.loadImage('data/player.png')

for i in range(3):
  # instantiate the Invader object:
  invader = Invader(x = 250, y = 50 + i*100)

  # add invader to invader_list:
  invader_list.append(invader)  
  
font = p5.loadFont('data/PressStart2P.otf')
    
program_state = 'START'

def setup():
  p5.createCanvas(300, 300)  
  p5.rectMode(p5.CENTER)
  p5.imageMode(p5.CENTER)
  p5.textFont(font)
  p5.textSize(18)
  print('use space bar to shoot the invaders..')

def draw():
  global player, program_state

  p5.background(0)   
  p5.image(background_img, 0, 0)
  
  if(program_state == 'START'):
    p5.background(0)
    p5.fill(255)
    p5.textSize(80)
    p5.textAlign(p5.CENTER, p5.CENTER)
    p5.text("Welcome to the Eating Dog Game - QianQian", p5.width / 2, p5.height / 2)

  if(program_state == 'PLAY'):
    bullet.update() 
    bullet.draw()
    
    if(p5.keyIsPressed == True):
      if(p5.keyCode == p5.DOWN_ARROW):
        if(player.y < p5.height - player.img.height/2):
          player.y += 2
          bullet.y = player.y
      elif(p5.keyCode == p5.UP_ARROW):
        if(player.y > player.img.height/2):
          player.y -= 2
          bullet.y = player.y

    player.draw()

    # Traverse invader_list
    i = 0  # loop counter variable
    while(i < len(invader_list)):
      invader = invader_list[i]
      invader.update()
      invader.draw()
      
      # distance between invader and bullet:
      d = p5.dist(invader.x, invader.y, bullet.x, bullet.y)
      if(d < 20):  
        print('invader hit!')
        # remove item at index i from invader_list:
        invader_list.pop(i)
        # if invader_list becomes empty:
        if(len(invader_list) == 0):
          program_state = 'WIN'

      # check if the invader reached the left boarder:
      if(invader.x < invader.img1.width/2):
          program_state = 'LOOSE'

      i += 1  # increment while loop counter

  elif(program_state == 'WIN'):
    p5.fill(255)
    p5.textSize(80)
    p5.text('You Win!', 150, 150)

  elif(program_state == 'LOOSE'):
    p5.fill(255)
    p5.textSize(80)
    p5.text('You Loose!', 150, 150)

  
def keyPressed(event):
  pass

def keyReleased(event):
  global bullet
  if(p5.key == ' '):
    # reset the bullet to spaceship coordinates:
    bullet.x = player.x
    bullet.y = player.y
  
def mousePressed(event):
  global program_state
  if(program_state == 'START'):
    program_state = 'PLAY'
    print('program_state = ' + program_state)

def mouseReleased(event):
  pass