class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        rooms = 0
        end_index = 0

        for time in start:
            if time < end[end_index]:
                rooms += 1
            else:
                end_index += 1

        return rooms
