barcode = 0
correct_numbers = 0
for i in range(0,1):
  barcode = str(input('>'))
  numbers = list(barcode)
  sum = 0
  checkdigit = 0
  for j in range(0,5):
    if j == 1 or j == 3:
      sum = sum + (3 * (int(numbers[j])))
    else:
      sum = sum + int(numbers[j])
  checkdigit = sum % 10
  if checkdigit == int(numbers[5]):
    correct_numbers += 1
print('The number of barcodes input correctly were: ' + str(correct_numbers))
