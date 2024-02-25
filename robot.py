from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pybullet_data

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.robotId = p.loadURDF("body.urdf")