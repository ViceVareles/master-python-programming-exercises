# Complete the function to return the previous and next number of a given number
def previous_next(num):
  # Your code here
 num = int(num)
  a = num - 1
  b = num + 1
  return a, b


# Invoke the function with any integer as its argument
print(previous_next(179))
