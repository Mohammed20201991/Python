''' The Home Work  #2 done by Mohammed Al-Hitawy (P622VN)
Supervision of teacher Mr.A Alwahab
Date 4/4/2021'''

#Home work3
# make dictonary to stor char and letters with key : value 
letter_dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
              "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
              "W": 32, "X": 33, "Y": 34, "Z": 35,
              "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

# compersion way to get the code for each char
letters = {ord(k): str(v) for k, v in letter_dic.items()} 

#-------------------------------------------------
# Function to check the vaildty of number depend on the folloing criteria 
def chech_validation_chars_iban(iban):
    zeros_iban = iban[:2] + '00' + iban[4:]
    iban_inverted = zeros_iban[4:] + zeros_iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    verification_chars = 98 - (int(iban_numbered) % 97)

    if verification_chars < 10:
        verification_chars = '{:02}'.format(int(verification_chars))
    return verification_chars


def validate_iban(iban):
    iban_inverted = iban[4:] + iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    return int(iban_numbered) % 97

#When the Python interpreter reads a file, the __name__ variable is set as __main__ if the module being run
if __name__ == '__main__':
    my_iban ='GB72HBZU70067212125300'
    # my_iba=input('Enter the IBAN ')
    #my_iba.replace(' ','')
    #line 03: ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability...
    #line 04: ...but remove them immediately)
    # make vildation
    if my_iban.isalnum():
      print('It is a number and letters only ')
    else:
        print('The meassage shuld contions only numbers and strings')
    print(my_iban)
    #07: the IBAN mustn't be shorter than 15 characters (this is the shortest variant, used in Norway)
    if(len(my_iban)) in range(15,32):
    #line 09: moreover, the IBAN cannot be longer than 31 characters (this is the longest variant,used in Malta
          print('true')
    else:
            print('lenght must be bettween 15 and 32')
# line 08: if it is shorter, the user is informed;
#line 10: if it is longer, make an announcement;
#convert it into two digits (note the way it's done here)
    if chech_validation_chars_iban(my_iban) == int(my_iban[2:4]):
        #is the remainder of the division of iban2 by 97 equal to 1?
        if validate_iban(my_iban) == 1:
              #If yes, then success;
            print('(Success)IBAN ok!\n')
        else:
              #Otherwise...
            print('IBAN invalid!\n')
    else:
#line 23: ...the number is invalid
        print('IBAN invalid!\n')




'''
# Second way  Please denote the first 
# import string
# LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}

# def _number_iban(iban):
#     return (iban[4:] + iban[:4]).translate(LETTERS)

# def generate_iban_check_digits(iban):
#     number_iban = _number_iban(iban[:2] + '00' + iban[4:])
#     return '{:0>2}'.format(98 - (int(number_iban) % 97))

# def valid_iban(iban):
#     return int(_number_iban(iban)) % 97 == 1
# if __name__ == '__main__':
#     my_iban = 'DE02100100100152517108'
#     if generate_iban_check_digits(my_iban) == my_iban[2:4] and valid_iban(my_iban):
#         print('Vaild IBAN ok!\n')
#     else:
#         print('IBAN not Vaild!\n')
'''