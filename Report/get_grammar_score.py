import nltk
from nltk.tokenize import word_tokenize
import language_tool_python
tool = language_tool_python.LanguageToolPublicAPI('en-US')
import utils

# Grammar Check
def get_grammar_score(list_user_input):
	
    for res in range(len(list_user_input)):
        user_input_words = word_tokenize(list_user_input[res].lower())
        matches = tool.check(list_user_input[res])
        mistake_score = len(matches) / len(user_input_words)

        utils.all_grammar_scores.append(1-mistake_score)
	
	# Can print the "message", "replacements", "context", "ruleIssueType" and "sentemce" 
	# for the errors found in the text
