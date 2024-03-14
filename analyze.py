import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data//backLegSensorValues.npy')
plt.plot(backLegSensorValues, label='Back-Leg Sensor Values', linewidth=2)

backLegSensorValues = np.load('data//frontLegSensorValues.npy')
plt.plot(backLegSensorValues, label='Front-Leg Sensor Values')
plt.legend()
plt.show()

TargetAngles = np.load('data/linSpace.npy')
plt.plot(TargetAngles, color='black',linewidth=2, label='targetAngles')
plt.legend()
plt.show()