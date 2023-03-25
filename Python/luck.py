import random
score = random.randint(1,100)

if score == 100:
  print("奇跡です！")
elif score >= 60:
  print(str(score) + "点です！" + "\n" + "合格です！")
else:
  print(str(score) + "点です・・・" + "\n" + "不合格です。")
