class Solution(object):
    def __init__(self):
        print('New input:\n'
              'nums1 = [1,2,3,0,0,0]\nm = 3\nnums2 = [2,5,6]\nn = 3\n'
              'Expected: nums1 = [1, 2, 2, 3, 5, 6]')
        self.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

        print('New input:\n'
              'nums1 = [1]\nm = 1\nnums2 = []\nn = 0\n'
              'Expected: nums1 = [1]')
        self.merge([1], 1, [], 0)

        print('New input:\n'
              'nums1 = [0]\nm = 0\nnums2 = [1]\nn = 1\n'
              'Expected: nums1 = [1]')
        self.merge([0], 0, [1], 1)

    @staticmethod
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp_nums1 = nums1

        for idx in range(n+m):
            if len(nums2) == 0:  # If nums2 is empty the for loop is not necessary
                break
            else:
                if temp_nums1[idx] > nums2[0]:
                    nums1.insert(idx, nums2[0])
                    nums2.pop(0)
                elif temp_nums1[idx] == 0:
                    nums1[idx] = nums2[0]
                    nums2.pop(0)

        nums1 = nums1[:m+n]  # For case there is still zeros in the end of nums1
        print(f'output: nums1 = {nums1}\n\n')


merge_sorted_array = Solution()
