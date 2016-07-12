#Given an array of integers, every element appears twice except for one. 
#Find that single one.

#Note:
#Your algorithm should have a linear runtime complexity. 
#Could you implement it without using extra memory?

#Subscribe to see which companies asked this question




from operator import xor

def singleNumber(nums):
	result = 0
	for num in nums:
		result = xor(result, num)
	return result


print singleNumber([1,1,2,3,2])