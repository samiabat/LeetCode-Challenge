class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heigh = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heigh[i]!=heights[i]:
                count += 1
        return count