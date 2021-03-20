from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(1000):
    mc.setBlock(x,y-1,z+i,1)
    
    
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(100):
    mc.setBlocks(x+i,y-1,z+i,x+i,y-1,z+i+3,1)
    
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

for i in range(10):
    mc.setBlocks(x+i,y-1,z+i,x+i,y-1,z+i+3,1)