""" This program will take a CSV data file, 
and determine the corresponding line(s) of each word in the file 
To run:
    pipenv run python part2.py fileName.csv
"""

from mrjob.job import MRJob
import csv

class lineChecker(MRJob):

    def mapper(self, key, document):
        """ Extracts each word and its corresponding line individually"""
        eachLine = []
        for word in document.split():
            eachLine.append(word)
            eachLine=" ".join(str(i) for i in eachLine)
            for word in document.split(","):
                yield word.strip(), eachLine

    def combiner(self, word, lines):
        """ Returns only unique values for each key"""
        allLines = list(lines)
        yield word, allLines[0] #Removes duplicates

    def reducer(self, word, lines):
        """ Returns all the corresponding lines of each word """
        allLines = list(lines)
        yield word, allLines

lineChecker.run()