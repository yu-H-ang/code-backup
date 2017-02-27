class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # 轮转i,j,k才得到正确答案
        
        num = [[strs[i].count('0'), strs[i].count('1')] for i in range(len(strs))]
        knapsack = [[0 for j in range(n+1)] for i in range(m+1)]
        for [zeros, ones] in num:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= zeros and j >= ones:
                        knapsack[i][j] = max(knapsack[i][j], 1 + knapsack[i-zeros][j-ones])
        return knapsack[m][n]

