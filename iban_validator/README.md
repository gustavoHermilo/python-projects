#  IBAN Validator (Python)

A simple Python program that validates an IBAN (International Bank Account Number) using the official IBAN validation algorithm.

This project:
- Cleans user input
- Validates characters and length
- Rearranges the IBAN structure
- Converts letters to numbers
- Applies the Modulo 97 validation rule

---

## Features
- Removes spaces automatically
- Validates alphanumeric characters
- Checks IBAN length
- Implements official IBAN validation logic
- Beginner-friendly Python code

---

## How IBAN Validation Works

1. Move the first 4 characters to the end of the IBAN  
2. Convert letters into numbers:
   - A = 10, B = 11, ..., Z = 35  
3. Convert the string into a number  
4. Apply modulo 97  
5. If result == 1 → IBAN is **VALID**  
   Else → IBAN is **INVALID**

