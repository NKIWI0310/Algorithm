class Solution(object):
    def sortPeople(self, names, heights):
        people = zip(names, heights)

        sPeople = sorted(people, key=lambda x:x[1], reverse=True)
        sNames = [name for name, height in sPeople]
        return sNames
        