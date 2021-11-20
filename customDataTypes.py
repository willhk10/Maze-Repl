class ListNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        return
    
    def hasParent(self):
        return self.parent != None

    def hasValue(self, value):
        if self.data == value:
            return True
        else:
            return False
    
    def findGrandparent(self):
        if self.hasParent():
            if self.parent.hasParent():
                self.grandparent = self.parent.parent
                return self.grandparent
    
    def findRoot(self):
        curNode = self
        while curNode.hasParent():
            curNode = curNode.parent
        return curNode

class PriorityQueue():
    def __init__(self):
        self.items = []
        self.allData = []

    def insert(self, data, priority):
        self.items.append((data, priority))
        self.allData.append(data)
    
    def popHighest(self):
        maxPriority = max([self.items[i][1] for i in range(len(self.items))])
        for i in range(len(self.items)):
            if self.items[i][1] == maxPriority:
                self.allData.remove(self.items[i][0])
                return self.items.pop(i)[0]
    
    def popLowest(self):
        minPriority = min([self.items[i][1] for i in range(len(self.items))])
        for i in range(len(self.items)):
            if self.items[i][1] == minPriority:
                self.allData.remove(self.items[i][0])
                return self.items.pop(i)[0]
    
    def print(self):
        for i in range(len(self.items)):
            print(self.items[i])
