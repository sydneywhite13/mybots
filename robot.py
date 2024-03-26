from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        #creates neural network
        self.nn = NEURAL_NETWORK(f'brain{solutionID}.nndf')
        self.solutionID = solutionID
        os.system(f'del brain{solutionID}.nndf')

    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            #print(linkName)

    def Sense(self, t):
        for sensor_name in self.sensors:
            self.sensors[sensor_name].Get_Value(t)


    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            #print(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                #print(neuronName, jointName, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        filename = f'tmp{self.solutionID}.txt'
        f = open(filename, 'w')
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system(f'rename tmp{self.solutionID}.txt fitness{self.solutionID}.txt')
        #os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")
