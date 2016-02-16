class Box:
    def __init__(self, height, width, breadth):
        self.height = height
        self.width = width
        self.breadth = breadth

    def getVolume(self):
        height = input("Please enter the Height: ")
        width = input("Please enter the Width: ")
        breadth = input("Please enter the Breadth: ")

        sArea = (width * height + breadth * height + width * breadth) * 2
        return sArea

        bVolume = (width * height * breadth)
        return bVolume
