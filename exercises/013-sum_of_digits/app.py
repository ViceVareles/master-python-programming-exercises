# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  uno = int(str(num)[0])
  dos = int(str(num)[1])
  tres = int(str(num)[2])
  return uno + dos + tres


# Invoke the function with any three-digit number
print(digits_sum(123))
