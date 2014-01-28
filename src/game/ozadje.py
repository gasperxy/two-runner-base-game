# -*- coding: utf-8 -*-
from __future__ import division

from cocos.actions import Move
from cocos.sprite import Sprite

from game.resources import resources

class MovingBackground(Sprite):
    def __init__(
            self,
            sprite,
            velocity = (-10, 0),
            *args,
            **kwargs):

        if 'position' not in kwargs.keys():
            kwargs['position'] = (800, 400)

        super(MovingBackground, self).__init__(sprite, *args, **kwargs)

        self.velocity = velocity

        self.do(Move())
        self.schedule(self.update)

    def update(self, dt):
        if self.position[0] < 0:
            self.position = 810, self.position[1]





class Oblacki(MovingBackground):
    """docstring for Oblacki"""
    def __init__(
        self,
        sprite = resources.cloud1,
        velocity = (-10, 0),
        *args,
        **kwargs):

        if 'position' not in kwargs.keys():
            kwargs['position'] = (800, 400)

        super(Oblacki, self).__init__(
            sprite,
            velocity = velocity,
            *args,
            **kwargs
        )

