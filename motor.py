import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset

        pyrosim.Set_Motor_For_Joint(

            bodyIndex=self.robotId,

            jointName="Torso_BackLeg",

            controlMode=p.POSITION_CONTROL,

            targetPosition=backLegTargetAngles[i],

            maxForce=c.max_force)

        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robotId,

            jointName="Torso_FrontLeg",

            controlMode=p.POSITION_CONTROL,

            targetPosition=frontLegTargetAngles[i],

            maxForce=c.max_force)
