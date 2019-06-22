import pandas as pd
import re
import numpy



def preprocessLine(inputLine):
	dict = {
		r"&lt;p&gt;" : "<p>",
		""" &lt;/p&gt;&#xA;" /> """: "</p>",
		r"""&#xA;""": " ",
		r"&#xD;" : " ",
		"&amp;" : "&",
		"&quot;": """ " """,
		"&apos;": "'",
		"&gt;" : ">",
		"&lt;" : "<",
		}
	htmldict = {
		"<p>": "",
		"</p>": "",
		"<blockquote>": " ",
		"</blockquote>": " ",
		"<li" : "",
		"</li>": "",
		"<ul": "",
		"</ul>": "",
		"<hr": "",
		"</hr>": "",
		"<em": "",
		"</em>": "",
		"</a>": "",
		"<row" : "",
		"/>" : ""
	}
	regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
	result = regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], inputLine)

	htmlregex = re.compile("(%s)" % "|".join(map(re.escape, htmldict.keys())))
	result = htmlregex.sub(lambda mo: htmldict[mo.string[mo.start():mo.end()]], result)

	def striphtml(data):
		p = re.compile(r'<a href= .*?>')
		return p.sub('', data)

	result = striphtml(result)

	return result



	#preprocess the data in each line
	#write your code here




def splitFile(inputFile, outputFile_question, outputFile_answer):

	for a in inputFile:
		result = preprocessLine(a)
		answer = re.compile(""" PostTypeId="2" """)
		question = re.compile(""" PostTypeId="1" """)

		cleaned_file = open("cleaned_file.txt", 'a')
		cleaned_file.writelines(result)
		cleaned_file.close()

		if answer.search(result):
			answer_file = open(outputFile_answer, 'a')
			answer_file.writelines(result)
			answer_file.close()
		if question.search(result):
			question_file = open(outputFile_question, 'a')
			question_file.writelines(result)
			question_file.close()
	#preprocess the original file, and split them into two files.
	#please call preprocessLine() function within this function
	#write you code here



if __name__ == "__main__":

	f_data = []
	zinput = str("<row")
	with open('data.xml', 'r') as f:
		for line in f:
			if zinput in line:
				f_data.append(line)

	f_question = "question.txt"
	f_answer = "answer.txt"




	splitFile(f_data, f_question, f_answer)

