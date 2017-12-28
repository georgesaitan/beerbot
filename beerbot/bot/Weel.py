

class Weel(object):
    def __init__(self, pinSet, pinNo1, pinNo2):
        self.pinSet = pinSet
        self.pinNo1 = pinNo1
        self.pinNo2 = pinNo2
        pinSet.initPin(pinNo1)
        pinSet.initPin(pinNo2)

    def forword(self):
        self.pinSet.setPin(self.pinNo1,True)
        self.pinSet.setPin(self.pinNo2, False)

    def back(self):
        self.pinSet.setPin(self.pinNo1, False)
        self.pinSet.setPin(self.pinNo2, True)

    def stop(self):
        self.pinSet.setPin(self.pinNo1, False)
        self.pinSet.setPin(self.pinNo2, False)