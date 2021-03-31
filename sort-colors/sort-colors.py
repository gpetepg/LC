class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(arr)):
                if arr[i-1] > arr[i]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                    swapped = True