def findLongestSubarrayBySum(s, arr):
	result = []
	limit = -1
	sum = 0
	start = 0
	for i in range(len(arr)):
		sum += arr[i]
		while sum > s:
			sum -= arr[start]
			start += 1
		if sum == s:
			if limit < i-start:
				limit = i-start
				result = [start+1, i+1]
	if result:
		return result
	else:
		return [-1]
