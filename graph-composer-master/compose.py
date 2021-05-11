"""
Implemented Markov Chain Composer by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
"""

import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) # this is saying to turn whitespaces into spaces. Very important!
        text = text.lower() # make everything lowercase to compare stuff
        # now we could be complex and deal with punctuation... but there are cases where 
        # you might add a period such as (Mr. Brightside), but that's not really
        # punctuation... so we just remove all the punctuation > 
        # Hello! it's me. --> hello its me etc
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() # split on spaces again

    words = words[:1000]

    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)
        # set our word to the previous word and iterate
        prev_word = word_vertex

    # now remember that we want to generate the probability mappings before composing
    # this is a great place to do that before we return the graph object
    g.generate_probability_mappings()
    
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start!
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    # step 1: get words fromtext
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song in os.listdir('songs/{}'.format(artist)):
        # if song == '.DS_Store':
        #     continue
        # words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))
        
    # step 2: make a graph using those words
    g = make_graph(words)
    # step 3: get the next word for x number of words (defined by user)
    # step 4: show the user
    composition = compose(g, words, 100) # inc params 
    print(' '.join(composition)) # return string, where all of the words are seperated by a space!!


if __name__ == '__main__':
    main()