import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/sensor_output.npy')
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()