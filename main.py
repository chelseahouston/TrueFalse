def print_output(a,b):
  if a == True and b == False:
    print("a is true, b is false")
  if a == True or b == True:
    print("a or b is true")
  if a == False and b == True:
    print("a is false and b is true")
  if a == False and b is False:
    print("a is false and b is false")
  if a == False or b == False:
    print("a or b is false")
  else:
    print("none are true")
print_output(True,False)
