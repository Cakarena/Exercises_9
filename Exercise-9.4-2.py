##Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
## To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. 
##At the end of the program print out the contents of your dictionary (order does not matter).

fname = 'mbox-short.txt'
lines = [line.strip("\n") for line in open(fname, 'r')
         if line.startswith("From") and not line.startswith("From:")]

days_dict = {}

for line in lines:
    words = line.split()
    days_dict[words[2]] = days_dict.get(words[2],0) + 1
    ##We can use get to write our histogram loop more concisely. 
    ##Because the get method automatically handles the case where a key is not in a dictionary,
    ## we can reduce four lines down to one and eliminate the if statement.

print(days_dict)

