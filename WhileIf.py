
sentence = ['big', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy','quit', 'dog']

for word in sentence:
    if word == "quit":
        print("Time to quit")
        break
    else:
        print(word)
else:
    print ("There was no 'quit' in the sentence")
print ("Now we're done....")