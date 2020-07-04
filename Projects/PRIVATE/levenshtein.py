def similarity(s1='', s2='', flag_print=False):
    """Levenshtein's distance"""
    def dist(l1, l2):
        if l1 == 0 or l2 == 0:
            # If one of the lines is empty
            return max(l1, l2)
        elif s1[l1-1] == s2[l2-1]:
            # If the last symbols are the same
            return dist(l1-1, l2-1)
        else:
            # If the symbols are different
            return 1 + min(dist(l1, l2-1),  # Deleting symbol
                           dist(l1-1, l2),  # Pasting symbol
                           dist(l1-1, l2-1))  # Replacing symbol

    if flag_print:
        print(f'Distance between "{s1}" & "{s2}" = {dist(len(s1), len(s2))}')
    return dist(len(s1), len(s2))


str1 = 'Hello'
str2 = 'Hi'
print(similarity(str1, str2, True))
