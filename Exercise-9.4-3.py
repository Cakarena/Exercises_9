##Exercise 3: Write a program to read through a mail log, 
##build a histogram using a dictionary to count how many messages have come from each email address, 
##and print the dictionary.

fname = 'mbox-short.txt'
lines = [line.strip("\n") for line in open(fname, 'r')
         if line.startswith("From") and not line.startswith("From:")]

who_dict = {}

for line in lines:
    words = line.split()
    who_dict[words[1]] = who_dict.get(words[1],0) + 1
    ##We can use get to write our histogram loop more concisely. 
    ##Because the get method automatically handles the case where a key is not in a dictionary,
    ## we can reduce four lines down to one and eliminate the if statement.

print(who_dict)
#This is the same as exercise 9.2 except you're selecting the second string not the third.
