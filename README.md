# Acronym Extractor - (Basic Text Processing Version)
### A simple python app that extracts all the acronyms and their corresponding meanings from a PDF file and prints them neatly for easy reference while reading.

<p align="center">
  <img src="https://github.com/jmsbutcher/acronym-extractor/blob/main/Images/desktop_example.png">
</p>

<br>
I came up with the idea for this app when I started reading a paper for my machine learning class. This paper had no less than *five* acronyms on its first page, all of them made up of large words. These acronyms were defined once, and then the paper proceeded to refer to them over and over by just their letters. Trying to understand the advanced concepts presented in the paper was hard enough without having to refer back to the acronym definitions every time I saw one. ("What was DTI again? Diffusion something... Or was that DAI?") I had to search for those little definitions every two seconds, lost somewhere in the thick text. <br><br>

If I had a physical print copy of the paper I could just highlight the important acronyms, but they would still be scattered throughout the pages. And this would be no help if I was reading a PDF on the laptop. Should I just try and memorize the acronyms? That might actually take less time.<br>

But what if there were a better way...<br>

And so I wrote this little helper program to make my research much, much easier. Now I can focus on learning the reserach, not wasting time doing a word search!<br>

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

  <li>Run the command "python acronym_extractor.py"</li>

  <li>You will be prompted with: "Enter the PDF file name:"</li>

  <li>Type in the name of the file. Be sure to include ".pdf" at the end.</li>
</ol>

<br>
The program will scan the contents of the file and compile a list of all the acronyms and their associated meanings.
Each acronym will be printed to the terminal in the order that they first appear in the paper, labelled by page number.

<br>

<p align="center">
  <img src="https://github.com/jmsbutcher/acronym-extractor/blob/main/Images/command_line_1.png">
</p>

<br>

You can now copy and paste the output into a small notepad on your desktop for easy reference.

<br>

#### Note:

- Due to the difficulty in translating from the PDF format, some acronyms will not come out properly.
- The way the program finds the acronyms' definitions means that it may not capture the full first word, especially if the definitions do not use capital letters. You may need to refer to the paper itself to get the exact definitions.

#### Future work:

- I plan to implement computer vision in the next version of this app. The program will scan the document as an image, thus avoiding the problems mentioned above.

<br>
<br>

Paper source:

S. Hu, Y. Li, and B. Li, "Video2Vec: Learning Semantic Spatial-Temporal Embeddings for Video Representation," *International Conference on Pattern Recognition*, 2016.

<br>

<hr>
© 2020 James Butcher

jmsbutcher1576@gmail.com



