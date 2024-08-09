#******************************************************************************#
#                                                                              #
#                        TABIND scrabble project                               #
#                                                                              #
#******************************************************************************#
#                                                                              #
# FILE: Tabind scrabble project                                                #
#                                                                              #
# USAGE: Tabind scrabble project                                               #
#                                                                              #
# DESCRIPTION: Gegerates all valid Scrabble words from a set                   #
#              of given letters, in this case "TABIND"                         #
#                                                                              #
# OPTIONS: List options for the script [-h]                                    #
#                                                                              #
# DEVELOPER: Zhaoyu Li                                                         #
# DEVELOPER PHONE: +1 (530) 234-2513                                           #
# DEVELOPER EMAIL: bruce040729@gmail.com                                       #
#                                                                              #
# VERSION: 1.0                                                                 #
# CREATED DATE-TIME: 20240809-10:00 Western Time Zone USA                      #
#                                                                              #
# VERSION: 1.1                                                                 #
# REVISION DATE-TIME: YYYYMMDD-HH:MM                                           #
# DEVELOPER MAKING CHANGE: First_name Last_name                                #
# DEVELOPER MAKING CHANGE: PHONE: +1 (XXX) XXX-XXXX                            #
# DEVELOPER MAKING CHANGE: EMAIL: first.last@email.com                         #
#                                                                              #
#******************************************************************************#

This goal of this Project is to create a Python Program that takes a set of letters("tabind") and generates an alphabetical list of all possible scrabble words that can be formed by using these letters. 
Expanations:
1. Load the Dictioanry: The "load dictionary" function read text file that contains Scrabble words, and loads them into a set for fast lookup.

2. Generate Permutations: The 'generate_permutations' function create all possible permutations of the input letters of length 2 or more using 'intertools.permutation'

3.Filter Valid Words:The 'filter_valid_words' function filters the permutations to keep only those that are valid Scrabble words, then sortys the results alphabetically. 

4.Main Funciton: The 'if_name_=="_main_":'block loads the dictionary, generates permutations of the input letter, filter for valid words, and prints them in alphabetical order. 