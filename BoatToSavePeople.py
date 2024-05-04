# Problem 881

class BoatToSavePeople:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people) - 1

        result = 0
        while start <= end and people[end] == limit:
            result += 1
            end -= 1

        while start <= end:
            if people[end] + people[start] <= limit:
                result += 1
                end -= 1
                start += 1
            else:
                result += 1
                end -= 1
        return result
