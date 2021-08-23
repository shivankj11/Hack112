# Stone Faced Emoji
# 112 Hackathon

# from https://textblob.readthedocs.io/en/dev/
import textblob
# nltk from https://www.nltk.org/
from textblob import TextBlob
# from https://docs.python.org/3/library/pprint.html
import pprint

# from http://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

finalData = readFile('FinalData.txt')

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

def getAnalysis(sample):
    sampleAnalysis = TextBlob(sample)
    return (sampleAnalysis.polarity, sampleAnalysis.subjectivity)

