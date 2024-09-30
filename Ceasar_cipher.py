def encrypt(original: str, shift_amount: int) -> str:
    '''
    Takes a string and an integer.
    Shifts each letter in the string forward in the ASCII chart by the shift_amount
    pre-conditions: shift_amount > 0  
    '''
    result = ''
    for letter in original:
        new_letter = ord(letter) + shift_amount
        if new_letter > 126:
            new_letter -= 95
        result += chr(new_letter) # % 128 caters for shifts beyond the end of teh chart
    return result


def decrypt(encrypted: str, shift_amount):
    '''
    Takes a string and integer.
    Uses the shift_amount to move backwards in ASCII chart to obtain original message.
    pre-conditions: shift_amount > 0  
    '''
    result = ''
    for letter in encrypted:
        new_letter = ord(letter) - shift_amount
        if new_letter < 32:
            new_letter += 95
        result += chr(new_letter)
    return  result


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt \n").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


value = ''
if direction == "encode":
    value = encrypt(text,shift)
elif direction =="decode":
    value = decrypt(text,shift)
else:
    value = "Invalid Usage"
print(value)
