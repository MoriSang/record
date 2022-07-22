class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k %= len(nums)
        a = nums[:-k]
        del nums[:-k]
        for i in a:
            nums.append(i)

if __name__ == '__main__':

    m = [1,2]
    k = 3

    Solution().rotate(m, k)
    print(m)
