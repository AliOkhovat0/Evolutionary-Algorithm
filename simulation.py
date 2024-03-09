import pybullet as bullet
import pybullet_data
import time

physicsClient = bullet.connect(bullet.GUI)
bullet.setAdditionalSearchPath(pybullet_data.getDataPath())
bullet.setGravity(0,0,-9.8)
planeId = bullet.loadURDF("plane.urdf")
#robotId = bullet.loadURDF("body.urdf")
robotId2 = bullet.loadURDF("body2.urdf")
bullet.loadSDF("world.sdf")

while True:
  bullet.stepSimulation()
  time.sleep(0.01)

bullet.disconnect() 
