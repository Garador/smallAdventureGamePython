from objects.door import Door
from objects.chest import Chest
from objects.mouseTrap import MouseTrap
import random

class Room:
    _chests = None
    _mouseTraps = None
    _doors = None
    _roomId = None

    def getChests(self):
        if self._chests is None:
            self._chests = []
            for x in range(0, random.randint(0,3)):
                self._chests.append(Chest())
        return self._chests;

    def getDoors(self):
        if self._doors is None:
            self._doors = []
            for x in range(0, random.randint(1,5)):
                newDoor = Door()
                newDoor.roomA = self
                newDoor.roomB = Room()
                self._doors.append(newDoor)
        return self._doors
    
    def getMousetraps(self):
        if self._mouseTraps is None:
            self._mouseTraps = []
            for x in range(0, random.randint(0,3)):
                self._mouseTraps.append(MouseTrap())
        return self._mouseTraps
    
    def getRoomID(self):
        if self._roomId is None:
            self._roomId = random.randint(1, 60000)
        return self._roomId
    
    def getStringInfo(self):
        return "%r Chests. %r Mousetraps. %r doors. It also has a plaque with the text \"%r\" as the room number." % (len(self.getChests()), len(self.getMousetraps()), len(self.getDoors()), self.getRoomID())
