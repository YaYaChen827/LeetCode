def longestWords(dictionary):
    # write your code here
    maxLen = 0
    maxList = []
    for word in dictionary:
    	if len(word) >= maxLen:
    		maxLen = len(word)
    for word in dictionary:
    	if len(word) == maxLen:
    		maxList.append(word)
    return maxList

print longestWords(["dog","google","facebook","internationalization","blabla"])