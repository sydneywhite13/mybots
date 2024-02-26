import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import math
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        print(jointName)


    # modify so that one motor oscillates at half the frequency of the other
    # must include conditional statement dependent on self.jointName
    def Prepare_To_Act(self):
        if self.jointName == 'Torso_BackLeg':
            self.amplitude = c.amplitude
            self.frequency = c.frequency*0.5
            self.offset = c.offset
        else:
            self.amplitude = c.amplitude
            self.frequency = c.frequency
            self.offset = c.offset
        self.motorValues = numpy.sin(
            (numpy.linspace(0, 2 * math.pi, 1000) * self.frequency) + self.offset) * self.amplitude

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot.robotId,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motorValues[t],

            maxForce=c.max_force)

    def Save_Values(self):
        numpy.save((f'data/%s.npy' % self.jointName), self.motorValues)


