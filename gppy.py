#gppy
#Version 1.1
#lechacal.com

# History
#1.0: First version
#1.1: added reset
#     added addcandlestick

import subprocess, string

class gppy:
	def __init__(self):
		self.pipe = subprocess.Popen(['gnuplot','-p'], stdin=subprocess.PIPE, shell=False)
		self.plotcmd = "plot "
		self.nplot = 0
		self.data = ""	

	def reset(self):
		self.data = ""
		self.plot = "plot "
		self.nplot = 0
	
	def write(self, text):
		self.pipe.stdin.write(text+"\n")

	def template(self, filename, parameters):
	        f = open(filename,'r')
	        template_file = f.read()
	        f.close()
	
	        s = string.Template(template_file)
	        gnucmd = s.safe_substitute(parameters)
		self.pipe.stdin.write(gnucmd)


	def plot_file(self, filename, Data_index=[1], Titles = None, x=None):
		if x==None:
			_x = ""
		else:
			_x = str(x)+":"
		if Titles == None:
			Titles = [""]*len(Data_index)

        	Plots = []
        	for i in range(len(Data_index)):
        	        Plots.append("\"%s\" u %s%s title \"%s\" w lines" \
                                                % (filename,_x,Data_index[i],Titles[i]))
        	#plotcmd = "plot %s"%", ".join(Plots)
        	self.addplot(", ".join(Plots))
		return self.plotcmd
	

	def xy_as_stdin(self,X,Y,execute=False):
		forplot = ""
                for i in range(len(X)):
                        forplot += "%s\t%s\n" % (str(X[i]),str(Y[i]))
                forplot += "e\n"
		if execute:
			self.pipe.stdin.write(forplot)
		return forplot

	def addplot(self,text):
		if self.nplot == 0:
			self.plotcmd += text
		else:
			self.plotcmd += ", " + text
		self.nplot += 1


	def adddata(self, X, Y=None):
		if Y==None:
			for i in range(len(X)):
				self.data += "%s\n" % (str(X[i]))
		else:	
			for i in range(len(X)):
				self.data += "%s\t%s\n" % (str(X[i]),str(Y[i]))
                self.data += "e\n"

	def addcandlestick(self, Co, Cl, Ch, Cc, T=None):
		if T==None:
			for co,cc,ch,cl in zip(Co,Cc,Ch,Cl):
				self.data += "%s\t%s\t%s\t%s\n" % (co,cl,ch,cc)
		else:
			for t,co,cc,ch,cl in zip(T,Co,Cc,Ch,Cl):
				self.data += "%s\t%s\t%s\t%s\t%s\n" % (t,co,cl,ch,cc)
                self.data += "e\n"


	def shoot(self):
		self.write(self.plotcmd)
		self.write(self.data)
