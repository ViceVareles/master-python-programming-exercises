# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  digito_uno = num // 10
  digito_dos = num % 10
  return digito_dos, digito_uno
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
