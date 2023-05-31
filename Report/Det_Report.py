import openpyxl
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import utils

class Det_Report(tk.Frame):

		#new.geometry("100x50+665+410")
	def __init__(self):
		new =tk.Frame.__init__(self)
		new = Toplevel(self)
		#new.pack()
		new.geometry("700x650+361+100")
		new.title("Evaluation Full Report")
		self.tk_setPalette(background='white')
		main_frame = Frame(new)
		main_frame.pack(fill=BOTH, expand=1)

		my_canvas = Canvas(main_frame)
		my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
		
		my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
		my_scrollbar.pack(side=RIGHT, fill=Y)
		
		my_canvas.configure(yscrollcommand=my_scrollbar.set)
		my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
		
		new_scroll = Frame(my_canvas)
		my_canvas.create_window((0, 0), window=new_scroll, anchor="nw")

		#final_score = (str)(utils.final_score) 
		#keyword = list(utils.keyword)
		similarity_score = 0
		keyword_score = 0
		grammar_score = 0
		spelling_score = 0
		Qtext = utils.Qtext

		similarity_score = sum(utils.all_similarity_scores)/ len(Qtext)
		utils.similarity_score = similarity_score

		grammar_score = sum(utils.all_grammar_scores)/ len(Qtext)
		utils.grammar_score = grammar_score

		spelling_score = sum(utils.all_spelling_scores)/ len(Qtext)
		utils.spell_score = spelling_score

		keyword_score = sum(utils.all_keyword_scores)/ len(Qtext)
		utils.keyword_score = keyword_score



		tk.Message(new_scroll, text=" Your Total Marks are = " + str(utils.total), font='Arial 10 underline',justify='left',aspect=1500).grid(row= 1, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new_scroll, text=" The Similarity factor of the sentence is : {:.2%}".format(utils.similarity_score), font='Arial 10 ',justify='left',aspect=1500).grid(row= 2, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new_scroll, text=" The Grammar accuracy of the sentence is : {:.2%}".format(utils.grammar_score), font='Arial 10 ',justify='left',aspect=1500).grid(row= 3, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new_scroll, text=" The Keyword Accuracy found in the sentence is :  {:.2%} ".format(utils.keyword_score), font='Arial 10',justify='left',aspect=10000).grid(row= 4, column=2, padx=2, pady=2,sticky=W)
		tk.Message(new_scroll, text=" The Spelling accuracy of the sentence is : {:.2%}".format(utils.spell_score), font='Arial 10 ',justify='left',aspect=10000).grid(row= 5, column=2, padx=2, pady=2,sticky=W)
		a= 6
		b= 7
		c=8
		d=9
		e=10

		for i in range(len(Qtext)):
			tk.Message(new_scroll, text="Score of "+str(i+1)+" question: {:}".format(utils.all_final_score[i]*10), font='Arial 10 underline', justify='left', aspect=1500).grid(row= a, column=2, padx = 2, pady=2, sticky=W )
			tk.Message(new_scroll, text="Similarity factor is: {:.2%}".format(utils.all_similarity_scores[i]), font='Arial 10 ', justify='left', aspect=1500).grid(row= b, column=2, padx = 2, pady=2, sticky=W )
			tk.Message(new_scroll, text= "Grammar accuracy is: {:.2%}".format(utils.all_grammar_scores[i]), font='Arial 10', justify='left', aspect=1500).grid(row= c, column=2, padx = 2, pady=2, sticky=W )
			tk.Message(new_scroll, text="Spelling accuracy is: {:.2%}".format(utils.all_spelling_scores[i]), font='Arial 10', justify='left', aspect=1500).grid(row= d, column=2, padx = 2, pady=2, sticky=W )
			tk.Message(new_scroll, text="Keyword Accuracy is: {:.2%}".format(utils.all_keyword_scores[i]), font='Arial 10', justify='left', aspect=1500).grid(row= e, column=2, padx = 2, pady=2, sticky=W )
			a+=5
			b+=5
			c+=5
			d+=5
			e+=5
	
		# key="> "
		# for k in keyword:
		# 	if k == keyword[len(keyword)-1]:
		# 		key= key+ " , " + k + " . "
		# 	elif k==keyword[0]:
		# 		key= key + k
		# 	else:
		# 		key= key+ " , " + k
		# #key=key.reverse()
		
		# tk.Message(new, text=" Some of the Sample Answers are: "+ (str)(utils.sample_ans), font='System 14',justify='left',aspect=200).grid(row= 6, column=2, padx=2, pady=2,sticky=W)
		# tk.Message(new, text=" The Keywords Extracted are :- \n"+key, font='System 12',justify='left',aspect=900).grid(row= 7, column=2, padx=2, pady=2,sticky=W)
		
		new.button2 = tk.Button( new_scroll, text = "Close", width = 15,command = self.close_window )
		#new.button.pack(side='right')
		new.button2.grid(row= e, column=2, padx=100, pady=15,sticky=S)
		
	def close_window(self):
		self.master.destroy()
	
