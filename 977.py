
class Solution:
    def sortedSquares(self, nums):
        for i, num in enumerate(nums):
            nums[i] *= num
        nums.sort()
        return nums


if __name__ == '__main__':

    m = [-4,-1,0,3,10]
    # m = [-7,-3,2,3,11]
    result = Solution().sortedSquares(m)
    print(result)
