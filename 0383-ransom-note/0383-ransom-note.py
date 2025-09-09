class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        strDict = {}
        # track occurrance of chars in mag into the dict 
        for item in magazine:
            if item in strDict.keys():
                strDict[item] += 1
            else:
                strDict[item] = 1
        # check if the chars in ransom match those in the dict - decrement 
        count = 0
        for item in ransomNote:
            if item in strDict:
                strDict[item] -= 1
                # if the value = 0, delete
                if strDict[item] == 0:
                    del strDict[item]
                count += 1
            else:
                return False
                break
        if count == len(ransomNote):
            return True