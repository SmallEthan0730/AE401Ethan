# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:13:44 2021

@author: ethan
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()




    
except:
    print('plz enter numbers')
    
name = input('enter your name:')
message = input('enter your message')
mc.postToChat(" <"+ name + "> " + message)

x,y,z = mc.player.getTilePos()
try: 
    a = int(input('enter your block:'))
    mc.setBlock(x,y,z,a)