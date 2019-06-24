class Solution1:
    def matrixReshape(self, nums, r, c):
        """类似MATLAB reshape"""
        if len(nums) * len(nums[0]) != r * c:
            return nums
        # 一行
        l = list()
        for row in nums:
            for i in row:
                l.append(i)

        new = list()       
        # for i in range(r):
        #     newin = list()
        #     for j in range(c):
        #         newin.append(l[(i*c)+j])
        #     new.append(newin)
        for j in range(r):
            new.append(l[j*c:j*c+c])

        return new


class Solution2(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            onerow = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
            return [onerow[t * c:(t + 1) * c] for t in range(r)]


sol = Solution1()
print(sol.matrixReshape([[1,2,3],[5,3,4]],3,2))