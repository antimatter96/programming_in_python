# Sorting

# Obvious sort

def obvious_sort(l):
    l2 = []

    while len(l) > 0:
        minimum = min_list(l)
        l.remove(minimum)
        l2.append(minimum)
    # find min
    # remove from l
    # add to new list
    # do this till l has an element
    return l2


def min_list(l):
    minimum = l[0]
    for i in range(0, len(l)):
        if l[i] < minimum:
            minimum = l[i]
    return minimum


print(obvious_sort([1, 2, 3, 10, 9, 8, 7, 6, 5, 4]))
