#!/usr/bin/python3

# fenton: specify target word then find the top n words from a
# dictionary which are closest using distance matching methods
#
# copyright 2020 Gregory V. Perry || GregoryVPerry@pm.me
#
# LICENSE: you are free to use this source code in any way you want, as long as you give me a shout out with
#          my email address on any deriviative code implementation and/or published research that follows.
#

import argparse, heapq, jellyfish, string, sys, textwrap
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


parser = argparse.ArgumentParser(description = 'fenton: specify target word then find the top n words from a dictionary\n\
        which are closest using distance matching methods',
        usage = 'python3 %(prog)s [-h] TARGETWORD [-m 1|2|3|4|5|6|7] [-d DICTIONARY] [-n NUMWORDS] [-l] [-s] [-v]',
        formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument('targetword', metavar = 'TARGETWORD', type = str, nargs = '+',
                    help = 'target word to analyze')

parser.add_argument('-m', '--method', action = 'store', dest = 'method',
                    default = 7, help = 'distance matching method to use, default = 7\n1 = Damerau-Levenshtein Distance\n\
2 = Hamming Distance\n3 = Jaro Distance\n4 = Jaro-Winkler Distance\n5 = Levenshtein Distance #1\n\
6 = Levenshtein Distance #2\n7 = The Kitchen Sink', type = int)

parser.add_argument('-d', '--dictionary', action = 'store', dest = 'dictionary',
                    default = 'words.txt', help = 'dictionary of words to compare, default words.txt', type = str)

parser.add_argument('-n', '--number', action = 'store', dest = 'numwords',
                    default = 10, help = 'number of matches to return, default 10', type = int)

parser.add_argument('-l', '--lower', action = 'store_true', default = False,
                    dest = 'lower',
                    help = 'convert dictionary to lowercase before analysis')

parser.add_argument('-s', '--strip', action = 'store_true', default = False,
                    dest = 'strip',
                    help = 'strip punctuation from dictionary before analysis')

parser.add_argument('-v', '--verbose', action = 'store_true', default = False,
                    dest = 'verbose',
                    help = 'verbose mode')

results = parser.parse_args()

def printsmallheap():
    for x in heapq.nsmallest(results.numwords, h):
        print(x[0], x[1])

def printlargeheap():
    for x in heapq.nlargest(results.numwords, h):
        print(x[0], x[1])

if results.verbose == True:
    print('targetword        = ', results.targetword[0])
    print('method            = ', results.method)
    print('dictionary        = ', results.dictionary)
    print('number of matches = ', results.numwords)
    print('lower             = ', results.lower)
    print('strip             = ', results.strip)
    print('verbose           = ', results.verbose)

with open(results.dictionary, 'r') as wordlist:
    wordlist = wordlist.read().splitlines()
    if results.lower == True:
        wordlist = list(map(str.lower, wordlist))

    if results.strip == True:
        table = str.maketrans('', '', string.punctuation)
        wordlist = [w.translate(table) for w in wordlist]

    print()

    if results.method == 1 or results.method == 7:
        print("Results for", results.targetword[0], "using Damerau-Levenshtein Distance:")
        print()
        h = []
        for line in wordlist:
            heapq.heappush(h, (jellyfish.damerau_levenshtein_distance(results.targetword[0], line), line))
        printsmallheap()
        print()

    if results.method == 2 or results.method == 7:
        print("Results for", results.targetword[0], "using Hamming Distance:")
        print()
        h = []
        for line in wordlist:
            heapq.heappush(h, (jellyfish.hamming_distance(results.targetword[0], line), line))
        printsmallheap()
        print()

    if results.method == 3 or results.method == 7:
        print("Results for", results.targetword[0], "using Jaro Distance:")
        print()
        h = []
        for line in wordlist:
            heapq.heappush(h, (jellyfish.jaro_distance(results.targetword[0], line), line))
        printlargeheap()
        print()

    if results.method == 4 or results.method == 7:
        print("Results for", results.targetword[0], "using Jaro-Winkler Distance:")
        print()
        h = []
        for line in wordlist:
            heapq.heappush(h, (jellyfish.jaro_winkler(results.targetword[0], line), line))
        printlargeheap()
        print()

    if results.method == 5 or results.method == 7:
        print("Results for", results.targetword[0], "using Levenshtein Distance #1:")
        print()
        h = []
        for line in wordlist:
            heapq.heappush(h, (fuzz.ratio(results.targetword, line), line))
        printlargeheap()
        print()

    if results.method == 6 or results.method == 7:
        print("Results for", results.targetword[0], "using Levenshtein Distance #2:")
        print()
        h = []
        for line in wordlist:
            heapq.heappush(h, (jellyfish.levenshtein_distance(results.targetword[0], line), line))
        printsmallheap()
        print()
