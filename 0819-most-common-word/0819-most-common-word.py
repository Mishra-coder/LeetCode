class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        banned_set = set(banned)
        freq = {}
        word = ""
        max_count = 0
        result = ""
        
        paragraph = paragraph.lower()
        
        for c in paragraph + " ":
            if c.isalpha():
                word += c
            else:
                if word:
                    if word not in banned_set:
                        freq[word] = freq.get(word, 0) + 1
                        
                        if freq[word] > max_count:
                            max_count = freq[word]
                            result = word
                    word = ""
        
        return result