from __future__ import division

from cocos.actions import Move
from cocos.collision_model import AARectShape
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window import key

from game import utils
from game.resources import resources

class MovingBlock(Sprite):
    def __init__(
            self,
            sprite,
            velocity = (-10, 0),
            *args,
            **kwargs):

        if 'position' not in kwargs.keys():
            kwargs['position'] = (800, 150)

        super(MovingBlock, self).__init__(sprite, *args, **kwargs)
        self.cshape = AARectShape(self.position, self.width//3, self.height//2)

        self.velocity = velocity

        self.do(Move())
        self.schedule(self.update)

    def update(self, dt):
        self.cshape.center = self.position
        if self.position[0] < 0:
            self.position = 810, self.position[1]





class Blocks(MovingBlock):
    """docstring for Blocks"""
    def __init__(
        self,
        sprite = resources.block,
        velocity = (-20, 0),
        *args,
        **kwargs):

        if 'position' not in kwargs.keys():
            kwargs['position'] = (800, 150)

        super(Blocks, self).__init__(
            sprite,
            velocity = velocity,
            *args,
            **kwargs
        )