"""ObstacleAvoidController controller."""

from RobotController import RobotController

robotController = RobotController()

speed = 1



while robotController.robot.step(robotController.timeStep) != -1:

    #if robotController.sensors[0].value() & robotController.sensors[7].value() & robotController.sensors[1].value() & robotController.sensors[6].value():
    #    robotController.moveForward(1)
   # else:
    #    if(robotController.sensors[5].value()):
    ##        robotController.turnOnPlace(-1)
    #    elif(robotController.sensors[2].value()):
    #        robotController.turnOnPlace(1)

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
