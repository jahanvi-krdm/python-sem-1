num = int(input("Enter a number: "))
assert num >= 0 and num < 100, "Number must be between 0 and 99"

def ones_place(num):
    if num == 0:
        return "Zero"
    elif num == 1:
        return "One"
    elif num == 2:
        return "Two"
    elif num == 3:
        return "Three"
    elif num == 4:
        return "Four"
    elif num == 5:
        return "Five"
    elif num == 6:
        return "Six"
    elif num == 7:
        return "Seven"
    elif num == 8:
        return "Eight"
    elif num == 9:
        return "Nine"
    
def teens_place(num):
    if num == 10:
        return "Ten"
    elif num == 11:
        return "Eleven"
    elif num == 12:
        return "Twelve"
    elif num == 13:
        return "Thirteen"
    elif num == 14:
        return "Fourteen"
    elif num == 15:
        return "Fifteen"
    elif num == 16:
        return "Sixteen"
    elif num == 17:
        return "Seventeen"
    elif num == 18:
        return "Eighteen"
    elif num == 19:
        return "Nineteen"

def tens_place(num):
    if num == 2:
        return "Twenty"
    elif num == 3:
        return "Thirty"
    elif num == 4:
        return "Fourty"
    elif num == 5:
        return "Fifty"
    elif num == 6:
        return "Sixty"
    elif num == 7:
        return "Seventy"
    elif num == 8:
        return "Eighty"
    elif num == 9:
        return "Ninety"
    
def convert_to_text(n): 
    if n < 10:
        return ones_place(n)
    elif n < 20:
        return teens_place(n)
    else:
        tens = n // 10 # extract the tens place
        ones = n % 10 # extract the ones place
        if ones == 0:
            return tens_place(tens)
        else:
            return tens_place(tens) + " " + ones_place(ones)
        
def test_convert_to_text():
    assert convert_to_text(26) == "Twenty Six"
    assert convert_to_text(0) == "Zero"
    assert convert_to_text(10) == "Ten"
test_convert_to_text()

print(convert_to_text(num))




    