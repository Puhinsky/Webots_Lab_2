from controller import Robot, DistanceSensor, Motor
from RobotSensor import RobotSensor

class RobotController(object):

    def __init__(self):
        self.robot = Robot()
        self.timeStep = int(self.robot.getBasicTimeStep())

        self.leftMotor = self.initMotor('left wheel motor')
        self.rightMotor = self.initMotor('right wheel motor')
        self.initSensors(['ps0', 'ps1', 'ps2', 'ps3', 'ps4','ps5', 'ps6', 'ps7'])
        pass

    def initMotor(self, motorName):
        motor = self.robot.getDevice(motorName)
        motor.setPosition(float('inf'))
        motor.setVelocity(0)
        return motor

    def initSensors(self, sensorsNames):
        self.sensors = []
        for sensorName in sensorsNames:
            sensor = RobotSensor(self.robot, sensorName, 80, self.timeStep)
            self.sensors.append(sensor)
        pass

    def moveForward(self, speed):
        self.leftMotor.setVelocity(speed)
        self.rightMotor.setVelocity(speed)
        pass

    def turnLeft(self, speed):
        self.leftMotor.setVelocity(-speed)
        self.rightMotor.setVelocity(speed)
        pass

    def turnRight(self, speed):
        self.leftMotor.setVelocity(speed)
        self.rightMotor.setVelocity(-speed)
        pass

    def smoothTurnLeft(self, speed, smoothKoefficient):
        self.leftMotor.setVelocity(speed / smoothKoefficient)
        self.rightMotor.setVelocity(speed)
        pass

    def smoothTurnRight(self, speed, smoothKoefficient):
        self.leftMotor.setVelocity(speed)
        self.rightMotor.setVelocity(speed / smoothKoefficient)
        pass

    def leftWall(self):
        return self.sensors[5].value()

    def rightWall(self):
        return self.sensors[2].value()

    def frontLeftWall(self):
        return self.sensors[0].value()

    def frontRightWall(self):
        return self.sensors[7].value()
    
    def leftCorner(self):
        return self.sensors[6].value()

    def rightCorner(self):
        return self.sensors[1].value()