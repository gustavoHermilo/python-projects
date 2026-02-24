#Anagrams
print("Detecting anagrams")
word1=input("Please enter a text=")
word2=input("Please enter a second text=")

word1_1= sorted(list(word1.lower()))
word2_1= sorted(list(word2.lower()))

if word1_1 == word2_1:
    print("Anagrams")
else:
    print("Not anagrams")
