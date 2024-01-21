import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
# note: change the z variable to half the height to prevent the simulator from growing the link
z = 0.5

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
x2 = 1
y2 = 0
z2 = 1.5
pyrosim.Send_Cube(name="Box2", pos=[x2, y2, z2] , size=[length, width, height])
pyrosim.End()