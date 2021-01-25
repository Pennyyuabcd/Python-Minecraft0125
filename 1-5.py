from mcpi.minecraft import Minecraft
PY=Minecraft.create()
import time
i=1
while True:
    i=i+1
    PY.postToChat("第"+str(i)+"次")
    time.sleep(3)