#The digit of life
date=input("Please enter your date of birthday (YYYYMMDD)=")
digits_list= [int (d) for d in str (date)]

total = sum(digits_list)
digits_total= [int (d) for d in str (total)]
if len(digits_total)==2:
    digit_of_life = sum(digits_total)
    print(f"The digit of life is {digit_of_life}")
else:
    print(f"The digit of life is {total}")
    
