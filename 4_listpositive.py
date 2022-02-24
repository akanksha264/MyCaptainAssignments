'''
Print positive numbers in a list
~Akanksha
'''

#create an empty list l1
l1 = []

#input list from user
n = int(input("Enter number of terms in the list : "))
print ("Enter elements in the list : ")
for i in range (0,n):
    x = int(input())
    l1.append(x)

#create another list for positive numbers
l2 = []
for num in l1:
    #for every number in l1 append it in l2 if it is positive
    if num > 0:
        l2.append(num)

print ("Input list : " , l1)
print ("Output list :" , l2)
