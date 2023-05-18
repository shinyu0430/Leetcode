def lcp(strs):
    if len(strs) == 0 :
        return ""
    
    strs.sort()

    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix = strs[0][:i]
        else:
            break
    return prefix
print(lcp(["flower","flow"]))

