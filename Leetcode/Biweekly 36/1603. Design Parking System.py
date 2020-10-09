# Question Link:- https://leetcode.com/problems/design-parking-system/

class ParkingSystem:
    
    # initialized the values for small, medium and big cars spaces available.
    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small
    
    # if  space is available for given type of car then return True else False
    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.b>0:
                self.b-=1
                return True
            else:
                return False
        if carType==2:
            if self.m>0:
                self.m-=1
                return True
            else:
                return False
        if carType==3:
            if self.s>0:
                self.s-=1
                return True
            else:
                return False
