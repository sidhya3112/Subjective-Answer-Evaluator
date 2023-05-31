import openpyxl
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Report.Report import Report
import utils
from tkinter import ttk



class Test(tk.Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Question Paper")
        self.tk_setPalette(background='white')
        main_frame = Frame(new)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        r = 1
        c = 0
        Rq = 0
        Cq = 0
        Qtext = utils.Qtext
        entry_font = ('Microsoft YaHei UI Light', 15, 'bold')
        self.entry_boxes = []  # Create an empty list to store entry boxes
        for i in range(len(Qtext)):
            tk.Label(second_frame, text=Qtext[i],font= entry_font).grid(row=Rq, column=Cq, padx=13, pady=21,sticky=W )
            entry_box = Text(second_frame, height=14, width=180, padx=5, pady=5, wrap=WORD, background='white')
            entry_box.grid(row=r, column=c, padx=13, pady=21, sticky=W)
            self.entry_boxes.append(entry_box)  # Append entry box to the list
            Rq += 2
            r += 2
        tk.Button(second_frame, width=39, pady=7, text='Submit', bg='#57a1f8', fg='white', border=0, command=self.click_ok).grid(row=r, column=0,padx=13, pady=21)
        #tk.Button(second_frame, text='  Submit  ', default='active', command=self.click_ok)
    
    def click_ok(self):
          Qtext = utils.Qtext
          utils.list_user_input = [''] * len(self.entry_boxes) 
          for i, entry_box in enumerate(self.entry_boxes):
                  user_input = entry_box.get("1.0", END)
                  if user_input.strip() == "":
                          messagebox.showinfo("Blank Input Error", "Please enter a Statement")
                  elif len(user_input.split()) < 5:
                          messagebox.showinfo("Too Short Input Error", "Please enter a proper Statement")
                  else:
                    utils.list_user_input[i] = user_input
          print(utils.list_user_input)
          self.newWindow = Report()
          self.destroy()