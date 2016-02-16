class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def getVolume(self):
        radius = input("Please enter the Radius: ")

        sArea = (4 * 3.14 * radius * radius)
        return sArea

        sVolume = ((4/3) * 3.14 * radius * radius * radius)
        return sVolume
