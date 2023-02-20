from algo_expert.arrays.medium.merge_overlapping_intervals import merge_overlapping_intervals


class TestMergeOverlappingIntervals:
    def test_case_0(self):
        intervals = [
            [1, 2],
            [3, 5],
            [4, 7],
            [6, 8],
            [9, 10]
        ]

        expected = [
            [1, 2],
            [3, 8],
            [9, 10]
        ]

        assert merge_overlapping_intervals(intervals) == expected
