import random
import re
from classes.room import Room

class Game:
    finished = False
    path = []
    currentRoom = None
    characterStatus = {
        "leftRoom": False
    }
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
    
    def isValidNumberOption(self, action):
        validAction = re.search(r"^[0-9]{1}$", str(action))
        return validAction is not None
    
    def listDoors(self, room):
        print "You look at the doors..."
        if(room.getDoors()):
            print "There are %d of them..." % len(room.getDoors())
            exitOption = False
            while exitOption is False:
                print "Please select a valid option:"
                action = input("""[1] Enter a door \n[2]See other options \n[3]Listen to door...\n>""")
                validAction = re.search(r"^[0-9]{1}$", str(action))
                if self.isValidNumberOption(action):
                    if int(action) == 1:    #Enter a room
                        strA = ""
                        for x in range(len(room.getDoors())):
                            strA+= "\nDoor #%d" % (x+1)
                        doorNum = input("Please, select the door to open: %s" % strA)
                        if self.isValidNumberOption(doorNum):
                            if int(doorNum)>0 and int(doorNum) <= len(room.getDoors()):
                                if(room.getDoors()[int(doorNum-1)].roomA != room):    #Going to RoomA
                                    self.enterRoom(room.getDoors()[int(doorNum-1)].roomA)
                                else:   #Going to RoomB
                                    self.enterRoom(room.getDoors()[int(doorNum-1)].roomB)
                        else:
                            print("You must select a valid door...")
                    elif int(action) == 2:  #View other options. Exit these options.
                        exitOption = True
                    elif int(action) == 3:  #Listen to door
                        strA = ""
                        for x in range(len(room.getDoors())):
                            strA+= "\nDoor #%d" % (x+1)
                        doorNum = input("Please, select the door to open: %s" % strA+"\n>")
                        if self.isValidNumberOption(doorNum):
                            if int(doorNum)>0 and int(doorNum) <= len(room.getDoors()):
                                targetRoom = room.getDoors()[int(doorNum-1)].roomB
                                if(room.getDoors()[int(doorNum-1)].roomA != room):    #Going to RoomA
                                    targetRoom = room.getDoors()[int(doorNum-1)].roomA
                                if len(targetRoom.getMousetraps()) > 0:
                                    foundMouse = False
                                    for x in range(len(targetRoom.getMousetraps())):
                                        if targetRoom.getMousetraps()[x]._hasMouse:
                                            foundMouse = True
                                            break
                                    if foundMouse:
                                        print("You hear the faint squeal of a small rodent...")
                                    else:
                                        print("You hear only but silence...")
                                else:
                                    print("You hear only but silence...")
                        else:
                            print("You must select a valid door...")
                else:
                    continue
        else:
            print "There are no doors..."
        
    def enterRoom(self, room = Room()):
        self.path.append(room)
        self.currentRoom = room
        print """
        You look around and you see you're in a room.
        """
        while self.characterStatus['leftRoom'] is False:
            action = input("""
        Select an action to perform:

        [1] List the objects in the room.
        [2] List doors
        
        >""")
            validAction = re.search(r"^[0-9]{1}$", str(action))
            if validAction:
                if int(action) == 1:
                    print room.getStringInfo()
                elif int(action) == 2:  #List doors                    
                    result = self.listDoors(room)
            else:
                print "Please select a valid action... %r is not a valida action. " % action

game = Game()
game.start()