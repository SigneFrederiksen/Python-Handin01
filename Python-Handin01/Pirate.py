# Pirate Class

class Pirate :
    # Constructor
    def __init__(self, name, pointer = None) :
        self._name = name
        self._pointer = pointer

    # Get name value
    def getName(self) :
        return self._name
    # Get pointer value
    def getPointer(self) :
        return self._pointer
    # Set pointer value
    def setPointer(self, pointer) :
        self._pointer = pointer

     # Method - toString
    def toString(self) :
        return self.getName() + " points to " + self.getPointer()
