class Solution:
    def rotate(self, nums, k):
        """
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums[len(nums)-1])
            nums.pop()

        return nums


class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]


sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7],3))


# Java 编写，逻辑简单，四种方法（准确的说是3种）

# import java.util.Arrays;

# class Solution {
#     /**
#      * 双重循环
#      * 时间复杂度：O(kn)
#      * 空间复杂度：O(1)
#      */
#     public void rotate_1(int[] nums, int k) {
#         int n = nums.length;
#         k %= n;
#         for (int i = 0; i < k; i++) {
#             int temp = nums[n - 1];
#             for (int j = n - 1; j > 0; j--) {
#                 nums[j] = nums[j - 1];
#             }
#             nums[0] = temp;
#         }
#     }

#     /**
#      * 翻转
#      * 时间复杂度：O(n)
#      * 空间复杂度：O(1)
#      */
#     public void rotate_2(int[] nums, int k) {
#         int n = nums.length;
#         k %= n;
#         reverse(nums, 0, n - 1);
#         reverse(nums, 0, k - 1);
#         reverse(nums, k, n - 1);
#     }


#     private void reverse(int[] nums, int start, int end) {
#         while (start < end) {
#             int temp = nums[start];
#             nums[start++] = nums[end];
#             nums[end--] = temp;
#         }
#     }

#     /**
#      * 循环交换
#      * 时间复杂度：O(n)
#      * 空间复杂度：O(1)
#      */
#     public void rotate_3(int[] nums, int k) {
#         int n = nums.length;
#         k %= n;
#         // 第一次交换完毕后，前 k 位数字位置正确，后 n-k 位数字中最后 k 位数字顺序错误，继续交换
#         for (int start = 0; start < nums.length && k != 0; n -= k, start += k, k %= n) {
#             for (int i = 0; i < k; i++) {
#                 swap(nums, start + i, nums.length - k + i);
#             }
#         }
#     }

#     /**
#      * 递归交换
#      * 时间复杂度：O(n)
#      * 空间复杂度：O(n/k)
#      */
#     public void rotate(int[] nums, int k) {
#         // 原理同上
#         recursiveSwap(nums, k, 0, nums.length);
#     }

#     private void recursiveSwap(int[] nums, int k, int start, int length) {
#         k %= length;
#         if (k != 0) {
#             for (int i = 0; i < k; i++) {
#                 swap(nums, start + i, nums.length - k + i);
#             }
#             recursiveSwap(nums, k, start + k, length - k);
#         }
#     }

#     private void swap(int[] nums, int i, int j) {
#         int temp = nums[i];
#         nums[i] = nums[j];
#         nums[j] = temp;
#     }
# }