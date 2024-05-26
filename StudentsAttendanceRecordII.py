# Problem 552
import functools


class StudentsAttendanceRecordII:

    def __init__(self):
        self.base = 1000000007

    def checkRecord(self, n: int) -> int:
        return (self.recurrence(n, 1) + self.recurrence(n, 0)) % self.base

    @functools.cache
    def recurrence(self, num: int, absent: int):
        if num == 1:
            if absent == 1:
                # A
                return 1
            else:
                # L, P
                return 2
        if num == 2:
            if absent == 1:
                # AL, AP, PA, LA
                return 4
            else:
                # LL, LP, PL,PP
                return 4
        if num == 3:
            if absent == 1:
                # ALL, ALP, APL, APP, LAL,LAP, PAL, PAP, LLA, LPA, PLA, PPA
                return 12
            else:
                # LLP, LPL, LPP, PLL, PLP, PPL, PPP
                return 7

        result = 0
        if absent == 1:
            # recent most is absent
            result = (result + self.recurrence(num - 1, 0)) % self.base

            # recent most is present
            result = (result + self.recurrence(num - 1, 1)) % self.base

            # if recent most is L then the past 2 should not be L
            #   L can follow any non L in n-1
            #   n-2, 0 followed by AL
            #   n-2, 1 followed by PL
            result = (result + self.recurrence(num - 2, 0)) % self.base
            result = (result + self.recurrence(num - 2, 1)) % self.base

            #   If L precedes with the recent i.e. n-1 is L,
            #   this implies for n-2 position is not L
            #   n-3,1 followed by PLL
            #   n-3,0 followed by ALL or PLL, but we consider just ALL because absent = 1 here
            result = (result + self.recurrence(num - 3, 1)) % self.base
            result = (result + self.recurrence(num - 3, 0)) % self.base
        else:
            # recent most is Present
            result = (result + self.recurrence(num - 1, 0)) % self.base

            # recent most is L
            # previous to recent i.e. n-1 is not L
            # n-2 followed by PL .. (no absent considered)
            result = (result + self.recurrence(num - 2, 0)) % self.base

            # suppose (n-1) is L and to be added is L
            # this implies (n-2) is not L i.e p
            # that is (n-3, 0) followed by PLL
            result = (result + self.recurrence(num - 3, 0)) % self.base

        return result % self.base


if __name__ == '__main__':
    s = StudentsAttendanceRecordII()
    print(s.checkRecord(2))
    print(s.checkRecord(1))
    print(s.checkRecord(10101))
