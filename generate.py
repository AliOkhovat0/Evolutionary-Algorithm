import pyrosim.pyrosim as pyrosim

def Create_World():
    x = 1.5
    y = 1.5
    z = 1.5
    lenght = 1
    width = 1
    height = 1
    
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[lenght, width, height])
    pyrosim.End()

def Create_Robot():
    x = 0
    xj = 0
    y = 0
    yj = 0
    z = 0.5
    zj = 1
    lenght = 1
    width = 1
    height = 1
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z], size=[lenght, width, height])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute",
                       position = [xj,yj,zj])
    pyrosim.Send_Cube(name="Link1",
                      pos=[x,y,z],
                      size=[lenght, width, height])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute",
                       position = [xj,yj,zj])
    pyrosim.Send_Cube(name="Link2",
                      pos=[x,y,z],
                      size=[lenght, width, height])
    pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute",
                       position = [xj+1,yj,zj-1])
    pyrosim.Send_Cube(name="Link3",
                      pos=[x,y,z],
                      size=[lenght, width, height])
    pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute",
                       position = [xj+1,yj,zj-1])
    pyrosim.Send_Cube(name="Link4",
                      pos=[x,y,z],
                      size=[lenght, width, height])
    pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute",
                       position = [xj,yj,zj-2])
    pyrosim.Send_Cube(name="Link5",
                      pos=[x,y,z],
                      size=[lenght, width, height])
    pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute",
                       position = [xj,yj,zj-2])
    pyrosim.Send_Cube(name="Link6",
                      pos=[x,y,z],
                      size=[lenght, width, height])
    pyrosim.End()

def Create_Robot2():
    x = 0
    xj = -0.5
    y = 0
    yj = 0
    z = 1.5
    zj = 1
    lenght = 1
    width = 1
    height = 1
    pyrosim.Start_URDF("body2.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[lenght, width, height])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute",
                       position = [xj,yj,zj])
    pyrosim.Send_Cube(name="BackLeg",
                      pos=[x-0.5,y,z-2],
                      size=[lenght, width, height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute",
                       position = [0.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", 
                      pos=[x+0.5,y,z-2],
                      size=[lenght, width, height])
    pyrosim.End()

#Create_Robot()
Create_Robot2()
Create_World()
