class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def compute(avaiable_nums, current_position):
            if current_position == 1:
                return 1

            total = 0
            for num_index in range(len(avaiable_nums)):
                num = avaiable_nums[num_index]
                if (num % current_position) == 0 or (current_position % num) == 0:
                    total += compute(avaiable_nums[0:num_index]+avaiable_nums[num_index+1:], current_position-1)
                else:
                    pass
            return total

        return compute(tuple(range(0+1, N+1)), N)
