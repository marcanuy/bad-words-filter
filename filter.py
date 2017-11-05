#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

def filter_bad_words(entries):

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
            print "Remove: %s" % quote
    print "Removed %s items." % (original_count - len(entries))

def findWholeWord(w):
    """ removes exact word"""
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def main():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        entries = {}
        for key, quote in enumerate(quotes):
            entry_key = "example{}".format(key)
            entries[entry_key] = {'quote': quote}
        print(entries)
        filter_bad_words(entries)

if __name__ == "__main__":
        main()

    
    
