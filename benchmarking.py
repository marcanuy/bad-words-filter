#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from nltk import word_tokenize
import re
import timeit

def filter_bad_words_with_set(entries):
    with open("badwords.txt", "r") as f:
        badwords = set(word.strip() for word in f)

    filtered_entries = {}
    for key, item in entries.items():
        quote = item['quote']
        words = word_tokenize(quote)

        if not any(word in badwords for word in words):
            filtered_entries[key] = {'quote': quote}

    return filtered_entries

def filter_bad_words_with_regex(entries):

    f = open("badwords.txt", "r")
    badwords = f.readlines()

    # remove new lines from each word
    for i in range(len(badwords)):
            badwords[i] = badwords[i].strip('\n')

    original_count = len(entries)
    for key, item in entries.items():
        quote = item['quote']
        if any(findWholeWord(x)(quote) for x in badwords):
            del entries[key]

def findWholeWord(w):
    """ removes exact word"""
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def main():
    filter_time()
    filter_set_time()

def filter_time():
    SETUP_CODE = '''
from __main__ import filter_bad_words
from nltk import word_tokenize
import re'''
 
    TEST_CODE = '''
with open("quotes.txt", "r") as f:
       entries = {
           "example{}".format(index): {'quote': quote}
           for index, quote in enumerate(f)
       }
       filter_bad_words_with_regex(entries)'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 1000)
 
    # priniting minimum exec. time
    print('Filter time: {}'.format(min(times)))        

def filter_set_time():
    SETUP_CODE = '''
from __main__ import filter_bad_words_with_set
from nltk import word_tokenize
import re'''
 
    TEST_CODE = '''
with open("quotes.txt", "r") as f:
       entries = {
           "example{}".format(index): {'quote': quote}
           for index, quote in enumerate(f)
       }
       filter_bad_words_with_set(entries)'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 1000)
 
    # priniting minimum exec. time
    print('Filter time with set: {}'.format(min(times)))        
 


if __name__ == "__main__":
    main()
