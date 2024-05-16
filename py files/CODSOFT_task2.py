#!/usr/bin/env python
# coding: utf-8

# In[1]:


class calculator:

        
    def addFunction(self,number1,number2):
        return number1+number2
    
    def subtractFunction(self,number1,number2):
        return number1-number2
        
    def multiplyFunction(self,number1,number2):
        return number1*number2
           
    def divideFunction(self,number1,number2):
        if number2 != 0:
            return number1/number2
        else:
            return "Cannot divide by zero!"
        
print("CODSOFT Task2: Calculator")
print("")
while True:    
    
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    MyCalculator = calculator()


    operation = int(input(""""Please select operation: 
                          1. ADD
                          2. SUBTRACT
                          3. MULTIPLY
                          4. DIVIDE
                          5. Exit
                          Enter Here: """))


    if operation==1:
        print("Result: ",MyCalculator.addFunction(number1,number2))

    if operation==2:
        print("Result: ",MyCalculator.subtractFunction(number1,number2))

    if operation==3:
        print("Result: ",MyCalculator.multiplyFunction(number1,number2))

    if operation==4:
        print("Result: ",MyCalculator.divideFunction(number1,number2))

    if operation==5:
        print("Program Terminated.")
        break


# 

# In[ ]:




