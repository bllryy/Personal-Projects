 def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return "-1" 

    first = str[0]
    last = str[-1]
    min_length = min(len(first), len(last))

    i = 0

    while i < min_length and first[i] == last[i]:
        i += 1


str = ["flower","flow","flight"]