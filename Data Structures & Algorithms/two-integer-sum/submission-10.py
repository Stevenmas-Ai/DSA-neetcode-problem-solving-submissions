class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using brute force
        # target
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

         #using hashmap
         target
         prevMap={}
         for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i


                   