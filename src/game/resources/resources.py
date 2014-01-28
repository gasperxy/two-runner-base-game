# -*- coding: utf-8 -*-

import pyglet

pyglet.resource.path = ["@game.resources.sprites"]
pyglet.resource.reindex()

mario = pyglet.resource.image("mario.jpg")
obstacle = pyglet.resource.image("obstacle.png")
background = pyglet.resource.image("background.jpg")
cloud1 = pyglet.resource.image("cloud1.png")
cloud2 = pyglet.resource.image("cloud2.png")
block = pyglet.resource.image("block.png")
# sun = pyglet.resource.image("sun.jpg")
