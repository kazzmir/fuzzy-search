#!/usr/bin/env python

def fixup(letters):
    def change(letter):
        if letter == '.':
            return '\.'
        if letter.isalpha():
            return '[' + letter.lower() + letter.upper() + ']'
        return letter
    return [change(x) for x in letters]

def fuzzy_match(what):
    import os
    import re
    regex = re.compile('.*' + '.*'.join(fixup(list(what))) + '.*')
    for root, dirs, files in os.walk('.'):
        for file in files:
            if regex.match(file):
                print os.path.join(root, file)

import sys
if len(sys.argv) <= 1:
    print "Give an argument to fuzzy match."
    print "  %s Tr" % sys.argv[0]
    print "Might yield 'Tree.java' and 'Train.cpp'"
else:
    fuzzy_match(sys.argv[1])
