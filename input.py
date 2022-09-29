"""User friendly Inputs from this class"""


from robot import Robot
from room import Room
import re

class RobotInput:


    def isvalidcommand(self, command):
        """Check if command is valid and have only R,L,F charactors."""


        return re.search(r'^[RFL]+$', command) is not None


    def robotinput(self):
        """Promot and take user input and validate them until user enter valid inputs."""

        
        while True:
            try:
                room_size = input("Enter wide and deep for the room like 5 7: ")
                wide, deep = room_size.strip().split(" ")
                room = Room(wide, deep)
            except ValueError:
                print("Please enter valid value for wide and deep like 5 5")
                continue
            else:
                break
                
        while True:
            try:
                starting_point = input("Enter your Starting Point: ")
                start_wide, start_deep, direction = starting_point.strip().split(" ")
                robot = Robot(start_wide, start_deep, direction, room)
            except ValueError:
                print("Please enter valid start wide, start deep and direction like 1 2 N")
                continue
            else:
                break

        while True:
            commands = input("Enter moving commands for Robot: ")
            if self.isvalidcommand(commands):
                robot.callcommands(commands.strip())
                break
            else:
                print("Enter valid values consist of R (right turn), L (left turn), F (move forward): RLRFFRF")
                continue

        output = robot.printresult()
        print("Current position of Robot: ", output)

        

robotinput = RobotInput()
robotinput.robotinput()


