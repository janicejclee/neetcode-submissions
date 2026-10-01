class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #building the dict
        index_of = {}
        for i in range(len(nums)):
            index_of[nums[i]] = i
        
        #loop through nums again and look for compliment in dict
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in index_of and index_of[complement] != j:
                return[j, index_of[complement]]
            

        

        

        

        
        
