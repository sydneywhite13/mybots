import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import math
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        #self.Prepare_To_Act()
        print(jointName)

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robotId,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=desiredAngle,

            maxForce=c.max_force)

