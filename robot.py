"""
Base file that setups basic robot. Actual robot is in team3200 module.
This file should not need to be edited.
"""
import wpilib
from team3200 import Robot as Robot

if __name__ == '__main__':
    wpilib.run(Robot, physics_enabled=True)

