
import math
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.sin(
            (numpy.linspace(0, 2 * math.pi, 1000) * c.frontLegFrequency) + c.frontLegPhaseOffset) * c.frontLegAmplitude

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.array_length:
            print(self.values)
