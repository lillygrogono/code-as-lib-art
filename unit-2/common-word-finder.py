file = "assignment-1.txt"

strawberry = {}

with open(file, "r") as file:
    for line in file:
        for word in line.split():
            strawberry[word] = strawberry.get(word, 0) + 1  
            
            # I HAD to look this part up because I could not figure out how to write a for loop for this, but I didn't copy and paste and I do understand it!
            # .get() is used to retrieve a word in the dictionary
            # if the word doesn't exist, start the count at zero and then add one
            # as the computer goes through each line, it will update with each word it runs into — so if it sees "and" again it will add another 1 to the count 

sorted_strawberry = sorted(strawberry.items(), key=lambda x: x[1], reverse=True)

# The sorted() function takes my dictionary (strawberry) and sorts it into a new list using the tupples - sorted would normally go in ascending order but we want largest to smallest which is why I used reverse=True
# The key=lambda x: x[1] is a function that tells the computer to sort by the second part of each tupple 
# x is equal to (key,value) SO in this case - x[0] would be key and x[1] would be the value AKA the count

print("Words sorted by frequency:")
for word, count in sorted_strawberry[:10]:  
    print(f"{word}: {count}")

# print(strawberry)

# telling it to display the top 10 words, and write it in the format word: count
  
# PART ONE:
# The: 141
# And: 109
# To: 108
# Of: 108
# I: 70
# In: 65
# My: 55
# It: 51
# A: 49
# Not: 48

# PART THREE:
# I'm not sure yet if this is something that makes total sense for the Unit 2 project, but I'm in two classes that are based around global security, conflict, and human rights... I'm wondering if I could do some sorting through official UN documents and treaties to see how often they use certain words/ verbiage.. maybe there would be a deeper meaning there to dive into?

