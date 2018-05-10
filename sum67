def sum67(nums):
	total = 0
	marker = 0
	for num in nums:
		if num == 6:
			marker = 1
			continue
		if marker == 1:
			continue
		if num == 7 and marker == 1:
			marker = 0
			continue
		if num != 6 and marker == 0:
			total += 1
	return total
