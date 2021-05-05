
def fizz_buzz():
	for number in range(1, 30):
		if number % 3 == 0 and number % 5 == 0:
			print(f'{number} - FizzBuzz')
		elif number % 3 == 0:
			print(f'{number} - Fizz')
		elif number % 5 == 0:
			print(f'{number} - Buzz')
		else:
			print(f'{number} - {number}')


fizz_buzz()
