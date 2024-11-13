def longest_common_prefix(strs):
    # if the list is empty, return a -1
    if not strs:
        return "-1"
    
    # sort the list of strings
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first), len(last))

    i = 0
    # find the common prefix between the first
    # and the last strings

    while i < min_length and first[i] == last[i]:
        i += 1

    # check if thers no common prefix
    if i == 0:
        return "-1"
    
    # return the common prefix
    return first[:i]

strs = ["geeksforgeeks", "geeks", "geek", "geezer"]
print("The longest common prefix is: ", 
      longest_common_prefix(strs))