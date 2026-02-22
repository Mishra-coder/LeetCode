class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        res = []
        
        for word in words:
            s = set(word.lower())
            if s <= row1 or s <= row2 or s <= row3:
                res.append(word)
        
        return res