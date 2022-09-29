"""Room class to represent how wide and deep room is."""


class Room:

    def __init__(self, wide, deep):
        """
        wide: int
            how wide is room
        deep: int
            how wide is room
        """


        self.wide = int(wide)
        self.deep = int(deep)

    def robotinroom(self, newwide, newdeep):
        """Function to check if robot starting points in the room or not."""

        
        if newwide < self.wide and newdeep < self.deep:
            return True
        else:
            return False

