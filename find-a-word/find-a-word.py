#Find a word
word=input("Enter the word you wish to find: ").upper()
text=input("Enter the string you wish to search through: ").upper()

found=True

for letter in word:
    if letter not in text:
        found= False
        break
if found:
    print("True")
else:
    print("False")
