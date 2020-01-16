#import team3200
#import commandbased

from wpilib import TimedRobot
from wpilib import Talon

class Robot(TimedRobot):

    def robotInit(self):
        '''This is where the robot code starts.'''
        self.talon = Talon(1)

    def autonomousPeriodic(self):
        self.talon.set(.5)
    
    def teleopInit(self):
        self.talon.set(0)
