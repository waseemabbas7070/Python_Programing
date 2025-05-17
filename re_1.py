import re
# Match function
# pattern = "^Hello"
# string = "Hellow, world!"
# if re.match(pattern,string):
#     print('Pattern Matched!')
# else:
#     print("Not Matched!")  

# pattern = r"\bp\w+"  
# string = "python is greate! let's learn about programming."

# matches = re.findall(pattern,string)

# print(f"Matches Found : {matches}" )

pattern = r"\d+"

string = "my phone number is 123-453-556"

replaced_string = re.sub(pattern,"#",string)
print(replaced_string)