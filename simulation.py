from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        # for running blind
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravity)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for i in range(c.array_length):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            if self.directOrGUI == 'GUI':
                time.sleep(c.sleep)
            #print(i)
    def __del__(self):
        p.disconnect()
        for sensor in self.robot.sensors:
            self.robot.sensors[sensor].Save_Values()
        #for motor in self.robot.motors:
        #    self.robot.motors[motor].Save_Values()

    def Get_Fitness(self):
        self.robot.Get_Fitness()


