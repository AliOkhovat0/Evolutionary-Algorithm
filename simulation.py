import pybullet as bullet
import time

physicsClient = bullet.connect(bullet.GUI)
for i in range(1000):
  bullet.stepSimulation()
  time.sleep(1)
bullet.disconnect()
