from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravity)

        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for i in range(c.array_length):
            p.stepSimulation()
            self.robot.Sense(i)
            '''
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
            '''
            time.sleep(c.sleep)
            #print(i)
    def __del__(self):
        p.disconnect()


