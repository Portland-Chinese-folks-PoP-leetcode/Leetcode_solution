from collections import defaultdict

import math
test_case1 = [5, 5, 3, 6, 5, 3]


def processCeil(process: list):
    # construct cohesion_dictionary
    res = 0
    cohesive_dict = defaultdict(list)
    for i in range(len(process)):
        cohesive_dict[process[i]].append(i)
    # construct new process list
    for i in range(len(process)):
        process[i] = [process[i], process[i]]
    print(cohesive_dict)
    print(process)
    for i in range(len(process)):
        time = process[i][0]
        cohesive_dict[process[i][1]].remove(i)
        for idx in cohesive_dict[process[i][1]]:
            process[idx][0] = math.ceil(process[idx][0]/2)
        res += time
    return res


print(processCeil(test_case1))
