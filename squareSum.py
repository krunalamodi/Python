## functions
def ss(nums):
	total = 0
	for i in range(len(nums)):
		#print(nums[i] ** 2)
		total += (nums[i] ** 2)
	return total

def mysum(i, nums):
	if (len(nums) == i):
		return 0
	else:
		return (nums[i] ** 2) + mysum(i+1, nums)

def ssRecur(nums):
	return mysum(0, nums)

## __Main code__
ans_iter  =      ss([1, 2, 3, 4])
ans_recur = ssRecur([1, 2, 3, 4])
print ("Answer using iterative version: ", ans_iter)
print ("Answer using recursive version: ", ans_recur, end="")