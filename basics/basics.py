
'''
## Basic Programming

Write a method that reverses a String (without using a built-in language method like String#reverse in Ruby).  Ideally, do this without allocating memory for another String.

    e.g. string_reverse("the_string") => "gnirts_eht"
'''

'''
We can treat strings as lists for indexing, but since strings are immutable,
we can't reverse them by reassigning elements as we would be able to 
reverse a list:
def reverse_list(l):
	v = None
	for i in range(len(l) / 2):
		v = l[i]
		l[i] = l[len(l) - i - 1]
		l[len(l) - i
	return l
However, we can use slice on the string to step over each character in reverse.
In the following notation, slice takes up to three arguments: stop, start, and 
step. The : notates beginning or end of the list depending on where it is placed.
Step denotes how many elements to move over each time. A positive number is forward
movement over the list or string, and negative number is backward movement. Hence, 
::-1 starts at the beginning of the string, and goes to the end in reverse order. 
'''
def reverse_string(word):
	return word[::-1]


'''
Write a method that returns the n'th integer in the Fibonacci sequence.

    find_fib(1) => 0
    find_fib(5) => 3

Base cases for fibonacci sequence are 0 and 1, so we can create a list with 
those as default values. Using a loop, iterate over the list n-2 times (so we dont
create more numbers in the sequence than we need) and add the two adjacent numbers, 
appending to the list to get the next number in the series.
'''

def fibonacci(n):
	l = [0, 1]
	for i in range(n - 2):
		l.append(l[i] + l[i + 1])
	return l[n - 1]



