# Meeting Rooms II

**LeetCode Problem:** 253
**Language:** Python


## Problem

Given an array of meeting time intervals, find the minimum number of conference rooms required so that all meetings can take place without overlapping.

For example:

```text
Input:
[[0,30], [5,10], [15,20]]

Output:
2
```

Two rooms are required because the first meeting overlaps with the other meetings.

## Approach

The starting times and ending times of all meetings are stored separately.

Both lists are sorted.

Then, each meeting start time is compared with the earliest meeting end time.

* If a meeting starts before the earliest meeting ends, a new room is required.
* Otherwise, an existing room becomes available and can be reused.

The maximum number of rooms needed at the same time is the answer.

## Example

For:

```text
[[0,30], [5,10], [15,20]]
```

The meetings overlap as follows:

```text
0 ---- 30
   5 -- 10
        15 -- 20
```

At most two meetings are happening at the same time, so:

```text
Output: 2
```

## Complexity

* Time: O(n log n)
* Space: O(n)

## Key Learning

This problem helped me practice:

* Sorting
* Interval problems
* Two-pointer technique
* Managing overlapping events
* Reusing available resources

## Conclusion

By separating and sorting the starting and ending times, we can efficiently determine how many meeting

## Author

T.nandhini rooms are required at the same time.

**Author:** T. Nandhini
