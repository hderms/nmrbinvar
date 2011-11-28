import Tkinter as tk
import os
from tkFileDialog import askopenfilename
import platform

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

print "Platform is %s" % platform.system()
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
		self.top.destroy()
	def report_group(self):
		if self.chosenvalue:
			return self.chosenvalue

class groupContainer(object):
	def __init__(self, window, number_of_groups = None):
		self.window = window
		self.number_of_groupsi = number_of_groups
		self.group_hash = {}
	def choose(self, window, path):
		temp_group = group(path)
		groupChooser = chooseGroup(self, window, temp_group)
	def report(self):
		print self.group_hash.keys()
	def add(self, group):
		self.group_hash[group.groupid] = group	
class group(object):
	def __init__(self, paths, groupid = None):
		self.groupid = groupid
		self.paths = paths
	
		
		

def get_files(window, num_groups, group_container):
	path = askopenfilename(multiple=True)
	print _Windows
	path = path if not _Windows else [x for x in window.tk.splitlist(str(path))]
	print type(path)
	group_container.choose(window, path)

		
def makeentry(parent, caption, width=None, **options):
	tk.Label(parent, text=caption).pack(side=tk.LEFT)
	entry = tk.Entry(parent, **options)
	if width:
		entry.config(width=width)
	entry.pack(side=tk.LEFT)
	return entry

tk.Button(root, text='Select Files', command=lambda : get_files(root, int(groupNumberEntry.get()), spectralGroups)).pack(padx=5, pady=5)
groupNumberEntry= makeentry(root, "Num Groups")
groupNumberEntry.insert(0, "1")
spectralGroups = groupContainer(int(groupNumberEntry.get()))

class listBoxFactory(object):
	def __init__(self, rootwindow, groupContainer):
		listbox = tk.Listbox(tk.Toplevel(root), selectmode=tk.EXTENDED)
		listbox.pack()
		listbox.config(width = 70)
		self.listOfTerms = []
		for x in groupContainer.group_hash.keys():
			for indy, path in enumerate(groupContainer.group_hash[x].paths):
				listbox.insert(tk.END, os.path.split(path)[1] + '\t Group:' + x)
				self.listOfTerms.append(path)
		self.listBox = listbox
	def __call__(self, *largs, **kargs):
		self.listBox(*largs, **kargs)
		print self.listOfTerms
		
#tk.Button(root, text="T-test/Anova", command=)
tk.Button(root,text="Display groups", command= lambda : listBoxFactory(root, spectralGroups)).pack(padx=5,pady=5)

root.mainloop()

