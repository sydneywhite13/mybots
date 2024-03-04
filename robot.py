from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        #creates neural network
        self.nn = NEURAL_NETWORK("brain.nndf")


    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            print(linkName)

    def Sense(self, t):
        for sensor_name in self.sensors:
            self.sensors[sensor_name].Get_Value(t)


    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            print(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                print(neuronName)
        for motor in self.motors:
            self.motors[motor].Set_Value(self, t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()