import openpyxl
from AnswerKey.ans_key import ans_key
import utils


def openmyfile(file_name):
	loc = ("Questions/" + file_name + ".xlsx") 		
	workbook = openpyxl.load_workbook(loc)
	utils.sheet = workbook.worksheets[0]
	utils.Qtext = [utils.sheet['A4'].value, utils.sheet['A11'].value, utils.sheet['A17'].value, utils.sheet['A23'].value, utils.sheet['A29'].value, utils.sheet['A35'].value,utils.sheet['A41'].value,utils.sheet['A47'].value,utils.sheet['A53'].value,utils.sheet['A59'].value]
	print(utils.Qtext[0])
	print(utils.Qtext[1])
	print(utils.Qtext[2])
	ans_key(utils.sheet)



