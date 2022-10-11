#File: Nonword Generator.txt

# By Ki James

import os
import csv
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('data/aralex.csv', newline='') as f:
    reader = csv.reader(f)
    rootlist = list(reader)

charList = "btvjHxd*rzs$SDTZEgfqklmnhwyY"

numofwords = int(input("How many roots would you like to generate?"))

word = ""

for i in range(0, numofwords):  
    for x in range(0, 3):
        word += (random.choice(charList))
    if word in rootlist:
        numofwords+1
        word = ""
    else:
        print(word)
        word = ""
