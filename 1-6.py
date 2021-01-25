from mcpi.minecraft import Minecraft
PY=Minecraft.create()
PY.postToChat("I'm watching you")
while True:
  X,Y,Z=PY.player.getTilePos()
  PY.postToChat(" X:"+str(X)+" Y:"+str(Y)+" Z:"+str(Z))