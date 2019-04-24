import random
from item import Item

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