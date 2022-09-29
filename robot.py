"""Robot class that have functions to operate robot."""

class Robot:

    directionstrtoint = {
            "N": 0,
            "E": 1,
            "S": 2,
            "W": 3
        }

    directioninttostr = {
            0:"N",
            1: "E",
            2: "S",
            3: "W"
        }
    
    def __init__(self, wide, deep, direction, room):
        """
        Parameters
        wide: int
            Starting wide position of the robot
        deep: int
            Starting deep position of the robot
        direction: str
            Direction of the robot facing towards
        """


        self.room = room
        self.wide = int(wide)
        self.deep = int(deep)
        self.direction = self.directionstrtoint.get(direction, -1)
    
    def turnright(self):
        """Turn right from the direction robot facing currenctly."""


        self.direction = (self.direction+1)%4

    def turnleft(self):
        """Turn left from the direction robot facing currenctly."""


        self.direction = (self.direction-1)%4

    def moveforward(self):
        """Take a step forward in the direction robot facing right now."""


        newwide = self.wide
        newdeep = self.deep
        if self.direction == 0:
            newdeep -= 1
        elif self.direction == 1:
            newwide += 1
        elif self.direction == 2:
            newdeep += 1
        elif self.direction == 3:
            newwide -= 1

        if self.room.robotinroom(newwide, newdeep):
            self.wide = newwide
            self.deep = newdeep
        else:
            raise Exception("Robot is facing towards wall")

    def formatdirection(self):
        """Get direction name from the repsenting number."""


        return self.directioninttostr.get(self.direction)

    def callcommands(self, commands):
        """Call command to make robot move or turn."""


        for command in commands:
            if command == "R":
                self.turnright()
            elif command == "L":
                self.turnleft()
            elif command == "F":
                self.moveforward()

    def printresult(self):
        """Print final result with wide, deep and direction robot is facing."""

        
        return ("{} {} {}".format(self.wide, self.deep, self.formatdirection()))


    

    
