class Coordinate:
    def __init__(self,id,x,y):
        self.__Id=id
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getId(self):
        return self.__Id
