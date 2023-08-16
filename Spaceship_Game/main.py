import js
p5 = js.window

# Load a font
font = p5.loadFont('data/PressStart2P.otf')

# Load the background image
cover_image = p5.loadImage("data/spaceship.png")
background_image = p5.loadImage("data/background.jpg")
asteroid_image = p5.loadImage("data/dog.png")
spaceship_image = p5.loadImage("data/lose.png")

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3

    def move(self, direction):
        if direction == "LEFT":
            self.x -= self.speed
        elif direction == "RIGHT":
            self.x += self.speed

    def display(self):
        p5.fill(0, 255, 0)
        #p5.rect(self.x, self.y, 40, 20)
        p5.image(spaceship_image, self.x, self.y, 40, 20)

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2

    def update(self):
        self.y += self.speed

    def display(self):
        p5.fill(255)
        p5.image(asteroid_image, self.x, self.y, 20, 20)

# Global variables
spaceship = None
asteroids = []

program_state = 'START'

win_time = 10000  # Time in milliseconds for winning condition
game_start_time = 0
game_over = False

def setup():
  p5.createCanvas(400, 400)
  p5.imageMode(p5.CENTER)

  global spaceship
  spaceship = Spaceship(p5.width / 2, p5.height - 40)

  global game_start_time
  game_start_time = p5.millis()

def draw():
  global program_state, game_start_time, game_over
  if program_state == "START":
      p5.background(255)
      p5.image(cover_image, p5.width / 2, p5.height / 2, p5.width, p5.height)
      p5.fill(0)
      p5.textSize(25)
      p5.text("Space Game", 10, 30)

      p5.textSize(18)
      p5.text("by Qianqian", p5.width / 2, p5.height - 5)

  elif program_state == "PLAY":
      p5.background(255)
      p5.image(background_image, p5.width / 2, p5.height / 2, p5.width, p5.height)
      spaceship.display()
      for asteroid in asteroids:
          asteroid.update()
          asteroid.display()

      if not game_over:
          elapsed_time = p5.millis() - game_start_time
          if elapsed_time >= win_time:
              program_state = "WIN"
          for asteroid in asteroids:
              asteroid.update()
              asteroid.display()
              if spaceship_collides_with(asteroid):
                  program_state = "LOSE"
                  game_over = True
      else:
          p5.fill(255, 0, 0)
          p5.textSize(30)
          p5.text("Game Over. Press R to restart.", 20, p5.height / 2)

  elif program_state == "WIN":
      p5.fill(0, 255, 0)
      p5.textSize(30)
      p5.text("You Win! Press R to restart.", 20, p5.height / 2)

  elif program_state == "LOSE":
      p5.background(255)
      p5.image(background_image, p5.width / 2, p5.height / 2, p5.width, p5.height)
      p5.fill(0)
      p5.textSize(32)
      p5.text("Game Over", 100, p5.height / 2)
  
def keyPressed(event):
    global program_state, game_over
    if program_state == "START":
        program_state = "PLAY"
    elif program_state == "PLAY":
        if event.key == "ArrowLeft":
            spaceship.move("LEFT")
        elif event.key == "ArrowRight":
            spaceship.move("RIGHT")
    elif program_state == "END":
        program_state = "START"

    if event.key == "r" and (program_state == "LOSE" or program_state == "WIN"):
      reset_game()

def keyReleased(event):
  pass
  
def mousePressed(event):
  if program_state == "PLAY":
        asteroids.append(Asteroid(p5.random(p5.width), 0))

def mouseReleased(event):
  pass

def spaceship_collides_with(asteroid):
  return (
      spaceship.x < asteroid.x + 20
      and spaceship.x + 40 > asteroid.x
      and spaceship.y < asteroid.y + 20
      and spaceship.y + 20 > asteroid.y
  )

def reset_game():
  global program_state, game_start_time, game_over, spaceship, asteroids
  program_state = "PLAY"
  game_start_time = p5.millis()
  game_over = False
  spaceship = Spaceship(p5.width / 2, p5.height - 40)
  asteroids = []