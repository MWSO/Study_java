score = [80,98,23,47,65,19]
total = 0

for i in score:
  total = total + i

print(total)

test = 5
abai = 0
a_total = 0
for a in range(15):
  abai = (test * a)
  a_total += abai
print(a_total)

import random
rand_a = random.randint(1,50)
rand_b = random.randint(1,50)
rand_c = random.randint(1,50)
rand_total = rand_a + rand_b + rand_c
if rand_total >= 100:
  print(str(rand_total)+"点です"+"\n"+"運がいい！")
else:
  print(str(rand_total)+"点です"+"\n"+"そうでもない")