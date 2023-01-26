################ Date 13 Sept 2022

def sumOfPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)
                
                
first = [1, 3, 4, 5, 6, 10, 15, 17, 19, 20, 26]
sumOfPairs(first, 6)