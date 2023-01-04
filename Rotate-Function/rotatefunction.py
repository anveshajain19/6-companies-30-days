class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
	    a = sum(nums)
	    n = len(nums)
	    res = sum(i*j for i,j in enumerate(nums)) 
	    total = res                           
	    for i in range(len(nums)):
		    total += n*nums[i] - a 
		    res = max(res, total)
	    return res