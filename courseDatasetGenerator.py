import random
import cPickle as pickle

class CourseDatasetGenerator():
	def __init__(self):		
		self.courseFileRaw = 'coursesRaw.dat'	# Raw course file extracted from the course page
		self.ratingFile = 'ratings.dat'	# Automated ratings for all courses. A user only rates courses of one genre
		# self.datasetFile = '/home/abhishek/spark-training-master/machine-learning/python/solution/courses.dat'
		self.courseFileProcessed = 'movies.dat' # Processed list of all courses
		self.genreMap = {'Architecture':'0', 'AI':'1', 'Database':'2', 'Formal Methods':'3', 'Graphics':'4', 'Systems':'5', 'Scientific Computing':'6','Theoretical CS':'7'}

		self.generateCourseFile()
		self.reverseIndex() 
		
	def generateCourseFile(self):
		f1 = open(self.courseFileRaw, 'r')
		f2 = open(self.courseFileProcessed, 'w')

		self.courseList = {}
		self.courseGenreMap = {}
		
		for idx, line in enumerate(f1.readlines()):
			lsplit = line.strip().split('\t')
			courseTitle = lsplit[0]+'-'+lsplit[2]
			genre = lsplit[3] if len(lsplit)>3 else '-1'
			self.courseList[idx] = courseTitle
			self.courseGenreMap[idx] = genre 				
			f2.write(str(idx)+'::'+courseTitle+'::'+genre+'\n')				
		f1.close()
		f2.close()

	def reverseIndex(self):
		self.rIndex = {}
		for courseID in self.courseGenreMap:
			genre = self.courseGenreMap[courseID]
			if genre not in self.rIndex:
				self.rIndex[genre] = []
			self.rIndex[genre].append(courseID)

	def generateRandomRatings(self, users=1000):
		f3 = open(self.ratingFile, 'w') 
		for userID in range(users):
			randomGenre = random.randint(0,len(self.genreMap)-1)
			courseGenre = self.rIndex[str(randomGenre)]
			for course in courseGenre:
				rating = random.randint(1,5)
				f3.write(str(userID+1)+'::'+str(course)+'::'+str(rating)+'::'+str(random.randint(0,9))+'\n')
		f3.close()	

if __name__ == '__main__':
	gen = CourseDatasetGenerator()
	gen.generateRandomRatings()
	pickle.dump(gen, open('courseDataset.pickle', 'wb'))

# 
