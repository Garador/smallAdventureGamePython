class Item:
    name = ""
    description = ""
    weight = None   #Weight in Grams
    description = None

    def getString(self):
        print "%s / %s / %d" % self.name, self.description, self.weight