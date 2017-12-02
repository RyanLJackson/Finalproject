'''
Created on Nov 18, 2017

@author: ITAUser
'''
#open the text file
#read the file 
#split the file
#count the letters

def countingletters(filename, mychar):
    f = open(filename,'r')
    count = 0;
    isDone = False
    while not isDone:
        char=f.read(1)
        char = char.lower()
        if char == mychar:
            count = count +1;
        if char == '':
            isDone = True 
    print(count)
    return count 
import string 
c = countingletters 
#make a list with the alphabet
letters = list(string.ascii_lowercase)
#make a list to store the count of each letter
letnum = []
#make loop that counts how many of each letter there are 
for i in letters:
    count = countingletters('constituton.txt',i)
    letnum.append(count)
        
#define the maximum value
maxval = max(letnum)
#Find the letter at the max value 
index = letnum.index(maxval)
let =letters[index]
#print the answer          
print (let,maxval)