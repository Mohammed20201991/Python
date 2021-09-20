''' The Home Work  #1 done by Mohammed Al-Hitawy (P622VN)
Supervision of teacher Mr.A Alwahab
Date 4/4/2021'''

# Home Work   1 
# list all poossible decimal numbers (0 to 9)
a=[
"# # #\n#   #\n#   #\n#   #\n# # #  ",
#----------------------------------------------------
"#\n#\n#\n#\n#",
#----------------------------------------------------
"""# # #\n    #\n# # #\n#    \n# # #  """,
#----------------------------------------------------
"""# # #\n    #\n# # #\n    #\n# # #  """,
#----------------------------------------------------
"""#   #\n#   #\n# # #\n    #\n    #  """,
#----------------------------------------------------
"""# # #\n#   \n# # #\n    #\n# # #  """,
#----------------------------------------------------
"""# # #\n#   \n# # #\n#   #\n# # #  """,
#----------------------------------------------------
"""# # #\n    #\n    #\n    #\n    #  """, 
#----------------------------------------------------
"""# # #\n#   #\n# # #\n#   #\n# # #  """,  
#----------------------------------------------------
"""# # #\n#   #\n# # #\n    #\n    #  """,   
]  # End of List 

# conversion of number to list of integers
  
# read number from prompt or user of can be read from file (binary,jison,txt....)
num = str(input('\nSample Input'))
  
# printing number 
# print ("The original number is " + str(num))
  
# by using list comprehension
# to convert number to list of integers
var = [int(x) for x in str(num)]
  
# printing result 
#print ("The list from number is " + str(var))
# Packing element of list by usin (*)   [1,2,3] => 1 2 3
print(*var)
print('Sample Output:')
#the LED lights on her.
for x in var:
      print(a[x],'\n')
