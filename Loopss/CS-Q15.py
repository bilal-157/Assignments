
value = int(input('enter the value'))

even = 0
odd = 0
for x in range(2,value+1,2):
  even = even + x
print("even sum to the given number is = " ,even)
for i in range(1,value+1,2):
   odd = odd + i
print("odd sum to the given number is = ",odd)
