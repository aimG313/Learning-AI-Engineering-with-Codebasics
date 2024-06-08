def calc_area(a,b):
  area=.5*a*b
  return area

a=float(input("give length:"))
b=float(input("give height:"))

area = calc_area(a,b)
print("The area is:",area)