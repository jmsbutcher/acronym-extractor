#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:37:03 2020

@author: JamesButcher

This app scans over a PDF document and attempts to extract all the
acronyms, printing them out next to their meanings, with page numbers
referring to where they first appear in the paper for easy reference.

- You must input the exact name of the PDF.
- The PDF must be in the same folder as this program.
       
"""

import PyPDF2
from pathlib import Path

# Initialize empty dict of acronyms
acronyms = dict()

# Open the PDF file
filename = input("Enter the PDF file name:")
filepath = Path.cwd() / filename
with open(filepath, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    page_count = pdf_reader.numPages
    
    for page_number in range(page_count):
        page_object = pdf_reader.getPage(page_number)
        page_text = page_object.extractText()
        
        for i in range(len(page_text)):
            origin = i
            
            # Look for opening parenthesis.
            if page_text[i] == '(' and ( page_text[i + 3] == ')' or
                                         page_text[i + 4] == ')' or
                                         page_text[i + 5] == ')' or
                                         page_text[i + 6] == ')' ):
                # If a closing ')' is 3-6 characters away, create new acronym.
                acronym = ""
                i += 1
                while page_text[i] != ')':
                    acronym += page_text[i]
                    i += 1
                    
                # Check whether all characters are letters or not.
                is_acronym = True
                for char in acronym:
                    if ord(char) < 64 or ord(char) > 123:
                        is_acronym = False
                
                # Check whether the acronym already exists in the dict.
                if is_acronym and acronym not in acronyms.keys():
                    
                    # Work backward to figure out words in acronym.
                    j = origin
                    acronym_letters = [letter.upper() for letter in acronym]
                    while len(acronym_letters) != 0:
                        j -= 1
                        letter = page_text[j].upper()
                        if letter == acronym_letters[-1]:
                            acronym_letters = acronym_letters[0:-1]    
                    acronym_words = ""
                    for k in range(j, origin):
                        acronym_words += page_text[k]
                        if page_text[k+1].isupper():
                            acronym_words += " "
                        
                    acronym_words += "  " + str(page_number + 1)

                    acronyms[acronym] = acronym_words

                
# Print out dict of acronyms.
print("\nPage#\n----------------------------------------------------")
for acronym, words in acronyms.items():
    words = words.replace("\n", "")
    print(words[-3:], "\t", acronym, "\t: ", words[:-2])
print()

