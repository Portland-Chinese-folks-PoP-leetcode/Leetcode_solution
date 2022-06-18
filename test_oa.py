def maxEvents(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )
    print(aux)
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    return ans


starts = [1, 3, 3, 5, 7]

durations = [2, 2, 1, 2, 1]

print(maxEvents(starts, durations))
# ziped = zip(starts, durations)
# print(dir(ziped))
# help(zip)
