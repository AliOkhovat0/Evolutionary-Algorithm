import pybullet as bullet
import time

physicsClient = bullet.connect(bullet.GUI)
bullet.loadSDF("box.sdf")

for i in range(1000):
  bullet.stepSimulation()
  time.sleep(0.1)

bullet.disconnect() 
