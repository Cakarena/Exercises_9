##Exercise 4: Add code to the above program (Exercise 3) to figure out who has the most messages in the file.
##fter all the data has been read and the dictionary has been created, 
##look through the dictionary using a maximum loop (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.


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

mostmessage = 0
most_person = None
for person in who_dict:
	if who_dict[person] > mostmessage:
		mostmessage = who_dict[person]
		most_person = person
print(most_person, who_dict[most_person])
#This is the same as exercise 9.2 except you're selecting the second string not the third.