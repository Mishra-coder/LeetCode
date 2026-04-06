class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        pos = {}
        for i in range(len(list1)):
            pos[list1[i]] = i

        ans = []
        min_sum = float('inf')

        for j in range(len(list2)):
            if list2[j] in pos:
                total = j + pos[list2[j]]
                if total < min_sum:
                    min_sum = total
                    ans = [list2[j]]
                elif total == min_sum:
                    ans.append(list2[j])

        return ans
        