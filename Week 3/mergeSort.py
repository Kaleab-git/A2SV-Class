class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        myList = nums
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            self.sortArray(left)
            self.sortArray(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    myList[k] = left[i]
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                myList[k]=right[j]
                j += 1
                k += 1
        return myList