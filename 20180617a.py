import os, re, glob

scorelist = [100, 50, 80, 200, 10000]

total = 0
for score in scorelist:
	total = total + score
print("合計=", total)

