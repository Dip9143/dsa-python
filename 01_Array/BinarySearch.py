def BinarySearch(nums, key=999):
	low = 0
	high = len(nums) - 1
	steps = 0

	while (low <= high):
		steps += 1
		mid = int ((high + low)/2)

		if nums[mid] == key:
			print("Found")
			print("Steps: ", steps)
			return
		elif nums[mid] < key:
			low = mid + 1
		elif nums[mid] > key:
			high = mid - 1


nums = list(range(1000))
BinarySearch(nums)
