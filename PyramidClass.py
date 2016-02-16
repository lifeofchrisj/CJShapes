import math

class Pyramid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        

    def getVolume(self):
        length = input("Please enter the length: ")
        width = input("Please enter the width: ")
        height = input("Please enter the height: ")
        
        
        

        sArea = (length * width + length.sqrt((width/2)**2 + height**2 + width.sqrt((length/2)**2 + height**2))
        return sArea

        sVolume = ((length * width * height)/3)
        return sVolume
