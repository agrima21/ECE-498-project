#!/usr/bin/env python

import sys
from os import remove, removedirs
from os.path import dirname, join, isfile
from time import time
import cPickle as pickle
from courseDatasetGenerator import CourseDatasetGenerator
import numpy
import operator

gen = pickle.load(open('courseDataset.pickle','rb'))
print "Make a selection:\nGenres:"
for key in sorted(gen.genreMap.items(), key=operator.itemgetter(1)):
	print str(key[1]) + ': ' + str(key[0])
genre = raw_input()

parentDir = dirname(dirname(__file__))
ratingsFile = join(parentDir, "personalRatings.txt")

if isfile(ratingsFile):
    r = raw_input("Looks like you've already rated the movies. Overwrite ratings (y/N)? ")
    if r and r[0].lower() == "y":
        remove(ratingsFile)
    else:
        sys.exit()

#prompt = "Please rate the following movie (1-5 (best), or 0 if not seen): "
prompt = "Please rate the following course (1-5 (best), or 0 if not seen): "
print prompt

now = int(time())
n = 0

f = open(ratingsFile, 'w')
randPerm = numpy.random.permutation(len(gen.rIndex[genre]))
for idx,courseID in enumerate(gen.rIndex[genre]):
    #ls = line.strip().split(",")    
    if idx in randPerm[0:3]:
	    valid = False
	    while not valid:
		rStr = raw_input(str(gen.courseList[courseID]) + ": ")
	#        rStr = raw_input(ls[1] + ": ")
		r = int(rStr) if rStr.isdigit() else -1
		if r < 0 or r > 5:
		    print prompt
		else:
		    valid = True
		    if r > 0:
		        f.write("0::%s::%d::%d\n" % (str(courseID), r, now))
		        n += 1
f.close()

if n == 0:
    print "No rating provided!"
