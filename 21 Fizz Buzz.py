21. Fizz Buzz

for num in range(1, 101, +1):
  if num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  else:
    print(num)