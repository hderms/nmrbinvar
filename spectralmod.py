import csv
from misc import printl
class spectralListGenerator(object):

	def __init__(self, listoffilenames=None):
		fileList = listoffilenames	
		if not listoffilenames:
			fileList = self.prompt_filenames()
	def prompt_filenames(self):
		pass	


class csvOpener(object):
	delimiter = '\t'
	def __init__(self, fileList = None, delimiter = '\t'):
		self.delimiter = '\t'
		self.csvList = []
		if fileList:
			for filenm in fileList:
				self.csvList.append(self.extract_contents(filenm))
	
	def extract_contents(self, fileName):
		file_ref = open(fileName ,'rb')
		csv_contents = [row for row in csv.reader(file_ref, self.delimiter)]
		return csv_contents
			

class controller(object):
	def __init__(self):
		self.controllerDict = {'variance':self.variance, 't-test/anova':self.t_test}

		which_module = raw_input("Which module would you like to use: %s\n" %self.controllerDict.keys())
		self.controllerDict[which_module]()
	
	def variance(self):
		printl("Opening files")		
	def t_test(self):
		pass
if __name__ == "__main__":
	ctrl = controller()
'''

import Tkinter as tk
from tkFileDialog import askopenfilename

root = tk.Tk()

def get_files():
path = askopenfilename(filetypes=[('TXT', '.txt')])
if path:
print path

tk.Button(root, text='1', font=('Wingdings', 12),
command=get_files).pack(padx=5, pady=5)

root.mainloop()

'''	
