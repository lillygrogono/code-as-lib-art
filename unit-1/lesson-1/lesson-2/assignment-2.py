from unit1lesson2 import *

#number_list.sort()
#print("The smallest number in the list is:", number_list[0])

# the code tells it to pull the list from unit1lesson2 and sort it and show us the smallest number in the list closest to zero.

# number_list.sort()

# for x in number_list:
 #   if x > 500:
  #    print(x)

#number_list.sort()
#even_numbers = []
#for num in number_list:
  #  if num % 2==0:
  #      even_numbers.append(num)

#even_numbers.sort()       
#print(even_numbers[0])

#append adds the value of num to the end of the list and in this case we defined num as even numbers only

#word_list.sort()
#last_word = max(word_list)
#print("The word that is last alphabetically is:", last_word)

word_list.sort()
longest_word = max(word_list, key=len)
print("The longest word in the list is:", longest_word)

# the max function is used to find the largest item in a set
# the key function tells the code to sort by length