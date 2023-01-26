import numpy as np

valuesArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9,
                       10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])


def max_product(values):
    max_a = values[1]
    max_b = values[0]

    for i in range(len(values) - 1):

        if values[i] > max_a:
            max_a = values[i]

        if values[i + 1] > max_b:
            print(i, max_b)
            max_b = values[i+1]
                

    # print(max_a)
    
    return max_a * max_b


print(max_product(valuesArray))
