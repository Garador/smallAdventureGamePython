import random
import re

class Item:
    name = ""
    description = ""
    weight = None   #Weight in Grams
    description = None

    def getString(self):
        print "%s / %s / %d" % self.name, self.description, self.weight

class Coin(Item):
    name = "Gold Coin"
    description = "Large Gold Coin"
    weight = 10.0

class Cheese(Item):
    name = "Cheese"
    description = "A small piece of cheese. Maybe you shouldn't eat it..."
    weight = 120.0

class Book(Item):
    name = "Book"
    description = "An ancient book with some weird drawings..."
    weight = 3800

class Key(Item):
    keys_found = {
        "Blue": False,
        "Green": False,
        "Yellow": False,
        "Orange": False,
        "Red": False
    }

    color = None

    def __init__(self):
        color = "Red"
        colors = [
            "Blue",
            "Green",
            "Yellow",
            "Orange",
            "Red"
        ]
        color_i = random.randint(0,4)
        self.color = colors[color_i]
        Key.keys_found[color] = True


    @property
    def name(self):
        return "%s Key" % self.color | "Common"
    
    @property
    def description(self):
        return "This is a %s key. It's %s." % ("Special" if self.color is not "Common" else "common lost key."), "very lightweight." if self.color is not "Common" else "lightweight."
    
    @property
    def weight(self):
        return 5.0 if self.color is not "Common" else 10.0

class Container():
    items = []

    def addItem(self, item):
        self.items.append(item)

class Chest(Container):
    def __init__(self):
        self.setRandomItems(random.randint(2,12))
    
    def setRandomItems(self, number):
        for x in range(number-1):
            item = None
            itemType = random.randint(1,4)
            if itemType == 1:
                item = Coin()
            elif itemType == 2:
                item = Cheese()
            elif itemType == 3:
                item = Book()
            self.addItem(item)
        if random.randint(0, 5) == 5:  #1/5 chances of getting a key
            self.items.append(Key())

class MouseTrap:
    _hasMouse = bool
    def __init__(self):
        self._hasMouse = True if random.randint(1, 10) == 1 else False

class Door:
    roomA = None  #Room
    roomB = None  #Room

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
        return []
    
    def getRoomID(self):
        if self._roomId is None:
            self._roomId = random.randint(1, 60000)
        return self._roomId
    
    def getStringInfo(self):
        return "%r Chests. %r Mousetraps. %r doors. It also has a plaque with the text \"%r\" as the room number." % (len(self.getChests()), len(self.getMousetraps()), len(self.getDoors()), self.getRoomID())

class Game:
    finished = False
    path = []
    def start(self):
        print """
        %s
        You wake up in a strange place...
        You don't have a memory of this place...
        %s
        """ % ("*"*40 , "*"*40)
        while self.finished is False:
            currentRoom = Room()
            self.path.append(currentRoom)
            self.enterRoom(currentRoom)
        
    def enterRoom(self, room = Room()):
        print """
        You look around and you see you're in a room.
        """

        leftRoom = False
        while leftRoom is False:
            action = input("""
        Select an action to perform:

        [1] List the objects in the room.
        """)
            print "ENTERED: %r " % action
            validAction = re.match("/^[0-9]{1}$/", str(action))
            if int(action) == 1:
                print room.getStringInfo()
            else:
                print "Please select a valid action... %r is not a valida action. " % action

game = Game()
game.start()