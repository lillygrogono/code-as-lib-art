import sys

# Question One:
# python3 assignment3.py pineapple cherry apple

word_list = sys.argv 
word_list.pop(0) # removes name of python file

word_list = sorted(word_list) # sorts the remaining words

print("alphabetically organized word list:", word_list)

