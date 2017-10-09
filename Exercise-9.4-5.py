##Exercise 5: This program records the domain name (instead of the address) 
##where the message was sent from instead of who the mail came from (i.e., the whole email address).
## At the end of the program, print out the contents of your dictionary.

fname = 'mbox-short.txt'
lines = [line.strip("\n") for line in open(fname, 'r')
         if line.startswith("From") and not line.startswith("From:")]

who_dict = {}

for line in lines:
    line = line.split()
    word = line[1]
    email = word.split("@")
    who_dict[email[1]] = who_dict.get(email[1],0) + 1
print(who_dict)