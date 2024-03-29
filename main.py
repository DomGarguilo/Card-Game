import pygame as pg

import save

import ui

import spritesheet
import customsheet

import client
import game
import builder
import menu

from constants import *

def start():
    pg.init()

    pg.display.set_mode((width, height))#, flags=pg.SCALED|pg.RESIZABLE)
    pg.display.set_caption('card game')

    save.init()
    spritesheet.init()
    customsheet.init()
    menu.init()
    client.init()
    game.init()
    builder.init()
    ui.init()
    
    

    ui.menu(menu.main_menu)
        
    pg.quit()


start()