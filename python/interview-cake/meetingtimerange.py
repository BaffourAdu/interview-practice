# Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] =>   [(0, 1), (3, 8), (9, 12)]
def merge_ranges(time_range):
    time_range = sorted(time_range)
    current_time_index = 0
    next_time_index = 1
    no_of_meeting_times = len(time_range) 

    while next_time_index < no_of_meeting_times:
        if (time_range[next_time_index][0] <= time_range[current_time_index][1]) and (time_range[current_time_index][1] >= time_range[next_time_index][1]):
            time_range[current_time_index] = (time_range[current_time_index][0], time_range[current_time_index][1])
            time_range.pop(next_time_index)
            no_of_meeting_times = no_of_meeting_times - 1
        elif (time_range[next_time_index][0] <= time_range[current_time_index][1]):
            time_range[current_time_index] = (time_range[current_time_index][0], time_range[next_time_index][1])
            time_range.pop(next_time_index)
            no_of_meeting_times = no_of_meeting_times - 1
        else:
            current_time_index = current_time_index + 1    
            next_time_index = next_time_index + 1   
        
    return time_range

test_case_1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]  # Output => [(0, 1), (3, 8), (9, 12)]
test_case_2 = [(1, 2), (2, 3)] # Output => [(1, 3)]
test_case_3 = [(1, 5), (2, 3)] # Output => [(1, 5)]
test_case_4 = [(1, 10), (2, 6), (3, 5), (7, 9)] # Output => [(1, 10)]

merged_times = merge_ranges(test_case_4)
print(merged_times)