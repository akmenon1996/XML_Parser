import preprocessData
import parser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def visualizeWordDistribution(inputFile, outputImage):
	#write your code here
	a = 0
	b = 0
	c = 0
	m = 0
	e = 0
	q = 0
	g = 0
	h = 0
	i = 0
	j = 0
	k = 0



	f = []
	zinput = str("<row")
	with open(inputFile, 'r') as file:
		for line in file:
			if zinput in line:
				f.append(line)
	for row in f:
		result = preprocessData.preprocessLine(row)
		parser.Parser(result)

	for value in parser.dict_vocab.values():
		if (value>= 0 and value < 10):
			a +=1
		elif (value>=10 and value <20 ):
			b+=1
		elif (value>=20 and value <30 ):
			c+=1
		elif (value>=30 and value <40 ):
			m+=1
		elif (value>=40 and value <50 ):
			e+=1
		elif (value>=50 and value <60 ):
			q+=1
		elif (value>=60 and value <70 ):
			g+=1
		elif (value>=70 and value <80 ):
			h+=1
		elif (value>=80 and value <90 ):
			i+=1
		elif (value>=90 and value <100 ):
			j+=1
		elif (value>=100):
			k+=1


	df = pd.DataFrame({'Labels' : ['0-10', '10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','Others'], 'Values':[a,b,c,m,e,q,g,h,i,j,k]})
	print(df)
	df.plot(kind='bar', x='Labels', y='Values', color='red')
	plt.savefig(outputImage)
	plt.clf()



def visualizePostNumberTrend(inputFile, outputImage):
	q1 = 0
	a1 = 0
	q2 = 0
	a2 = 0
	q3 = 0
	a3 = 0
	q4 = 0
	a4 = 0

	f = []
	zinput = str("<row")
	with open(inputFile, 'r') as file:
		for line in file:
			if zinput in line:
				f.append(line)
	for row in f:
		result = preprocessData.preprocessLine(row)
		parser.Parser(result)

	for (value), (type) in zip(parser.dict_quarter.values(), parser.dict_type.values()):
		if int(value) == 1 and int(type) == 1:
			q1+=1
		if int(value) == 1 and int(type) == 2:
			a1+=1
		if int(value) == 2 and int(type) == 1:
			q2+=1
		if int(value) == 2 and int(type) == 2:
			a2+=1
		if int(value) == 3 and int(type) == 1:
			q3+=1
		if int(value) == 3 and int(type) == 2:
			a3+=1
		if int(value) == 4 and int(type) == 1:
			q4+=1
		if int(value) == 4 and int(type) == 2:
			a4+=1


	df1 = pd.DataFrame(
		{'Quarters': ['1','2','3','4'],
		 'Questions': [q1,q2,q3,q4],
		 'Answers':[a1,a2,a4,a4]})
	print(df1)
	print(df1)

	ax = plt.gca()

	df1.plot(kind='line', x='Quarters', y='Questions', ax=ax)
	df1.plot(kind='line', x='Quarters', y='Answers', color='red', ax=ax)
	plt.savefig(outputImage)
	plt.clf()


if __name__ == "__main__":
	dict_type = {}
	dict_date = {}
	dict_vocab = {}
	dict_quarter = {}

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)



