"""
Given a list of start time and end times of a list of queries, how will you find the maximum
concurrency shown by the system?
"""

def max_concurrency(times):
    """
    :type times: List[int]
    """
    line = []
    
    for time in times:
        line.append((time[0], True))
        line.append((time[1], False))
    
    # [(10, True), (20, False), (15, True), (30, False), (5, True), (10, False)]

    line.sort(key=lambda x: (x[0], -x[1]))
    # [(5, True), (10, True), (10, False), (15, True), (20, False), (30, False)]
    history_max = 0
    count = 0

    for _, is_start in line:
        if is_start:
            count += 1
            history_max = max(history_max, count)
        else:
            count -= 1

    return history_max 


input1 = [(10, 20), (15, 30), (5, 10)] ## [(5, True), (10, True), (10, False), (15, True), (20, False), (30, False)]

print(max_concurrency(input1))    