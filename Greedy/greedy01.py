def findContentChildren(g, s):
    g.sort()
    s.sort()

    l,r = 0,0
    total = 0

    while r < len(s) and l < len(g):
        if s[r] >= g[l]:
            total+=1
            l+=1
            r+=1
        else:
            r+=1

    return total