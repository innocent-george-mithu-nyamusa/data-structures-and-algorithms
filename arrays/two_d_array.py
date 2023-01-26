import numpy as np
import time as tm

twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [
                     9, 10, 11, 12], [13, 14, 15, 16]])
# print(twoDArray)

start_time = tm.time()
other2Darray = np.insert(
    twoDArray, [[17, 18, 19, 20], [21, 22, 23, 24]], axis=0)

passed_time = tm.time() - start_time
# print(passed_time)
print(other2Darray)

