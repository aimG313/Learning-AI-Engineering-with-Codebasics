x = input("x:")
y = float(input("y:"))

try:
  z = x/y
except ZeroDivisionError as e:
  print('Division by zero exception:', e)
  z = None
except TypeError as e:
  print('Type error exception:', type(e),__name__)
  z = None
print("Division is: ",z) 

