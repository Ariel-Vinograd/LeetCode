class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp_nums1 = nums1

        for idx, val in enumerate(temp_nums1):
            if len(nums2) == 0:
                if nums1[-1] == 0:
                    nums1.pop(-1)
                break

            if temp_nums1[idx] > nums2[0]:
                nums1.insert(idx, nums2[0])
                nums2.pop(0)
            elif temp_nums1[idx] == 0:
                nums1[idx] = nums2[0]
                nums2.pop(0)
            print("nums1", nums1)

