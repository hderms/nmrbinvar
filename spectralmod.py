import csv
from misc import printl
import spectralerrors

import tkMessageBox


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
		print "csvOpener init"
		self.delimiter = '\t'
		self.csvList = []
		self.numcolumnlist = []
		if fileList:
			for filenm in fileList:
				tempcontents = self.extract_contents(filenm)
				if tempcontents:
					self.csvList.append(tempcontents)
				else:
					print "Did not add %s, an error must have occurred, otherwise Nonetype would not have been returned by extract_contents" %filenm
		try:
			assert(len(self.csvList) != 0)
		except:
			raise spectralerrors.EmptyGroupError("Empty group")

	def extract_contents(self, fileName):
		try:
			file_ref = open(fileName ,'rb')
		except:
			printl('Error opening %s' %fileName)
			tkMessageBox.showerror("File Error", "Error opening %s" %fileName)
			return None
		try:
			csvContents = [row for row in csv.reader(file_ref, delimiter = self.delimiter)]
		except:
			tkMessageBox.showerror("File Error", "CSV is not tab-delimited. Error opening  %s" %fileName)
			return None
		self.numcolumnlist.append(max([len(x) for x in csvContents]))
		return csvFile(fileName, csvContents)
class csvFile(object):
	def __init__(self, filename, csvContents):
		self.name = filename
		self.contents = csvContents #csvContents = row of rows
		if csvContents:
			self.generate()
		
	def __str__(self):
		return self.name + '\n' + str(self.contents)
	def generate(self):
		self.contents = filter(lambda x: len(x) > 0, self.contents)
		self.x_values = set([x[0] for x in self.contents])
		
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
