##Gavin Swiger
##September 15th 2020
## Module 2 | SDLC Assignment

##Write a text analyzer that reads a file and outputs statistics about that file.
##It should output the word frequencies of all words in the file,sorted by the most frequently used word.
##The output should be a set of pairs, each pair containing a word and how many times it occurred in the file.


import re


def clean_the_poem(poem):
    ##Clean the poem string variable
    poem = poem.replace(',',' ')
    poem = poem.replace('â€',' ') ##Was used as online line continuation character.
    poem = re.sub('[\W_]+', ' ', poem)
    poem = poem.lower()##Changes the string to all lower case.
    poem = poem.split()
    return poem;

def main():

    ##Open and store the file as a string.
    with open("Module 2 Poem.txt", "r") as file:
        poem = file.read().replace('\n', ' ')

    poem = clean_the_poem(poem);


    ##Make a list of all the different words in the poem.
    unique_words = []

    for word in poem:
        if word not in unique_words:
            unique_words.append(word)


    ##Make a dictionary with words as "keys" and occurrance rate as "values"

    unique_word_dict = {}
    for word in unique_words:
        item = {word: poem.count(word)}
        unique_word_dict.update(item)

    ##Make a new dictionary with words sorted by occurrance rate.
    ##This sorts into accending order.
    sorted_unique_word_dict = sorted(unique_word_dict.items(), key=lambda x: x[1])


    ##Loop through dictionary backwards printing value and key.
    i = len(sorted_unique_word_dict) - 1

    while(i != -1):
        print(sorted_unique_word_dict[i])
        i = i-1
    

if __name__ == "__main__":
    main()






    



