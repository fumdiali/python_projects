# fibonacci experience

def fibo_cur(n):
  if n <= 1:
    return n
  else:
    return(fibo_cur(n - 1) + fibo_cur(n - 2))


nterm = int(input("Enter number of terms: "))
if nterm <= 0:
  print("Please,enter a POSITIVE integer!")
else:
  print("Your sequence: ")
  for i in range(nterm):
    print(fibo_cur(i))

