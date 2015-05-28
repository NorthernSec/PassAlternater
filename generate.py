#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Takes one or more words and generates possible leetified passwords

# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels
# This software is licensed under the Original BSD License

# Imports
from itertools import product
import argparse
import fileinput

# Variables
leetlist=[['a','A','@','4'],['b','B','8'],['c','C','('],['d','D'],
          ['e','E','€','3'],['f','F'],['g','G','6'],['h','H'],
          ['i','I','1','1'],['j','J'],['k','K'],['l','L','1','7'],
          ['m','M'],['n','N'],['o','O','0'],['p','P'],['q','Q','9'],
          ['r','R'],['s','S','5'],['t','T','7'],['u','U'],['v','V'],
          ['w','W'],['x','X'],['y','Y'],['z','Z','2']]

# Functions
def generate(word):
  w=list(word.lower())
  c=[]
  for l in w:
    g=[]
    for tg in leetlist:
      if l == tg[0]:
        g=tg;break
    c.append(g) if len(g)>0 else c.append([l])
  o=list(product(*c))
  return [''.join(x) for x in o]

def importList(file):
  global leetlist
  l = open(file,'r')
  lst = [[y.strip() for y in x.split(',')] for x in l]
  leetlist=lst

if __name__ == '__main__':
  # Parse arguments
  description='''Takes one or more words and generates possible leetified passwords.'''

  parser = argparse.ArgumentParser(description=description)
  parser.add_argument('word',  metavar='word', type=str, help='Word used to generate the passwords', nargs="?" )
  parser.add_argument('-s',    action='store_true',      help='Show statistics')
  parser.add_argument('-v',    action='store_true',      help='Verbose')
  parser.add_argument('-l',    metavar='list', type=str, help='Supply new combination list' )
  parser.add_argument('-o',    metavar='file', type=str, help='Output file')
  args = parser.parse_args()

  # Import new list if requested
  if args.l:
     importList(args.l)
     if args.v:
       print("List imported: %s"%args.l)
       print(leetlist)

  # Generate word list
  if args.word:
    wordlist=generate(args.word)
  else:
    # Read from stdin
    words=[]
    for line in fileinput.input(): words.append(line.strip())
    wordlist=[]
    for word in words: wordlist.extend(generate(word))

  if args.s:
    print("Word length:            %s"%len(args.word))
    print("Number of combinations: %s"%len(wordlist))
  else:
    if not args.o or args.v:
      print('\n'.join(wordlist))
  # Save to file
  if args.o:
    f=open(args.o,'w')
    f.write('\n'.join(wordlist))
