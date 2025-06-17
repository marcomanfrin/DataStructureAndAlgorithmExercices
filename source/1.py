def rearrange_list(data):
	result = []
	for i in range(len(data)):
		for j in range(i, len(data)):
			result.append(data[j])
		data = data[1:]
	return result

## TIME AND SPACE COMPLEXITY
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# The time complexity is O(n^2) because we have a nested loop where 
# the outer loop runs n times and the inner loop runs up to n times in the worst case.
# The space complexity is O(n^2) because we are storing the result in a list 
# that can grow up to n^2 elements in the worst case.

##
