def find_duplicate(nums):
    num_repet = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in num_repet:
            return num
        num_repet.add(num)
    return False
