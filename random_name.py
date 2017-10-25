from random import randint
def randlist(r):
	alpha = ["a","b","c","d","e","f"]
	used = [0,0,0,0,0,0]
	used[r] = 1
	c = alpha[r]
	print (used)
	return c
   
def main():
	done = False
	while done == False:
		r = randint(0,5)
		c = randlist(r)
		#print (used)
		print(c,end="")
main()
