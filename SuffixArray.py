# T = banana
# P = nan

# Suffix Array
#0 a
#1 ana
#2 anana
#3 banana
#4 na
#5 nana

# find(T, P)

def create_suffix(text):
    result = []

    for i in range(len(text)):
        result.append(text[i:])

    return sorted(result)

# [0, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7]
# [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] binary search + linear O(N/2), linear search O(1)
# [0, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7] O(lgN) + O(N/2), O(N)
def binary_search(pattern, suffixes, lowest=True):
    end = len(suffixes) - 1
    start = 0
    result = -1

    while end >= start:
        mid = (end + start)//2
        if suffixes[mid].startswith(pattern):
            result = mid
            if lowest:
                end = mid - 1
            else:
                start = mid + 1
        elif suffixes[mid] > pattern:
            end = mid - 1
        else:
            start = mid + 1
    return result;

# an -> 'ana', 'anana'
def find(pattern, suffixes):
    low = binary_search(pattern, suffixes, True)
    high = binary_search(pattern, suffixes, False)
    result = suffixes[low:high + 1]
    return result


res = ['a', 'ana', 'anana', 'banana', 'na', 'nana']
assert [] == create_suffix('')
assert res == create_suffix('banana')

assert 5 == binary_search('nan', res)
assert 5 == binary_search('nan', res, False)

assert 1 == binary_search('an', res)
assert 2 == binary_search('an', res, False)

assert -1 == binary_search('ax', res)

assert ['ana', 'anana'] == find('an', res)
