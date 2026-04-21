class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
value = int(input("Enter sum for which you want to make this search : "))
print(pair_elements().twoSum((1,2,3,4,5,6),value))
