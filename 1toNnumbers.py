#Program to Print numbers from 1 to n

def gagan(n):
	if n > 0:
		gagan(n - 1)
		print(n, end = ' ')

# Driver code
gagan(100)