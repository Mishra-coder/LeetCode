class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        for word in words:
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            remainder = total_weight % 26
            mapped_char = chr(ord('z') - remainder)
            result.append(mapped_char)
        return "".join(result)
        