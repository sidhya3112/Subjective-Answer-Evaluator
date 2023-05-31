# Spell Check 
from Report.get_valid_words import load_words
from nltk.tokenize import word_tokenize, sent_tokenize
import utils
import string


def get_spelling_score(list_user_input):
	g = 0
	english_words = load_words() 
	# Create a translation table with punctuation marks mapped to None
	translator = str.maketrans('', '', string.punctuation)

	for i in range(len(list_user_input)):
		g=0
		temp = list_user_input[i]
		temp = temp.strip()
		
	# strip() is used to remove leading and trailing whitespaces
	# print(user_input)
		# Remove punctuation from the text using the translation table
		user_input_without_punctuation = temp.translate(translator)

	# check for valid words in the user_input	
		user_input_words = word_tokenize(user_input_without_punctuation.lower())
		for t in user_input_words:
			# print(t)
			if t in english_words:
				g = g + 1 #g is the count of valid english words in the user input
		temp = g / len(user_input_words)
		utils.all_spelling_scores.append(temp)

	
	
