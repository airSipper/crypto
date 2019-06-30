# Prime or composite

def comp_or_prime(lower, upper):
	""" show if numbers in a range are prime or composite """

	for num in range(lower, upper + 1):
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					print("{} : Composite".format(num))
					break
			else:
				print("{} : Prime !".format(num)) 

## test
#comp_or_prime(10, 100)
