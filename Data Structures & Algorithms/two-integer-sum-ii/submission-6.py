class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1               # 1‑based left pointer
        j = len(numbers)    # 1‑based right pointer (last element)

        while i < j:
            cur = numbers[i-1] + numbers[j-1]   # convert to 0‑based for access
            if cur > target:
                j -= 1        # move right pointer left
            elif cur < target:
                i += 1        # move left pointer right
            else:
                return [i, j] # already 1‑based, no +1 needed