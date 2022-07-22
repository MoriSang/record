class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1



if __name__ == '__main__':
    # 主函数

    nums = [4]
    target = 4
    result = Solution().search(nums, target)
    print(result)
