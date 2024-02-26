
import math
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.array_length)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.array_length:
            print(self.values)
