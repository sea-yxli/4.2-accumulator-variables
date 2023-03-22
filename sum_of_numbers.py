# calculate the sum of the numbers from 1 to 10.
count = 1
total = 0
while count <= 10:
  print(count)
  total += count
  count += 1
print(total)
# calculate the sum of the numbers from 100 to 200.
sum_1 = 0
count = 100
while count <= 200:
  print(count)
  sum_1 += count
  count += 1
print(sum_1)
# calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.
sum_2 = 0
count = 200
while count <= 300:
  print(count)
  sum_2 += count
  count += 1
print(sum_1 - sum_2)
# calculate the sum of the multiples of 5 between the numbers 1000 and 10000.
total = 0
count = 1000
while count <= 10000:
  print(count)
  total += count
  count += 5
print(total)
# calculate the sum of the multiples of 5 between 1 and 100, but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.
total = 0
count = 0
while count <= 100:
  print(count)
  if not count%3 == 0:
    total += count
  count += 5
print(total) 
