from cs50 import *
import string

# prompt the user for text
text = get_string("Text: ")

# count the avarege number of letters (lengh) per 100 words
count_words = 1
for i in text:
    if i == " ":
        count_words += 1

count_letters = 0
for i in text:
    if i.lower() in ["z", "x", "c", "v", "b", "n", "m", "a", "s", "d", "f", "g", "h", "j", "k", "l", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]:
        count_letters += 1

# count the avarage number of sentences per 100 words
count_sentences = 0
for i in text:
    if i in ["!", ".", "?"]:
        count_sentences += 1

# place this values on the Coleman-Liau index formula
L = (count_letters / count_words) * 100
S = (count_sentences / count_words) * 100

CLI = round(0.0588 * L - 0.296 * S - 15.8)

if CLI >= 16:
    print("Grade 16+")
    
# print the formula result
elif CLI < 1:
    print("Before Grade 1")

else:
    print(f"Grade {CLI}")
