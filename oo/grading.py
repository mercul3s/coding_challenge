'''
Check for valid input when the object is created. Make sure the type is a string,
and that it contains at most two characters. Lookup the value in the dictionary, and
create a number value based on the input.

Overriding __cmp__ will let us test the numeric value of each object, 
and determine which is greater; sorting can then be done using that comparison.
'''
class Grade(object):

	def __init__(self, grade_letter):
		grades = {'A': 94, 'B': 84, 'C': 74, 'D': 64, 'F': 54, '-': -4, '+': 4}

		if len(grade_letter) == 1 and grade_letter.upper() in grades:
			self.grade_letter = grade_letter.upper()
			self.grade_value = grades[grade_letter.upper()]
		elif len(grade_letter) == 2 and grade_letter[0].upper() in grades:
			self.grade_letter = grade_letter[0].upper()
			self.grade_value = grades[grade_letter[0].upper()] + grades[grade_letter[1]]

	def __cmp__(self, other):
		return self.grade_value.__cmp__(other.grade_value)
	# def __cmp__(self, other):
		

l = sorted([Grade('B+'), Grade('a'), Grade('F'), Grade('c-'), Grade('D')])

for item in l:
	print item.grade_letter, item.grade_value

print Grade('A') > Grade('c-')

'''
End result:

$ python grading.py
F 54
D 64
C 70
B 88
A 94
True
'''