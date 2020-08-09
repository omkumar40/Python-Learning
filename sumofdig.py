#finding all the numbers and their sum from  a text file using regular expressions


import re
name = input("Enter file:")
#if len(name) < 1 : name = "regex_sum_862637.txt"
handle = open(name)
#This will find 1 or more digit numbers
x=re.findall('[0-9]+',handle.read())

x=list(map(int,x))
print(sum(x))