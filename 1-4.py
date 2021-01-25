from mcpi.minecraft import Minecraft
import time
PY=Minecraft.create()
X=200
Y=200
Z=100
PY.player.setTilePos(X,Y,Z)
time.sleep(2)
X=150
Y=150
PY.player.setTilePos(X,Y,Z)
time.sleep(2)
X=100
Y=100
PY.player.setTilePos(X,Y,Z)