# decipher-caesar-cipher

This is a Python program which, given input of a message ciphered with a Caesar cipher, can predict the message most likely encrypted. It utilizes data indicating the frequency of each English letter, and uses that to determine the most likely shift in characters. It is also able to eliminate possible solutions by detecting the presence of a vowel; if there is no vowel present in a word, the possibility is eliminated. This makes this program able to narrow down possibilities quite rapidly with multiple words in a sentence. 

I created this while at a summer camp, where we were learning about Caesar ciphers and implementing it in Python; I was curious how a computer could algorithmically decipher an encrypted message without knowing the shift in letters, and after some research, I created this program. 
