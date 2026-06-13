class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower_chars = set()
        upper_chars = set()
        
        for char in word:
            if char.islower():
                lower_chars.add(char)
            else:
                upper_chars.add(char.lower())
                
        return len(lower_chars.intersection(upper_chars))
        