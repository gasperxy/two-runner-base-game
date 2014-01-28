# -*- coding: utf-8 -*-

from __future__ import division

import cocos
import cocos.collision_model as cm
import pyglet


from game import ozadje
from game import obstacle
from game import player
from game import utils
from game import blocks
from game.resources import resources


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(255, 255, 255, 255)

        self.player = player.Player()
        self.obstacle = obstacle.Obstacle()

        self.collision_manager = cm.CollisionManagerBruteForce()

        self.add(self.player, z=1)
        self.collision_manager.add(self.player)

        self.add(self.obstacle, z=1)
        self.collision_manager.add(self.obstacle)

        self.oblacki = ozadje.Oblacki()
        self.add(self.oblacki, z = 1)

        self.block = blocks.Blocks(resources.block, position =(800,60),velocity=(-20,0))
        self.add(self.block, z=1)
        self.collision_manager.add(self.block)

        self.schedule(self.update)

    def update(self, dt):
        collisions = self.collision_manager.objs_colliding(self.player)
        if collisions:
            if self.obstacle in collisions:
                scene = cocos.scene.Scene()
                scene.add(cocos.layer.MultiplexLayer(
                    YouLostMenu(),
                    OptionsMenu()),
                    z=1
                )
                scene.add(BackgroundLayer(), z=0)
                cocos.director.director.run(scene)
            if self.block in collisions and self.player.position[1] > self.block.position[1] +self.block.height:
                self.player.position = (self.player.position[0],self.block.position[1] + self.player.height/2 + self.block.height/2)
                
                self.player.velocity = (self.player.velocity[0], 0)
                print('in')
            else:
                pass
            
           
          
        

            


class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__()

        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 52
        self.font_title['color'] = (240, 0, 220, 255)

        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['color'] = (240, 0, 220, 255)

        items = []

        items.append(cocos.menu.MenuItem('New game', self.on_new_game))
        items.append(cocos.menu.MenuItem('Options', self.on_options))
        items.append(cocos.menu.MenuItem('Quit', self.on_quit))

        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

    def on_new_game(self):
        game_layer = Game()
        game_scene = cocos.scene.Scene(game_layer)

        cocos.director.director.push(game_scene)

    def on_options(self):
        self.parent.switch_to(1)

    def on_quit(self):
        pyglet.app.exit()


class OptionsMenu(cocos.menu.Menu):
    def __init__(self):
        super(OptionsMenu, self).__init__("two_runner")

        self.font_title["font_name"] = "Edit Undo Line BRK"
        self.font_title["font_size"] = 52
        self.font_title["color"] = (240, 0, 220, 255)

        self.font_item["color"] = (255, 255, 255, 255)
        self.font_item_selected["color"] = (240, 0, 220, 255)

        items = []
        items.append(cocos.menu.MenuItem("Fullscreen", self.on_fullscreen))
        items.append(cocos.menu.MenuItem("Back", self.on_quit))
        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

    def on_fullscreen(self):
        cocos.director.director.window.set_fullscreen(
            not cocos.director.director.window.fullscreen
        )

    def on_quit(self):
        self.parent.switch_to(0)


class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()

        self.image = cocos.sprite.Sprite(resources.background)
        self.image.position = 400, 250
        self.add(self.image, z=0)

        self.player = cocos.sprite.Sprite(resources.mario)
        self.player.position = 200, 250
        self.add(self.player, z=1)

class YouLostMenu(cocos.menu.Menu):
    def __init__(self):
        super(YouLostMenu, self).__init__("YOU LOST")

        self.font_title["font_name"] = "Edit Undo Line BRK"
        self.font_title["font_size"] = 52
        self.font_title["color"] = (240, 0, 220, 255)

        self.font_item["color"] = (255, 255, 255, 255)
        self.font_item_selected["color"] = (240, 0, 220, 255)

        items = []
        items.append(cocos.menu.MenuItem("High Scores", self.on_high_scores))
        items.append(cocos.menu.MenuItem("New Game", self.on_new_game))
        items.append(cocos.menu.MenuItem("Main Menu", self.on_main_menu))
        items.append(cocos.menu.MenuItem("Quit", self.on_quit))
        self.create_menu(items, cocos.menu.shake(), cocos.menu.shake_back())

    def on_high_scores(self):
        pass

    def on_quit(self):
        pyglet.app.exit()

    def on_new_game(self):
        scene = cocos.scene.Scene()
        scene.add(cocos.layer.MultiplexLayer(Game(), OptionsMenu()), z=1)
        scene.add(BackgroundLayer(), z=0)
        cocos.director.director.run(scene)

    def on_main_menu(self):
        scene = cocos.scene.Scene()
        scene.add(cocos.layer.MultiplexLayer(MainMenu(), OptionsMenu()), z=1)
        scene.add(BackgroundLayer(), z=0)
        cocos.director.director.run(scene)

if __name__ == '__main__':
    cocos.director.director.init(width=800, height=500)
    cocos.director.director.window.push_handlers(utils.keys)
    scene = cocos.scene.Scene()
    scene.add(cocos.layer.MultiplexLayer(MainMenu(), OptionsMenu()), z=1)
    scene.add(BackgroundLayer(), z=0)
    cocos.director.director.run(scene)
