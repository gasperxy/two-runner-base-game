# -*- coding: utf-8 -*-

from __future__ import division

from cocos.actions import Move
from cocos.collision_model import AARectShape
from cocos.sprite import Sprite

from game.resources import resources

class Obstacle(Sprite):
    def __init__(
            self,
            position = (770, 30),
            velocity = (-100, 0),
            speed = 50,
            *args,
            **kwargs):

        kwargs['position'] = position

        super(Obstacle, self).__init__(resources.obstacle, *args, **kwargs)

        self.speed = speed
        self.velocity = velocity

        self.cshape = AARectShape(self.position, self.width//3, self.height//2)
        self.do(Move())
        self.schedule(self.update)

    def update(self, dt):
        self.cshape.center = self.position
        if self.position[0] < 0:
            self.position = 830, 30
