# Compare two strings A and B, determine whether A contains all of the characters in B.
# We can think that the B list is empty which show A including B

def compareStrings(A, B):
    # write your code here
    BList = list(B)
    for letter in A:
    	if letter in BList:
		BList.remove(letter)
    if BList == []:
    	return True
    return False

print compareStrings('ADFQERADBOAFHUHFDAHADFADFHADFHADFAODIYFAS','DFJEAFFEFYF')
