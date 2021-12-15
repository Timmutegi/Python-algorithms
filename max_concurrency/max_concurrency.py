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

"""
Find the missing number in the array

A naive solution is to simply search for every integer between 1 and n 
in the input array, stopping the search as soon as there is a missing number. 
But we can do better. Here is a linear, O(n)O(n), solution that uses the 
arithmetic series sum formula.​​ 
"""
def find_missing(input):
    sum_of_elements = sum(input)

    n = len(input) + 1
    actual_sum = (n * (n+1)) / 2

    return actual_sum - sum_of_elements

"""
Given an array of integers and a value, determine if there are any two 
integers in the array whose sum is equal to the given value. 
Return true if the sum exists and return false if it does not.
"""
def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return True

        found_values.add(a)

    return False

"""
Given two sorted linked lists, merge them so that the resulting linked list 
is also sorted. Consider two sorted linked lists and the merged list below 
them as an example.
"""
def merge_sorted(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    mergedHead = None

    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next
    
    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2
    

    return mergedHead
    