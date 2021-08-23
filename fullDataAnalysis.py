# Stone Faced Emoji
# 112 Hackathon


# from https://textblob.readthedocs.io/en/dev/
import textblob
# nltk from https://www.nltk.org/
from textblob import TextBlob
# from https://docs.python.org/3/library/pprint.html
import pprint
# from https://github.com/python/cpython/blob/3.8/Lib/ast.py
import ast

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# used to clean data from web-scraper
def decipherData(dataDictionary):
    newDataDictionary={} #the cleaned up dictionary
    for entry in dataDictionary:
        stringList=dataDictionary[entry] #gets list of excerpts from category
        newList=[] #list of cleaned up strings
        for string in stringList:
            inArrows=False 
            #checks if the value in the string is part of the html or actual language
            currString="" #creates cleaned string
            for char in string:
                if char=="<":
                    inArrows=True
                if not inArrows and char!="\n" and char!="\'":
                    currString+=char
                if char==">":
                    inArrows=False
            newList.append(currString)
        newDataDictionary[entry]=newList
    return newDataDictionary

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# from http://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def compileData(fileName, instances):
    dataDict = dict()
    for i in range(instances):
        if i == 0:
            fileName = fileName
        else:
            fileName = f'data{i + 1}' 
        dataDict[i] = readFile(fileName + '.txt')
    # at this point we have a dictionary mapping integers to strings of dictionaries
    data = dict()
    for elem in dataDict:
        temp = ast.literal_eval(dataDict[elem])
        data.update(temp)
    # compiled dictionary of all the data: genres map to list of sentences
    for genre in data:
        fullGenreString = ''
        for sentence in data[genre]:
            fullGenreString += sentence
        data[genre] = fullGenreString
    # returns compiled dictionary of genres mapping to a long string of words
    return data

data = compileData('data', 3)

# Creating set of all genres from data
genres = set()
for key in data:
    genres.add(key)

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# Next functions get a list of words common to each genre
def commonWord(data):
    wordCount = {}
    dictionary = decipherData(data)
    for genre in dictionary:
        wordCount[genre] = wordCount.get(genre,{})
        for string in dictionary[genre]:
            for word in string.split():
                word = word.lower()
                newWord = ''
                for letter in word:
                    if letter.isalpha():
                        newWord += letter
                word = newWord
                if word not in wordCount[genre]:
                    wordCount[genre][word] = 0
                count = wordCount[genre].get(word,0)
                wordCount[genre][word] += 1
    return wordCount

def averageWordLength(data):
    dictionary = decipherData(data)
    wordLengths = {}
    for genre in dictionary:
        wordSum = 0
        wordCount = 0
        for string in dictionary[genre]:
            for word in string.split():
                wordCount +=1
                wordSum += len(word)
        wordLengths[genre] = wordSum / wordCount
    return wordLengths

def predictByCount(string,wordCount):
    possibilities = {}
    for word in string.split():
        for genre in wordCount:
            if genre not in possibilities:
                possibilities[genre] = 0
            curCount = possibilities.get(genre,0)
            if word in wordCount[genre]:
                curCount += 1
                possibilities[genre] = curCount
    maxValue = [[],0]
    for genre in possibilities:
        if possibilities[genre] > maxValue[1]:
            maxValue[0] = genre
            maxValue[1] = possibilities[genre]
        elif possibilities[genre] == maxValue[1]:
            maxValue[0].append(genre)
    return maxValue[0]

def predictWordLength(string,wordLengths):
    possibilities = []
    distances = {}
    wordSum = 0
    count = 0
    for word in string.split():
        count += 1
        wordSum += len(word)
    average = wordSum/count
    for genre in wordLengths:
        distances[genre] = abs(wordLengths[genre] - average)
    return distances

wordCount = commonWord(data)
wordLengths = averageWordLength(data)

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# Create dictionary with genres mapping to average scores
dataAverages = dict()
for elem in genres:
    dataAverages[elem] = []

# Using textblob to analyze 'training data'
for genre in data:
    analyzer = TextBlob(data[genre])
    dataAverages[genre] = (analyzer.polarity, analyzer.subjectivity)
    #'Sentiment Analysis:' analyzer.sentiment_assessments
    #'Noun Phrases:' analyzer.noun_phrases
    #'Tags:' analyzer.tags

# from http://www.cs.cmu.edu/~112/notes/notes-strings.html
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

# puts the dataAverages for all of the genres into a final data file (separate)
writeFile('FinalData.txt', str(dataAverages))
