from mcpi.minecraft import Minecraft
mc = Minecraft.create()

t=0
while True:
    t=t+1
    mc.postToChat(str(t) + 'times')
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat(str(x)+" "+str(y)+" "+str(z))