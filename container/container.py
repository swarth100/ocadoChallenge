import sys

class Container:

    def __init__(self):
        # Initialise dimensions
        self.height = sys.maxsize
        self.length = sys.maxsize
        self.width = sys.maxsize

        self.items = []

    def __len__(self):
        return len(self.items)

    def addItem(self, item):
        self.items.append(item)

    def getLastItemOrder(self):
        if len(self.items) >= 1:
            return self.items[-1].orderID
        return 0

    def getItemWeights(self):
        res = 0

        for item in self.items:
            res += item.weight

        return res

    def getItemVolumes(self):
        res = 0

        for item in self.items:
            res += item.volume

        return res

    def getSeg(self):

        segMin = 10
        segMax = 0

        for item in self.items:
            if item.category >= 9:
                continue
            if item.category > segMax:
                segMax = item.category

            if item.category < segMin:
                segMin = item.category

        segMinVal = False
        if 1 <= segMin <= 4:
            segMinVal = True

        if 5 <= segMax <= 8:
            if segMinVal:
                return "MIX"
            else:
                return "HIG"
        else:
            return "LOW"

    def getDry(self):

        dryItems = [1, 2, 5, 6]

        dryList = []
        wetList = []

        for item in self.items:
            if item.category in dryItems:
                dryList.append(item)
            else:
                wetList.append(item)

        if len(dryList) == 0:
            return "WET"
        if len(wetList) == 0:
            return "DRY"
        return "MIX"




