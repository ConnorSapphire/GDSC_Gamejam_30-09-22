# GDSC_Gamejam_30-09-22

## Inspiration
We were inspired by the game Rhythm Heaven. We initially settled on mixing colours pretty early on, and wanted to make something paint shop themed. We weren't sure how we could make that work with Rhythm Heaven, but we couldn't get the idea out of our heads. So we tried our best to merge the two ideas and create something unique.

## What it does
Our game is a rhythm game, where "paint orders" come down from the top of the screen towards the shop owner. The shop owner must then move between lanes and hit the correct keys: a = blue, s = yellow, d = red, in order to create the requested paint. The goal of the game is to fulfill as many orders as possible to the beat of the song.

## How we built it
We decided to build our game in Python Arcade, deciding it would be an easier choice than Pygame for what we were doing. We started simple just drawing everything to screen and worked from there. Each team member focusing on one thing and working out how to add its functionality, then coming together in a call to merge everything into one cohesive unit.
## Challenges we ran into
Our biggest challenge was by far timing the falling "paint orders" to the beat of the song to enable them to touch the line perfectly in time. Otherwise, everything went fairly smoothly and the whole team was working as hard as possible to pump it out.

## Accomplishments that we're proud of
Our biggest accomplishment was simply working collaboratively over GitHub. We all came together really well. While there were inevitable miscommunications we all sorted it out together. In terms of code, our biggest accomplishment was by far getting the beats in time to the music. It was very finnicky but worth every second.

## What we learned
We learned so much! This was everyone's first time using Python Arcade, so we were all starting from scratch. We not only learnt how to use the module, but also how to work in a team better. 

## What's next for Paint Treble
If we decide to continue working on this project, I think we'd like to hone the art style to better represent the game. Incorporate new songs, and possibly divide the game into levels.


## Ideas

So far we have:

- Rhythm game to do with combining colours (mixing -- colour theory) to deal damage
- If the player is hit, is knocked back so they are always 'on edge'
- Guitar hero with 3 primary colour buttons (or 2 for the theme maybe) and you have to click the right combination when a projectile enters your hitbox
- Theme idea: paint mixing shop - customers with orders - call and response system

## Log

- How the basics currently work
  - The scene object contains sprite lists.
  - The player and beat class currently inherit from arcade.Sprite, so they can be included in the sprite list
  - Their constructor says where they spawn
  - <mark>The update function in these classes is called when scene.update() is called -- this should control their intenal logic</mark>
  - Game settings are controlled by constants.py
  - The scene.draw() function draws everything in the current scene, after the previous frame is cleared by background
  
  ## References 
- [Excalidraw idea board](https://excalidraw.com/#room=b1b331cdc14bf105071c,3ENxMURdof3BfPm86YKy8Q)
- Artwork: https://shubibubi.itch.io/
- Music: https://www.youtube.com/watch?v=K_sk82MgSK8 
 
## ✍️ Authors <a name = "authors"></a>
[@CindyU-beep](https://github.com/CindyU-beep): Cindy Um
[@ConnorSapphire](https://github.com/ConnorSapphire): Connor Sapphire 
[@lyliux](https://github.com/lyliux): Holly Trikilis
[@Zarlden](https://github.com/Zarlden): Damon Lam 
