def longest_common_prefix(strs):
    # if the list is empty look for a return of "-1"
    if not strs:
        return "-1"
    
    # sort the list of strings
    strs.sort()

    # get the first and last strings after sorting 
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first), len(last))