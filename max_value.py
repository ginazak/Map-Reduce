""" This program will take a CSV data file, 
and output the maximum value of all the numbers
using the map-reduce paradigm.
To run:
    pipenv run python part1.py fileName.csv
"""

from mrjob.job import MRJob
import csv

class maxValue(MRJob):
    
    def mapper(self, key, document):
        """ Extracts each number individually """
        for number in document.split(","):
            yield "_", float(number)

    def reducer(self, _ , document):
        """  Finds the max value of all the extracted numbers """
        yield "_", max(document)

maxValue.run()
