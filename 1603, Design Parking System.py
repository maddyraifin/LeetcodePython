# Reference: https://leetcode.com/problems/design-parking-system/
# Sequence = 1603. Design Parking System
# Prepared by - Maddy Rai
import time


class ParkingSystem:
    dtypes = dict()
    count = 999

    def __init__(self, big, medium, small):
        if big not in range(0, 10001) or medium not in range(0, 10001) or small not in range(0, 10001):
            raise Exception("Inputs are out of range.")

        self.dtypes[1] = big
        self.dtypes[2] = medium
        self.dtypes[3] = small

    def addCar(self, carType):
        self.count = self.count - 1
        if self.count < 0:
            raise Exception("Maxnium number of calls exceeded.")

        if carType not in self.dtypes.keys():
            raise Exception("Unexpected carType.")

        bcase = False
        if self.dtypes[carType] > 0:
            self.dtypes[carType] = self.dtypes[carType] - 1
            bcase = True

        return bcase


obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
print(param_1)
param_1 = obj.addCar(2)
print(param_1)
param_1 = obj.addCar(3)
print(param_1)
param_1 = obj.addCar(1)
print(param_1)

tic = time.perf_counter()
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")