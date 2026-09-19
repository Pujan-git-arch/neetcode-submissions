class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left= 0
        right= len(numbers)-1
        while left < right:
            currentsum=numbers[left]+numbers[right]
            if currentsum>target:
                right=right-1
            elif currentsum<target:
                left=left+1
            elif target==currentsum:
                return [left+1,right+1]