from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import keyboard

app = Ursina()
window.borderless = False
mouse.visible = False

player = Entity(model='cube', color=color.red, scale=1, collider='box', position=(5,0,0))
#player = FirstPersonController() to make the game in the first person

keys = ['a', 'w', 'd', 's', 'escape']


def get_input(key):
    player.x += held_keys['d'] * 0.05
    player.x -= held_keys['a'] * 0.05
    player.y += held_keys['w'] * 0.05
    player.y -= held_keys['s'] * 0.05

    if keyboard.is_pressed('escape') and mouse.visible == False:
        mouse.visible = True
    elif keyboard.is_pressed('escape') and mouse.visible == True:
        mouse.visible = False


def update():
    get_input(keys)


box = Entity(model='cube', color=color.magenta, scale=(1, 2, 1)  ,collider='mesh')


camera.parent = player

app.run()