import markovify # import markovify library

# load the text file, open, & read
text = open("combinedtext.txt").read()

# initialize the Markov generator
generator = markovify.Text(text, state_size=2)

paragraph = "" # string to store the final essay & accumulate sentences
word_count = 0 # word count to ensure I reach 250 words
unique_sentences = set() # set that stores sentences that have already been used
last_words = [] # list that keeps track of the last two words from each sentence to ensure they don't repeat in the next sentence

# create forbidden phrases list
forbidden_phrases = [
    "soft and white", 
    "measured and slow", 
    "go to another country", 
    "calls to you like the wild geese", 
    "sun rays"
]

# defining my custom rules:

def starts_with_conjunction(sentence): # def = defining a new function, check if a sentence starts with a conjunction
    conjunctions = ["and", "but", "or", "so", "for", "nor", "yet"] # define list of conjunctions
    first_word = sentence.split()[0].lower() if sentence else "" # takes the sentence and splits it into individual words, based on spaces. Zero means it's calling on the first word in the sentence and lower converts it to lowercase making sure the word is not case sensitive. I want the code to recognize both and & And. 
    # if the sentence is empty, the furst word will be sent to an empty string -- ensures there won't be errors when trying to split an empty sentence
    return first_word in conjunctions # check if the first word is a conjunction. It will return True if it starts with one and False if it doesn't.

def avoid_repetitive_words(sentence):
    words = sentence.split() #split sentence into words
    if last_words and words[0] in last_words: # last_words is defined later in the code as the last two words of each sentence.. if the first word in words list is in last_words, return the next word
        return " ".join(words[1:])  # aka remove the first word to avoid repetition
    return sentence

def check_capitalization_and_punctuation(sentence):
    if sentence and not sentence[0].isupper(): # if sentence checks to make sure the sentence isn't empty, not sentence[0] checks to see if the first letter is uppercase. If it is, it returns True, if not, it returns false.
        sentence = sentence.capitalize()  # capitalize the first letter
    if not sentence.endswith(('.', '?', '!')): # checks if sentence ends with punctuation (T/F)
        sentence += '.'  # If the statement is T, the +- appends the code and adds a punctuation mark to the end of the sentence
    return sentence

# loop until we reach approximately 250 words
while word_count < 250:
    # generate a new sentence
    sentence = generator.make_sentence()

    # ensure the sentence is unique and non-empty
    if sentence and sentence not in unique_sentences:
        # check for forbidden phrases
        if any(phrase in sentence for phrase in forbidden_phrases):
            continue  # skip this if a forbidden phrase is found

        # apply/ call on the custom rules from above
        if not starts_with_conjunction(sentence):  # check if it doesn't start with a conjunction
            sentence = avoid_repetitive_words(sentence)
            sentence = check_capitalization_and_punctuation(sentence)

            # Add the modified sentence to the paragraph
            unique_sentences.add(sentence)
            paragraph += sentence + " "
            word_count += len(sentence.split())  # Update word count

            # update the last words to avoid repetition
            last_words = sentence.split()[-2:]  # Keep track of the last two words

# save the generated paragraph to a text file
with open("essay.txt", "w") as essay_file: # w = write mode, this indicated that if continue to run this code, the paragraph will overwrite the content before 
    essay_file.write(paragraph)

print("\n\n\nEssay saved as 'essay.txt'\n\n\n")

# \n\n\n adds three line breaks before and after it says "essay saved.."









