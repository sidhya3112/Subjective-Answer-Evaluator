def load_words():
	'''
	words_alpha.json contains 370101 valid words used for spelling check of words in the user input.
	nltk also contains a words corpus which can be used for this purpose but the length of that corpus is
	smaller than the json file (236736). Hence json file is used.
	'''
	with open('words_alpha.json') as word_file:
		valid_words = set(word_file.read().split())
		# print(valid_words) 
	return valid_words