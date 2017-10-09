file = input('Enter file: ')  #Decided to select a file, otherwise just fhand = open(wordtext.txt, 'r')
try:
	fhand = open(file,'r')
except:
	print('File cannot be opened: ',file)
	exit()
words = dict()
for line in fhand:
	line = line.split()
	for word in line:
		if word not in words:
			words[word] = 1
##print(words)
while True:
	chk= input('Enter word: ')
	if chk == 'I am finished':
		print(chk in words, '- Exiting programme.')
		exit()	
	elif chk in words:
		print(chk, 'is in the dictionary')
	elif chk not in words:
		print(chk, 'is NOT in dictionary')


## Exercise 1: [wordlist2]
## Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
## t doesn't matter what the values are.
## Then you can use the in operator as a fast way to check whether a string is in the dictionary.