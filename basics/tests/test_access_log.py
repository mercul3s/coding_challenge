import access_log_summary
import basics

def test_parse_lines():
	'''Test for returning a URL, Response Code, and Size'''
	log = open('tests/test_log.log')
	u, c, s = access_log_summary.parse_lines(log)
	tools.assert_equals(u['"http://mediacast.realgravity.com/"'], 1)
	tools.assert_equals(c['200'], 59)
	tools.assert_equals(s[0], 593)

def test_reverse_string():
	'''make sure that the function returns a reversed string'''
	result = basics.reverse_string('word')
	tools.assert_equals(result, 'drow')

def test_fibonacci():
	'''make sure to return the correct number in the sequence'''
	result = basics.fibonacci(5)
	tools.assert_equals(result, 3)
