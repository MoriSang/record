class Solution:

    def findMinMoves(self, machines) -> int:
        n = len(machines)
        if sum(machines) % n != 0:
            return -1
        avg_clothes = sum(machines)//n
        ans, s = 0, 0
        for i in range(n):
            machines[i] -= avg_clothes
            move_num = sum(machines[:i])
            ans = max(ans, machines[i], abs(move_num))
        return ans

if __name__ == '__main__':
    # 主函数

    # m = [2, 6, 0, 0]
    M = [[1], [0,0,11,5], [0,2,0]]
    for m in M:
        result = Solution().findMinMoves(m)
        print(result)

