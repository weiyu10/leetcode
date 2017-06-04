class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        for first_num in nums:
            y = 0
            for second_num in nums:
                if first_num + second_num == target:
                    if x == y:
                        pass
                    else:
                        return [x, y]
                else:
                    pass
                y = y + 1
            x = x + 1


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
