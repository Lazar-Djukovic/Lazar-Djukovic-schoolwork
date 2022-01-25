import numbers


def addnums(number):
  sum = 0
  for n in number:
    sum = sum + n
  return sum

def raddnums(number):
  if len(number) == 1:
    return number[0]
  else:
    return

marks = [3,6,2,8,1]
total = addnums(marks)
print(total)