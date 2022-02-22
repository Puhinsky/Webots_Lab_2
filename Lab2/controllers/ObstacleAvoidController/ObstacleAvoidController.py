"""ObstacleAvoidController controller."""

from RobotController import RobotController

robotController = RobotController()
speed = 1

while robotController.robot.step(robotController.timeStep) != -1:
    if robotController.frontLeftWall():
        robotController.turnLeft(speed)
    else:
        if robotController.rightWall():
            robotController.moveForward(speed)
        else:
            robotController.smoothTurnRight(speed, 4)
        if robotController.rightCorner():
            robotController.smoothTurnLeft(speed, 4)
    pass
