num1 = 5
num2 = 10
if num1 % 2 == 1:
    temp = num1
    num1 = num2
    num2 = temp
else:
print(num1, num2)