'''
functions in computer programming is used to create a
block of code that can be reused

'''


# create a function in python

# does not take any argument

def sqr(x):

  print(x**2)

sqr(6)

# assignment
# write a function that computes the sum of any two numbers

def sum(x,y):

    print(x + y)


sum(5,6)
# function that returns a value 

def findDifference(x,y):

  return x-y

difference = findDifference(8,8)

print(difference)

###########################################
# CONTROL STATEMENTS
'''
- if
- else
- while
- for

'''

age = 12

if age > 10:
  print("age is greater than 10")
else:
  print("age not greater than 10")


while True:

  age = int(input("enter your age:"))

  if age == 3:

    print("you are too young")
    break

name = "Joshua" # ["J","o","s","h","u","a"]

for j in name:

  print(j)


for J,j in enumerate(name):

  print("index: ",J, "value: "+j)


'''

1. j =J
2. j =o

'''


















