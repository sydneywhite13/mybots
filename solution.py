import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import constants as c
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Start_Simulation(self, direct_or_gui):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + direct_or_gui + ' ' + str(self.myID))
        # os.system(f'start /B python3 simulate.py {direct_or_gui} {self.myID}')
        # os.system(f'python3 simulate.py {direct_or_gui}')

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f'fitness{self.myID}.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, 'r')
        self.fitness = float(f.read())
        f.close()
        os.system(f'del fitness{self.myID}.txt')
        #print(self.fitness)


    def Evaluate(self, direct_or_gui):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + direct_or_gui + ' ' + str(self.myID))
        # os.system(f'start /B python3 simulate.py {direct_or_gui} {self.myID}')
        # os.system(f'python3 simulate.py {direct_or_gui}')

        fitnessFileName = f'fitness{self.myID}.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, 'r')
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[c.box_x, c.box_y, c.box_z], size=[c.length, c.width, c.height])
        pyrosim.End()

        while not os.path.exists("world.sdf"):
            time.sleep(0.01)

    def Create_Robot(self):
        pyrosim.Start_URDF("body.urdf")
        # x,y,z = 0, 0, 0.5 length, width, height = 1,1,1
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[c.length, c.width, c.height])
        # only the root link has absolute position, everything else is relative to its upstream joint

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[c.length, c.width, c.height])

        pyrosim.End()

        while not os.path.exists("body.urdf"):
            time.sleep(0.01)


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f'brain{self.myID}.nndf')

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

        while not os.path.exists(f'brain{self.myID}.nndf'):
            time.sleep(0.01)

    def Mutate(self):
        row = random.randint(0, 2)
        column = random.randint(0, 1)
        self.weights[row, column] = random.random()* 2 - 1

