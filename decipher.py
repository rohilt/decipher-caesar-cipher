user_input = raw_input("Enter an encrypted phrase: ")
print ""
print "Here are the possible messages this phrase encodes: "
print ""
letters_list = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']
frequency_list = [12.02, 9.10, 8.12, 7.68, 7.31, 6.95, 6.28, 6.02, 5.92, 4.32, 3.98, 2.88, 2.71, 2.61, 2.30, 2.11, 2.09, 2.03, 1.82, 1.49, 1.11, 0.69, 0.17, 0.11, 0.10, 0.07]
scores = []
solutions = []
for number in range (0, 26):
	is_vowel = False
	phrase = ""
	score = 0
	for letter in user_input:
		if ord(letter) >= 97 and ord(letter) <= 122:
			if ord(letter) + number > 122:
				nl= chr(ord(letter) - 26 + number)
				phrase += nl
			else:
				nl = chr(ord(letter) + number)
				phrase += nl
			score += frequency_list[letters_list.index(nl)]
		elif ord(letter) >= 65 and ord(letter) <= 90:
			if ord(letter) + number > 122:
				nl= chr(ord(letter) - 26 + number)
				phrase += nl
			else:
				nl = chr(ord(letter) + number)
				phrase += nl
		elif ord(letter) == 32:
			phrase += letter
			nl = " "
			if is_vowel == False:
				break
				break
			is_vowel = False
		else:
			phrase += letter
			nl = letter
		if ord(nl)==97 or ord(nl)==101 or ord(nl)==105 or ord(nl)==111 or ord(nl)==117 or ord(nl)==121:
			is_vowel = True
	if is_vowel:
		solutions.append(phrase)
		scores.append(score)
scores_solutions = zip(scores, solutions)
scores_solutions.sort()
for x in scores_solutions:
	print x
	print ""