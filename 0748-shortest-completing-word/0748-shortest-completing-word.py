class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        from collections import Counter
        lp_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        result = None

        for word in words:
            w_count = Counter(word)
            
            if all(w_count[c] >= lp_count[c] for c in lp_count):

                if result is None or len(word) < len(result):
                    result = word
        
        return result