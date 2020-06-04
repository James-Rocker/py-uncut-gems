import PyPDF2
import matplotlib.pyplot as plt
from collections import Counter

file = open('GEMS_FINAL_SCRIPT.pdf', 'rb')
fileReader = PyPDF2.PdfFileReader(file)
words = ''

for page in range(fileReader.numPages):
    pageObj = fileReader.getPage(page)
    words += pageObj.extractText()

Counter = Counter(words.lower().split())
most_occur = Counter.most_common(20)

plt.bar(*zip(*most_occur))
plt.show()
