class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        def findindex(nums, target):
            n = len(nums)
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return n
            low, high = 0, n-1
            while low <= high:
                mid = (high - low) // 2 + low
                if nums[mid] < target < nums[mid+1]:
                    return mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        try:
            index = nums.index(target)
        except:
            index = findindex(nums, target)
        finally:
            return index

if __name__ == '__main__':
    # 主函数

    # m = [2, 6, 0, 0]
    m = [5]
    target = 5
    result = Solution().searchInsert(m, target)
    print(result)
