# Space Invaders

## Description
"Space Invaders" is a classic space-themed shooter game where players control a spaceship to fend off invading enemies. Your goal is to eliminate the invaders while avoiding their attacks. The game window has a size of 300x300 pixels.

## Code Overview

### Import Statements
The game imports essential classes and functions from external files, including `sprite.py`, `bullet.py`, `invader.py`, and `player.py`.

### Instantiating Objects
The game initializes instances of various classes: `Player` (spaceship), `Bullet` (projectiles), and `Invader` (enemies).

### Setting up the Game
In the `setup()` function, the game window is initialized with a black background. The font is loaded, and the text size is set to 18. The initial program state is set to 'START', displaying a welcome message.

### Drawing the Game
The `draw()` function serves as the main game loop. Depending on the program state, it displays different elements. In the 'START' state, a welcome message is shown. In the 'PLAY' state, the game updates and draws bullets, player, and invaders. When a bullet hits an invader, it's removed from the `invader_list`. If all invaders are defeated, the game state changes to 'WIN'. If an invader reaches the left border, the game state changes to 'LOSE'.

### Key and Mouse Events
The game responds to key and mouse interactions. Pressing the spacebar resets the bullet to the player's position. Clicking the mouse during the 'START' state changes the game state to 'PLAY'.

# Doggy Dodge

## Description
"Doggie Dodge" challenges you to control a dog and dodge falling little doggies (asteroids) using object-oriented programming. Maneuver the main dog to avoid collisions with the falling little doggies. Colliding results in a game over, while successfully avoiding them leads to a win. After the game ends, players can restart.

## Features

- Control the main dog (dog 1) using keyboard inputs to avoid falling little doggies (dog 2).
- Object-oriented programming structures the gameplay and interactions.
- Collision detection implemented: Colliding with a falling little doggy ends the game.
- Win condition: Successfully avoid all little doggies to win.
- Restart option: After the game concludes (win or lose), players can restart.

The game focuses on avoiding collisions, providing an engaging gameplay experience while keeping mechanics simple.
