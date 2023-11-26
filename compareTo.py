
def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return -ord(s2[0])
    if not s2:
        return ord(s1[0])
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])
