import access_log_summary
from nose import tools

def test_parse_lines():
	'''Test for returning a URL, Response Code, and Size'''
	log = open('tests/test_log.log')
	u, c, s = access_log_summary.parse_lines(log)
	tools.assert_equals(u['"http://mediacast.realgravity.com/"'], 1)
	tools.assert_equals(c['200'], 59)
	tools.assert_equals(s[0], 593)
