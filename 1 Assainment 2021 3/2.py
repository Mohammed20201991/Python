''' The Home Work  #2 done by Mohammed Al-Hitawy (P622VN)
Supervision of teacher Mr.A Alwahab
Date 4/4/2021'''

# Home work#2 
#line 02: ask the user to enter the open (unencrypted), one-line message;
message= input('\nSimple Input (Plaintext) ')

#print(f"The Plain Text is :{message.replace('Z','A').replace('z','A')}")  # by using chining method
#line 03: prepare a string for an encrypted message (empty for now)
encrypted_meassage=[]
new_message=[]      # auxilry list 

#line 04: start the iteration through the message;
for key in message:
#line 05: if the current character is not alphabetic...
 if (key>='A' or key>='a') and (key<='Z' or key<='z'):
      new_message.append(key) 
#line 06: ...ignore it;

#line 07: convert the letter to upper-case (it's preferable to do it blindly, rather than check 
# convert a list to string to make it Upper case letters by using list comprehension 
new_message = ' '.join([str(elem) for elem in new_message])
#print(new_message.upper())   # To see Printed elemnt in upper case
#print(new_message)       # print message after upper case

# line 08: get the code of the letter and increment it by one (ASCII)
for k in new_message:
# ord()  built_in function to give ASCII  CODE for letters
      x= (ord(k))                   
     # print(x+1)
      encrypted_meassage.append(x+1)
encrypted_meassage1=[]
for i in encrypted_meassage:
      if i==33:
            continue     
      else:
       encrypted_meassage1.append(chr(i).upper())

print('Out Puts:')
# Function to convert

def listToString(encrypted_meassage1): 
    
    # initialize an empty string
    str1 = ""     
    # traverse in the string  
    for ele in encrypted_meassage1: 
        str1 += ele     
    # return string 

    #line 09: if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
    # line 10: ...change it to the A code;
    return print(str1.replace('Z','A').replace('z','A')) 

# function call and print the cipher
listToString(encrypted_meassage1)     