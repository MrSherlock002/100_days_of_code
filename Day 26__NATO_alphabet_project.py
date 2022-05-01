##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (1/05/2022)
##  Day 26__NATO_alphabet_project
##
##########################################################################

import  pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
#TODO 1. Create a dictionary in this format:

phonetic_dict ={ row.letter : row.code for (index,row) in data.iterrows() }
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word : ").upper()
output_list =[phonetic_dict[letter] for letter in word]
print(output_list)


##########################################################################
# 
# letter,code
# A,Alfa
# B,Bravo
# C,Charlie
# D,Delta
# E,Echo
# F,Foxtrot
# G,Golf
# H,Hotel
# I,India
# J,Juliet
# K,Kilo
# L,Lima
# M,Mike
# N,November
# O,Oscar
# P,Papa
# Q,Quebec
# R,Romeo
# S,Sierra
# T,Tango
# U,Uniform
# V,Victor
# W,Whiskey
# X,X-ray
# Y,Yankee
# Z,Zulu

##########################################################################
                                    # Happy Coding #
##########################################################################
