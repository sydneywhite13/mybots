import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/back_sensor_output.npy')
frontLegSensorValues = numpy.load('data/front_sensor_output.npy')

matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label='front leg', linewidth=3)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()