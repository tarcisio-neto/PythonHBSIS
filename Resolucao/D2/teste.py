class Ponto:
 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
 
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
 
    def set_x(self, x):
        if x > 0:
            self.__x = x
 
    def set_y(self, y):
        if y > 0:
            self.__y = y
 
p = Ponto(2, 3)
print p.get_x()
p.set_x(10)