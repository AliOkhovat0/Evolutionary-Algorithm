import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = 0.5
lenght = 1
width = 1
height = 1

pyrosim.Start_SDF("boxes.sdf")

for column in range(10):
    z_new = z+column
    lenght_new = lenght*(0.9**column)
    width_new = width*(0.9**column)
    height_new = height*(0.9**column)
    for row in range(5):
        x_new = x+row
        for i in range(5):
            y_new = y+i
            pyrosim.Send_Cube(name=f"Box{i*row*column}",
                              pos=[x_new,y_new,z_new] ,
                              size=[lenght_new, width_new, height_new])
    
pyrosim.End()

