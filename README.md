# Acronym Extractor - (Basic Text Processing Version)
### A simple python app that extracts all the acronyms and their corresponding meanings from a PDF file and prints them neatly for easy reference while reading.


<br>

## Requirements:
<ul>
  <li>Python 3.7</li>
  <li>PyPDF2 1.26.0</li>
</ul>

## Setup:
1. Make sure the above requirements have been installed
2. Clone or download this repository
3. Using the terminal, navigate into the folder containing this repository
4. Run this command:
```
python acronym_extractor.py
```
or ```python3 acronym_extractor.py``` if python 3 is not your default version.

<br>

# Usage:

<ol>
  <li>Download the paper you want to read into your current working directory. Give it a simple name.</li>

  <li>Run the command ```python acronym_extractor.py```</li>

  <li>You will be prompted with: ```Enter the PDF file name:```</li>

  <li>Type in the name of the file. Be sure to include ".pdf" at the end.</li>
</ol>

<br>
The program will scan the contents of the file and compile a list of all the acronyms and their associated meanings.
Each acronym will be printed to the terminal in the order that they first appear in the paper, labelled by page number.

#### Note:

- Due to the difficulty in translating from the PDF format, some acronyms will not come out properly.
- The way the program finds the acronyms' definitions means that it may not capture the full first word, especially if the definitions do not use capital letters. You may need to refer to the paper itself to get the exact definitions.




