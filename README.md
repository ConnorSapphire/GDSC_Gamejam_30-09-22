# GDSC_Gamejam_30-09-22

## Links

- [Excalidraw idea board](https://excalidraw.com/#room=b1b331cdc14bf105071c,3ENxMURdof3BfPm86YKy8Q)

### Inspiration

- Rhythm tengoku
- Rhythm heaven fever

## Theme

- Two colours
- On edge

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
