class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    # Soution1: array / Time:O(nlogn)/Space :O(n)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
