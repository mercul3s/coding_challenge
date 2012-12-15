import grading
from nose import tools
from mock import patch

def test_grade_class_char():
	'''make sure that the grade object is created returns the letter grade'''
	result = grading.Grade('A')
	tools.assert_equals(result.grade_letter, 'A')

'''
This test doesn't work - having trouble asserting the TypeError. 
Probably solution is validating input before the object is created.
'''
def test_grade_class_non_char():
	'''make sure that the grade object is not created and returns an error'''
	result = grading.Grade(4)
	tools.assert_raises(TypeError)
