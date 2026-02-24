#Detecting Palindromes
word= input("Please enter a word=")
word1= word.replace(" ","").lower()
word2= list(word1)

i= 0
is_palindrome =True
while i< len(word2) // 2:
    if word2[0+i] != word2[-1-i] :
        is_palindrome= False
        break
    i+=1
if is_palindrome:
    print(f"{word} is a palindrom")
else:
    print(f"{word} is not  a palindrom")
    
