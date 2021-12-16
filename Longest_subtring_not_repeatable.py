#sliding window problem
def longest_substring(subs):
    length = len(subs)
    l = r = 0
    longest = 0
    window = set()
    while r<length:
        if subs[r] not in window:
            window.add(subs[r])
            r = r + 1
        else:
            window.remove(subs[l])
            l = l + 1
        longest = max(longest,r-l)
    return longest, window


s = input()
print (longest_substring(s))