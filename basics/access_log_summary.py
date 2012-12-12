import operator
'''
Write a program that parses the access logs found in the *mediacast_access.log.gz* file and produces the following information:

  - A breakdown of request counts by response code.
  - A list of the top 5 URLs hit (with counts).
  - The average and median request size.

The logs in that file follow this format:

    <remote_ip> [<timestamp>] "<request>" <status> <size> <duration> "<referer>" "<user_agent>" "<forwarded_for>"
'''

'''
------
Parse each line of the log file into URLs, size, and status code
Store URLs as a key in a dictionary with the counts as their value
Store requests response codes in a dictionary along with the number of times they occur
Average: add up all the sizes
Median: find the element in the middle of all sizes
------
'''

'''
------
Iterate over lines in file, split lines on spaces, and add keep a tally of urls and status codes in
a dictionary. Add all sizes to a list for averaging (assuming data in integer form is OK).
or just use awk to split out your columnns into another file and parse that:
cat mediacast_access.log | awk '{print $3,$6,$7,$9}' > media_access.txt
However, you'd still need to open the file and read all lines.
Probably checking for urls with regex would be a better way of adding URLs to the dictionary.
------
'''
def parse_lines(f):
	urls = {}
	status_codes = {}
	sizes = []
	for line in f:
		s = line.split()
		if s[8] != '"-"':
			if s[8] not in urls:
				urls[s[8]] = 1
			else:
				urls[s[8]] += 1
		if s[5] not in status_codes:
			status_codes[s[5]] = 1
		status_codes[s[5]] += 1
		sizes.append(int(s[6]))
	return urls, status_codes, sizes

'''
------
Call this function to get the average and median of a list. If the list is an odd number of elements, 
get the middle element as the median value. If it is even, average the two middle values. There might
be a way to get the average at the same time as sorting to avoid copying the list, but this code works
as is.
------
'''
def get_avg_and_med(l):
	a = sum(l) / len(l)	
	m = sorted(l)
	if len(l) % 2 == 1:
		median_val = m[len(l) / 2]
	median_val = (m[len(l) / 2] + m[len(l) / 2 - 1]) / 2
	return a, median_val

'''
------
Sort the url dictionary by value, and return the last 5 URLs and their corresponding hit counts.
------
'''
def get_top_five(d):
	url_list = sorted(d.iteritems(), key = operator.itemgetter(1))
	return url_list[-5:]

'''
Run all the things
'''
def main():
	log = open('mediacast_access.log')

	url_counts, status_counts, sizes = parse_lines(log)
	avg_val, med_val = get_avg_and_med(sizes)
	top_five = get_top_five(url_counts)
	log.close()
	print 'The average request size is %d, and the median request size is %d' % (avg_val, med_val)
	for key, value in status_counts.iteritems():
		print 'Response code %s occurred %d times' %(key, value)
	print 'The top five URLs are:'
	for item in top_five:
		print '%s was hit %s times' %(item[0], item[1])

main()