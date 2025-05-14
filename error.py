try:
    numerator = int(input("Enter a numerator : "))
    denominator = int(input("Enter a denominator : "))
    result = numerator/denominator
except ZeroDivisionError:
 print("Error: You cannot divide by zero!")   
except ValueError:
   print("Error! Invalid input, please enter a valid integer .")
else:
   print(f"Result : {result}")   
finally:
   print("Exception Completed!")
      
    