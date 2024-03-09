import pybullet as bullet
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy as np
import time

physicsClient = bullet.connect(bullet.GUI)
bullet.setAdditionalSearchPath(pybullet_data.getDataPath())
bullet.setGravity(0,0,-9.8)
planeId = bullet.loadURDF("plane.urdf")
#robotId = bullet.loadURDF("body.urdf")
robotId2 = bullet.loadURDF("body2.urdf")
bullet.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId2)
backLegSensorValues = np.zeros(10000)
frontLegSensorValues = np.zeros(10000)

for i in range(10000):
  bullet.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  time.sleep(0.001)

bullet.disconnect() 
np.save('data//backLegSensorValues.npy',backLegSensorValues)
np.save('data//frontLegSensorValues.npy',frontLegSensorValues)