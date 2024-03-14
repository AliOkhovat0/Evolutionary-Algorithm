import pybullet as bullet
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy as np
import random
import time

amplitude = np.pi/4
frequency = 50
phaseOffset = 0
amplitude2 = np.pi/4
frequency2 = 50
phaseOffset2 = np.pi/2

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

targetAngles = np.linspace(-np.pi/4, np.pi/4, 10000)
motorSignal = amplitude*np.sin(frequency*targetAngles+phaseOffset)
motorSignal2 = amplitude2*np.sin(frequency2*targetAngles+phaseOffset2)

for i in range(10000):
  bullet.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  pyrosim.Set_Motor_For_Joint(bodyIndex=robotId2, jointName="Torso_BackLeg",
                              controlMode=bullet.POSITION_CONTROL, 
                              targetPosition=motorSignal[i],
                              maxForce=40)
  pyrosim.Set_Motor_For_Joint(bodyIndex=robotId2, jointName="Torso_FrontLeg",
                              controlMode=bullet.POSITION_CONTROL, 
                              targetPosition=motorSignal2[i],
                              maxForce=40)
  time.sleep(0.01)

bullet.disconnect() 
np.save('data//backLegSensorValues.npy',backLegSensorValues)
np.save('data//frontLegSensorValues.npy',frontLegSensorValues)