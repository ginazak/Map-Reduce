""" This program will take a CSV data file,  
and output all paths of length 2 for corresponding URL links as strings
To run:
    pipenv run python part4.py fileName.csv
"""

from mrjob.job import MRJob
import csv

class linkFinder(MRJob):

    def mapper(self,key,document):
        """ Extracts each URL and it's corresponding line"""
        eachLine =  document.strip().split(",")
        for url in eachLine:
            yield url, eachLine

    def reducer(self,key,document):
        """ Returns the 2 length path of each URL as a string"""
        for i in document:
            for j in document:
                if i[1] == j[0]:
                    triplet= i[0], j[0], j[1]
                    path = ",".join(triplet)
                    yield "_", path

                if j[1] == i[0]:
                    triplet = j[0],i[0],i[1]
                    path = ",".join(triplet)
                    yield "_", path
    
linkFinder.run()
