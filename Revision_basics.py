##pattern printing

##*
##**
##***
##****

for x in range(5,0,-1):
    print(x*''+(5-x)*'*')
print('')

#############################################

#binary formatting

o=21
print('{0:b}'.format(o))
print()

#############################################

#format example
android = 9.01
type_def= "pie"

print('{} is the new android version "{}"'.format(android,type_def))
print()

#############################################

#join/concatenating example
food_items = ['chaat','samosa','pakoda']
print(', '.join(food_items))
print()
print()

#############################################

#rectangle pattern
def rectangle(m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(i==1 or i== m or j==1 or j==n):
                print('*',end="")
            else:
                print(" ",end="")
        print()

rows=int(input())
column=int(input())

rectangle(rows,column)

print()
print()

#############################################

#square pattern

def square(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1 or i==n or j==1 or j==n):
                print('*',end="")
            else:
                print(" ",end="")
        print()

side = int(input())
square(side)

print()
print()

##############################################

#statistics_basic

import statistics
#from statistics import mean as m

example_list= [5,7,2,15,12,10,8,9,14,11,12]

x= statistics.mean(example_list)
print(x)
#print(m(example_list))

y= statistics.mode(example_list)
print(y)

z=statistics.median(example_list)
print(z)

m= statistics.stdev(example_list)
print(m)

n= statistics.variance(example_list)
print(n)

print()
print()


##############################################


# 


