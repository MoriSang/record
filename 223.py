class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area = (by2 - by1) * (bx2 - bx1) + (ay2 - ay1) * (ax2 - ax1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area - overlapArea


if __name__ == '__main__':
    # 主函数
    # ax1 = -2
    # ay1 = -2
    # ax2 = 1
    # ay2 = 1
    # bx1 = 1
    # by1 = 1
    # bx2 = 2
    # by2 = 2

    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = -2,-2, 2, 2, -3, -3, 3, -1

    # ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = -2, -2, 2, 2, -2, -2, 2, 2

    result = Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    print(result)
