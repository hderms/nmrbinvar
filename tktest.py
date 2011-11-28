import Tkinter as tk
import os
from tkFileDialog import askopenfilename
import platform
import spectralmod
import tkMessageBox
import spectralerrors
'''EXPERIMENTAL BRANCH'''

root = tk.Tk()

#platform specific logic because tk askopenfile contains some bugs with python + windows
global _Plotting
global _Windows
if platform.system() == 'Windows':
	_Windows = True
else:
	_Windows = False
try:
	import matplotlib
except:
	_Plotting = True


class chooseGroup(object):
	
	def __init__(self,container, parent, group):
		top=self.top=tk.Toplevel(parent)
		tk.Label(top,text="Group").pack()
		self.e = tk.Entry(top)
		self.e.pack(padx=5)
		b = tk.Button(top, text="Ok",command=self.ok)
		b.pack(pady=5)
		self.chosenvalue = None
		self.container = container
		self.group = group
	def ok(self):
		self.chosenvalue = self.e.get()
		self.group.groupid = self.chosenvalue
		self.container.add(self.group)	
		self.container.check_compatibility()
		self.top.destroy()
	def report_group(self):
		if self.chosenvalue:
			return self.chosenvalue

class graphGenerator(object):
	def __init__(*args):
		pass
	def variance_graph(self, groupContainer):
		pass

class groupContainer(object):
	def __init__(self, window, number_of_groups = None):
		self.window = window
		self.number_of_groups = number_of_groups
		self.group_hash = {}

	def choose(self, window, paths):
		temp_group = group(paths)
		
		if paths:
			if window:
				groupChooser = chooseGroup(self, window, temp_group)

			

		else: 
			tkMessageBox.showerror('Group error', 'No acceptable files chosen')
	def report(self):
		print self.group_hash.keys()
	def add(self, group):
		if group.groupid:
			self.group_hash[group.groupid] = group
			group.read_spectra()

			
		else:
			raise KeyError
	def allgroups(self):
		pass
	def group_xvalue_intersection(self, list_of_groups ):
		x_values_list= []
		for group in list_of_groups:
			for elem in self.group_hash[group].spectralList:
				x_values_list.append(elem.x_values)
		return reduce(lambda x, y: x & y, x_values_list)
			
		
	def check_compatibility(self, list_of_groups = None):
		
		if not list_of_groups:
			list_of_groups = self.group_hash.keys()
		print self.group_xvalue_intersection(list_of_groups)
			
class group(object):
	def __init__(self, paths, groupid = None):

		self.groupid = groupid
		self.paths = paths

	def read_spectra(self):
		if self.paths:
			try:
				self.csvopen = spectralmod.csvOpener(fileList = self.paths)
			except spectralerrors.EmptyGroupError:
				print "empty group error"
			self.spectralList = self.csvopen.csvList
			self.numcolumns = max(self.csvopen.numcolumnlist)
			print "num columns is %s" % self.numcolumns
		else:
			raise Exception('No paths')
	def __str__(self):
		return '\n\n'.join([str(x) for x in self.spectralList])
		
		

def groupContainerGenerator(window, num_groups, group_container):
	path = askopenfilename(multiple=True)
	print _Windows
	path = path if not _Windows else [x for x in window.tk.splitlist(str(path))]
	print type(path)
	group_container.choose(window, path)

		
def makeEntryBox(parent, caption, width=None, **options):
	tk.Label(parent, text=caption).pack(side=tk.LEFT)
	entry = tk.Entry(parent, **options)
	if width:
		entry.config(width=width)
	entry.pack(side=tk.LEFT)
	return entry
class listBoxFactory(object):
	def __init__(self, rootwindow, groupContainer):
		listbox = tk.Listbox(tk.Toplevel(root), selectmode=tk.EXTENDED)
		listbox.pack()
		listbox.config(width = 70)
		self.listOfTerms = []
		for x in groupContainer.group_hash.keys():
			for enumindex, path in enumerate(groupContainer.group_hash[x].paths):
				listbox.insert(tk.END, str(os.path.split(path)[1]) + '\t Group:' + x)
				self.listOfTerms.append(path)
		self.listBox = listbox
	def __call__(self, *largs, **kargs):
		self.listBox(*largs, **kargs)
		print self.listOfTerms
		
if __name__== "__main__":
	print "Platform is %s" % platform.system()
	tk.Button(root, text='Select Files', command=lambda : groupContainerGenerator(root, int(groupNumberEntry.get()), spectralGroups)).pack(padx=5, pady=5)
	groupNumberEntry= makeEntryBox(root, "Num Groups")
	groupNumberEntry.insert(0, "1")
	spectralGroups = groupContainer(int(groupNumberEntry.get()))
	
	
	#tk.Button(root, text="T-test/Anova", command=)
	tk.Button(root,text="Display groups", command= lambda : listBoxFactory(root, spectralGroups)).pack(padx=5,pady=5)
	tk.Button(root,text="Spectral Variance", command= lambda : spectralGroups.dis).pack(padx=5,pady=5)
	
	root.mainloop()
	
