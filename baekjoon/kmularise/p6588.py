def check_goldbach(num, sieve):
	for i in range(3, num // 2 + 1):
		if sieve[i] == True and sieve[num - i] == True:
			print(num, "=", i, "+", num - i)
			return True
	print("Goldbach's conjecture is wrong.")
	return False

def prime_sieve(n):
	sieve = [True] * n
	max_sqrt_n = int (n ** 0.5)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, max_sqrt_n + 1):
		if sieve[i] == True:
			for j in range(2 * i, n, i):
				sieve[j] = False
	sieve[2] = False
	return sieve

num_set = []
while True:

	num = int(input())
	if num == 0:
		break
	num_set.append(num)
sieve = prime_sieve(max(num_set))
for num in num_set:	
	check_goldbach(num,sieve)