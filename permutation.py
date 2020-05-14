def permutation(string1, string2):
	if len(string1)==len(string2) and set(string1.lower())==set(string2.lower()):
		return True
	return False
permutation("dog", "GoDD")