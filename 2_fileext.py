'''
Take a filename from user and print its extension
~Akanksha
'''

#First take filename as input
fn = input("Input the filename : ")

#Now seperate name from extension
#we use split function
#split function separates a string into a list
#It splits at each occurence of the substring in paranthesis
f = fn.split('.')

#extension is the last part of the filename
#so it is the last member of the list
print('The extension of the file is : ' + f[-1])
