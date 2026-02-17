#Caesar Cipher

text= input("Enter text to encrypt: ")

while True:
    try:
        shift= int(input("Enter shift value (1-25):"))
        if 1<= shift <=25:
            break
        else:
            print("Shift must be between 1 and 25.")
    except ValueError:
        print("Please enter a valid number")
encrypted_text=" "

for ch in text:
    if ch.islower():
        new_char= ord(ch)+shift
        if new_char>ord('z'):
            new_char-=26
        encrypted_text+= chr(new_char)
    elif ch.isupper:
        new_char= ord(ch)+shift
        if new_char>ord('Z'):
            new_char -=26
        encrypted_text += chr(new_char)
    else:
        encrypted_text += ch
print("Encrypted text :",encrypted_text)
