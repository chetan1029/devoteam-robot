"""Writing test cases for thr program."""


from robot import Robot
from room import Room
import unittest

class RobotTest(unittest.TestCase):

    def test_room(self):
        """Test room."""


        room = Room(5,5)
        self.assertTrue(room.robotinroom(2,3))
        self.assertTrue(room.robotinroom(1,3))
        self.assertTrue(room.robotinroom(0,4))
        self.assertFalse(room.robotinroom(1,5))
        self.assertFalse(room.robotinroom(6,3))
        self.assertFalse(room.robotinroom(5,6))

    def test_callcommands(self):
        """Test commands"""


        room = Room(5,5)
        robot = Robot(1,2,"N",room)
        robot.callcommands("RFRFFRFRF")
        result = robot.printresult()
        self.assertEqual(result, "1 3 N")

        room = Room(5,5)
        robot = Robot(0,0,"E",room)
        robot.callcommands("RFLFFLRF")
        result = robot.printresult()
        self.assertEqual(result, "3 1 E")

    def test_rightturn(self):
        """Test Right turn."""


        room = Room(5,5)
        robot = Robot(1,2,"N",room)
        robot.turnright()
        self.assertEqual(robot.formatdirection(), "E")
        robot.turnright()
        self.assertEqual(robot.formatdirection(), "S")

    def test_leftturn(self):
        """Test Left turn."""


        room = Room(5,5)
        robot = Robot(1,2,"N",room)
        robot.turnleft()
        self.assertEqual(robot.formatdirection(), "W")
        robot.turnleft()
        self.assertEqual(robot.formatdirection(), "S")

    def test_moveforward(self):
        """Test moving forward of Robot."""


        room = Room(5,5)
        robot = Robot(1,2,"N",room)
        robot.moveforward()
        self.assertEqual(robot.wide, 1)
        self.assertEqual(robot.deep, 1)

        room = Room(5,5)
        robot = Robot(0,0,"N",room)
        self.assertRaises(Exception, robot.moveforward())



if __name__ == '__main__':
    unittest.main()