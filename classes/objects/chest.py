from container import Container
from book import Book
from coin import Coin
from cheese import Cheese
from key import Key

import random

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