def merge_overlapping_intervals(intervals: list) -> list:
    sorted_intervals = sorted(intervals)
    result = []
    while len(sorted_intervals) > 0:
        result.append(sorted_intervals.pop(0))
        while len(sorted_intervals) > 0 and result[-1][1] >= sorted_intervals[0][0]:
            result[-1][1] = max([sorted_intervals.pop(0)[1], result[-1][1]])
    return result
