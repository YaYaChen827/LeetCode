def singleNumber_BigOn(nums):
	result = set()
	for n in nums:
		if n in result:
			result.remove(n)
		else:
			result.add(n)
	return list(result)

def singleNumber(nums):
	bit_num = 0
	for num in nums:
		bit_num ^= num
		print bit_num

print singleNumber([1,2,1,3,2,5])
#print singleNumber([0,0,1,2])
#print singleNumber([-1,0])