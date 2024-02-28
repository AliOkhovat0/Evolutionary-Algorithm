import pybullet as bullet
import pybullet_data
import time

physicsClient = bullet.connect(bullet.GUI)
bullet.setAdditionalSearchPath(pybullet_data.getDataPath())
bullet.setGravity(0,0,-9.8)
planeId = bullet.loadURDF("plane.urdf")
bullet.loadSDF("boxes.sdf")

while True:
  bullet.stepSimulation()
  time.sleep(0.01)

bullet.disconnect() 
