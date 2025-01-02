class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        mymap = {}
        res = []

        # Store reversed words in the map
        for i in range(n):
            word = words[i]
            key = word[::-1]
            mymap[key] = i

        for i in range(n):
            word = words[i]
            length = len(word)
            for j in range(length + 1):  # Include the empty suffix/prefix
                left = word[:j]  # Prefix
                right = word[j:]  # Suffix

                # Case 1: Left is a palindrome, and reversed right exists in the map
                if self.__ispalindrome(left) and right in mymap and mymap[right] != i:
                    res.append([mymap[right], i])

                # Case 2: Right is a palindrome, and reversed left exists in the map
                if j != length and self.__ispalindrome(right) and left in mymap and mymap[left] != i:
                    res.append([i, mymap[left]])

        return res

    def __ispalindrome(self, word: str) -> bool:
        l = 0
        r = len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
