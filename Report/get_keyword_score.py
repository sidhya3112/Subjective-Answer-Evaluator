# Keyword Check
import nltk
from nltk.corpus import stopwords
import spacy
import utils
#nltk.download('stopwords')

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def get_keyword_score(list_user_input, all_keywords):		
	found = []
	for key in range(len(all_keywords)):
		found.clear()
		templist = all_keywords[key]
		for a in templist:
			if a.lower() in list_user_input[key].lower():
				found.append(a)
		
		utils.all_found.append(len(found))
		temp = len(templist)/len(utils.finalList[key])
		result = len(found)/temp
		if result >= 1:
			utils.all_keyword_scores.append(1)
		else:
			utils.all_keyword_scores.append(result)

		
	