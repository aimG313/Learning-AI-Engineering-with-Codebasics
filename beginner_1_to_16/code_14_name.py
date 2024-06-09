def calc_area(a,b):
  print("__name__:",__name__)
  area=.5*a*b
  return area


if __name__ == "__main__":
 
 print("I am in area.py")
 area = calc_area(5,6)
 print("The area is:",area)