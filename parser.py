import preprocessData
import re

dict_type = {}
dict_date = {}
dict_vocab = {}
dict_quarter = {}

class Parser:
	"""docstring for ClassName"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.cleanBody = self.getCleanedBody()
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.VocabularySize = self.getVocabularySize()

	def __str__(self):
		return "ID is equal to:" + self.ID + "\n" + "Post Type is equal to: "+ self.type+ "\n"+"Quarter is equal to:" + self.dateQuarter+"\n"+"Vocabulary size is equal to: " + str(self.VocabularySize) + "\n"



	def getID(self):
		x = self.inputString.strip()
		ID = x[x.find('Id=')+4: x.find(' ')-1]
		return ID
		#write your code here
		

	def getPostType(self):
		x = self.inputString.strip()
		PostTypeId = x[x.find('PostTypeId') + 12:x.find('C') - 2]
		dict_type[self.ID]= PostTypeId
		return PostTypeId
		#write your code here
		

	def getDateQuarter(self):
		x = self.inputString.strip()
		Date = x[x.find('C') + 14:x.find('B') - 2]
		month = Date[Date.find('-')+1:Date.find('T')-3]
		month = int(month)

		if (month == 1 or month==2 or month==3):
			quarter = 1
			dict_quarter[self.ID] = quarter
			quarter = str(quarter)
			return quarter

		elif (month == 4 or month==5 or month==6):
			quarter =2
			dict_quarter[self.ID] = quarter
			quarter = str(quarter)
			return quarter
		elif (month == 7 or month==8 or month==9):
			quarter =3
			dict_quarter[self.ID] = quarter
			quarter = str(quarter)
			return quarter
		else:
			quarter = 4
			dict_quarter[self.ID] = quarter
			quarter = str(quarter)
			return quarter

	#write your code here
		

	def getCleanedBody(self):
		self.inputString = preprocessData.preprocessLine(self.inputString)
		#write your code here
		

	def getVocabularySize(self):
		n = 0
		unique = []
		x = self.inputString.strip()
		Body = x[x.find('B') + 6:len(x) - 1]
		Body =  re.sub(r'[^\w\s]','',Body)
		words = Body.split()
		for word in words:
			if word not in unique:
				unique.append(word)
		unique_words = set(unique)
		for words in unique_words:
			n+=1
		dict_vocab[self.ID] = n
		return n



#write your code here
if __name__ == "__main__":


	f_data = []
	zinput = str("<row")
	with open('data.xml', 'r') as f:
		for line in f:
			if zinput in line:
				f_data.append(line)

	for a in f_data:
		Parser(a)
		print(Parser(a))





