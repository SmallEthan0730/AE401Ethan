# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:09:35 2021

@author: ethan
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("Block ID: " + str(block))
        
