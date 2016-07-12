#Write a function that takes a string as input and reverse only the vowels of a string.

#Example 1:
#Given s = "hello", return "holle".

#Example 2:
#Given s = "leetcode", return "leotcede".

#Subscribe to see which companies asked this question


def reverseVowels(s):
	vowels = 'aeiouAEIOU'
	new_string =''
	vowel_value = ''

	for letter in s:
		if letter not in vowels:
			new_string = new_string + letter
		else:
			new_string = new_string + '@'
			vowel_value = vowel_value + letter

	for i in range(len(vowel_value)-1, -1, -1):
		if '@' in new_string:
			new_string = new_string.replace('@', vowel_value[i], 1)
	return new_string


print reverseVowels('hello')
print reverseVowels('leetcode')
print reverseVowels('aA')
print reverseVowels('a a')
print reverseVowels("A mana plana canal -- Panama")