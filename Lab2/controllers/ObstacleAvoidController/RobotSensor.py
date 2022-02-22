from controller import DistanceSensor

class RobotSensor(object):

    def __init__(self, robot, sensorName, sensivity, updateRate):
        self.sensor = robot.getDevice(sensorName)
        self.sensor.enable(updateRate)
        self.sensivity = sensivity
        pass
    
    def value(self):
        return self.sensor.getValue() > self.sensivity
