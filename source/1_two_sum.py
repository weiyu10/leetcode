class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first_num_index in xrange(len(nums)):
            for second_num_index in xrange(len(nums)):
                if nums[first_num_index] + nums[second_num_index] == target:
                    if first_num_index == second_num_index:
                        pass
                    else:
                        return [first_num_index, second_num_index]
                else:
                    pass
