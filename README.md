# Map-Reduce
1. max_value.py will take a CSV data file, and output the maximum value of all the numbers using the map-reduce paradigm.
To run: pipenv run python max_value.py fileName.csv

      i.e. Given the following sample CSV file:
      2,2,3
      4,3
      
      The output will be 4.

2. corresponding_lines.py will take a CSV data file, and output all the corresponding line(s) that each word appears in, in the file 
To run: pipenv run python corresponding_lines.py fileName.csv

      i.e Given the following file:
      goat,chicken,horse
      cat,horse
      dog,cat,sheep
      buffalo,dolphin,cat
      sheep 

      The ouput will be:
      "buffalo" ["buffalo,dolphin,cat"]
      "cat" ["buffalo,dolphin,cat", "cat,horse", "dog,cat,sheep"]
      "chicken" ["goat,chicken,horse"]
      "dog" ["dog,cat,sheep"]
      "dolphin" ["buffalo,dolphin,cat"]
      "goat" ["goat,chicken,horse"]
      "horse" ["cat,horse", "goat,chicken,horse"]
      "sheep" ["dog,cat,sheep", "sheep"] 

3. sequence_counter will take a text file containing words separated by spaces, and output the total number of occurrences of each 4 word sequence.
To run: pipenv run python sequence_counter fileName.txt

      i.e. Given the following text file:
      one two three four seven one two three four
      three four seven one
      seven one two three
      
      The output will be:
      "three four seven one" 2
      "four seven one two" 1
      "one two three four" 2
      "seven one two three" 2
      "two three four seven" 1

      

4. path_length2.py will take a CSV data file,and finds all paths of length two in the corresponding URL links
To run: pipenv run python path_length2.py fileName.csv
      
      i.e. Given the following csv file:
      url1,url2
      url1,url3
      url2,url3
      url4,url5
      url2,url4
      
      All lengths of path 2 will be:
      url2, url4, url5
      url1, url2, url3
      url1, url2, url4

