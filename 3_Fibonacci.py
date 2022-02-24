'''
Print Fibonacci Sequence
~Akanksha
'''

#input number of terms from user
n = int(input ("Enter number of terms : "))

#initialize two values as 0 and 1
a = 0
b = 1

#loop n times
for i in range (0,n):
        #print a
        print (a)
        #next term is the sum of previous 2 terms
        c = a+b
        #for next iteration update values of a and b
        a = b
        b = c
