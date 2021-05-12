""" This program will take a text file containing words separated by spaces, 
and output the total number of occurrences of each 4 word sequence.
To run:
    pipenv run python part3.py fileName.txt
"""

from mrjob.job import MRJob

class sequenceCounter(MRJob):

    def mapper(self, line, document):
        """ Extracts each 4 word sequence as a list, individually"""
        finalList = []
        firstList = document.split(" ")
        for i in range(len(firstList)-3):
            finalList.append(firstList[i:i+4])
            yield finalList.pop(), 1

    def reducer(self, key, occurrences):
        """ Returns the total occurrences of each 4 word sequence string"""
        key = " ".join(key)
        yield key, sum(occurrences)

sequenceCounter.run()
