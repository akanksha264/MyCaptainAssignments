'''
Take a string as input and print letter in decreasing order of frequency
use dictionary
~Akanksha
'''

#create a function to create the dictionary
def create_d(s):
    #create an empty dictionary
    d = {}
    #for all letters in string count frequency
    for key in s:
        #get function returns value and key from dictionary (using 0 as default)
        d[key] = d.get(key,0) + 1
    return d
        
#create a function to print dictionary in sorted order
def print_d (d):
    #create a list of frequencies
    l = []
    for key in d:
        #if frequency already not present in list add it
        if d[key] not in l:
            l.append(d[key])
            
    #now sort frequencies in reverse order
    l.sort(reverse = True)
    
    #print keys in dictionary with frequencies
    for freq in l:
        for key in d:
            if (d[key] == freq):
                print (key + ' = ' , freq)




#Take string from user
st = input ('Enter a string : ')

#create dictionary
diction = create_d(st)

#print in decreasing frequency
print_d(diction)
