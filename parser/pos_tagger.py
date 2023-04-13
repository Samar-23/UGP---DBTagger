import os
from nltk.tag import StanfordPOSTagger

# Set the path to the tagger and model files
stanford_dir = 'stanford-postagger-full-2020-11-17'
modelfile = stanford_dir + '/models/english-left3words-distsim.tagger'
jarfile = stanford_dir + '/stanford-postagger.jar'

# Initialize the tagger
tagger = StanfordPOSTagger(modelfile, jarfile)

# Take input sentence from user
sentence = input("Enter an English sentence: ")

# Tag the sentence
tagged_words = tagger.tag(sentence.split())

# Join the tagged words into a string with the specified format
tagged_sentence = ' '.join([f"{word}/{tag}/" for word, tag in tagged_words])

# Print the tagged sentence
print(tagged_sentence)
