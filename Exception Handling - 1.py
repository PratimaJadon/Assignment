#!/usr/bin/env python
# coding: utf-8

# # Q1.What is an Exception in Python? Write the difference between Exceptions and Syntax errors.

# An exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions. 
# 
# 
# Exceptions are typically caused by errors that occur due to invalid operations, such as dividing by zero, attempting to access an out-of-bounds index in a list, or opening a file that does not exist.

# In[1]:


try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception occurred: {e}")


# ## Differences Between Exceptions and Syntax Errors
# ### Exceptions:
# 
# Occurrence: Exceptions occur during the execution of a program when an error or unexpected condition arises.
# 
# Handling: Exceptions can be caught and handled using try-except blocks. This allows the program to continue running or to gracefully terminate.
# 
# Examples: Examples of exceptions include ZeroDivisionError, FileNotFoundError, IndexError, and KeyError.

# try: 
#     file = open('not_existed_file','r')
# except filenotfoundError as e:
#     print("Exception occured: {e}")

# ### Syntax Errors:
# 
# Occurrence: Syntax errors occur when the parser detects incorrect syntax in the code. This happens before the program is executed.
# 
# Handling: Syntax errors cannot be caught or handled using try-except blocks because they prevent the code from running in the first place.
# 
# Examples: Examples of syntax errors include missing colons, incorrect indentation, misspelled keywords, or mismatched parentheses.

# In[3]:


# This will cause a syntax error and prevent the program from running
if True
    print("This will cause a syntax error")


# # Q2. What happens when an exception is not handled? Explain with an example

# When an exception is not handled in Python, the program terminates abruptly and displays an error message called a traceback. The traceback provides information about the type of exception, the exact line of code where the exception occurred, and the sequence of function calls that led to the error. This abrupt termination can be problematic, especially for long-running programs or applications that require graceful error handling.

# In[5]:


def divide(a,b):
    return a/b
result = divide(10,0)
print(result)


## ZeroDivisionError: division by zero


# # Q3. Which Python statements are used to catch and handle exceptions? Explain with the help of example.

# 
# In Python, the try, except, else, and finally statements are used to catch and handle exceptions. Here’s a breakdown of how each of these statements works:
# 
# try Block: The code that might raise an exception is placed inside the try block. If an exception occurs, the rest of the try block is skipped, and the control is passed to the except block.
# 
# except Block: This block catches and handles the exception. You can specify the type of exception to catch, or use a generic except to catch any exception. Multiple except blocks can be used to handle different exceptions differently.
# 
# else Block: The else block is executed if no exceptions were raised in the try block. It is useful for code that should run only if the try block did not raise an exception.
# 
# finally Block: The finally block contains code that will be executed no matter what, whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
# 
# 

# In[6]:


try:
    result=10/2
    print("Result:{Result}")
    
except ZerodivisionError as e:
    print("Exception occured :{e}")
except TypeError as e:
    # Handle wrong type error
    print(f"Exception occurred: {e}")
else:
    # This block will be executed if no exceptions were raised
    print("No exceptions occurred")
finally:
    # This block will be executed no matter what
    print("Execution of the try-except block is complete")
    


# # Q4. Explain with an example:
# a.try and else
# b.finally
# c. raise

# In[7]:


def divide(a,b):
    if b==0:
        raise ValueError('Cannot divide by zero')
    return a/b
try:
    result = divide(10,0)
except ValueError as e:
    print('Exception error:{e}')


# # Q5. What are custom Exception in python? Why do we need Custom Exception ? Example with an example

# # Custom Exceptions in Python
# Custom exceptions in Python are user-defined exception classes that are created to handle specific error situations unique to a particular program or module. They extend the standard exception classes and provide a way to add more meaningful error messages or additional error-handling capabilities tailored to the specific needs of the application.
# 
# 
# # Why Do We Need Custom Exceptions?
# Clarity: Custom exceptions can make your code more readable and maintainable by providing clear, descriptive error messages.
# 
# Specificity: They allow you to distinguish between different types of errors and handle them accordingly.
# 
# Modularity: Custom exceptions can encapsulate error-handling logic that is specific to a module or class, making the code more modular and easier to debug.
# 
# Extendability: They provide a mechanism to add additional attributes and methods to exception classes, enhancing error-handling capabilities.

# In[10]:


class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age} -> {self.message}'

  


# In[11]:


def check_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    else:
        print(f"Age {age} is valid.")

try:
    age = 130
    check_age(age)
except InvalidAgeError as e:
    print(f"Exception occurred: {e}")


# # Q6. Create a custom exception class.Use this class to handle an exception.

# In[14]:


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount, message="Insufficient funds for this transaction"):
        self.balance = balance
        self.amount = amount
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Attempted to withdraw {self.amount} with a balance of {self.balance}. {self.message}'


# In[15]:


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(100)  # Create an account with a balance of $100
    print(f"Balance before withdrawal: ${account.balance}")
    account.withdraw(150)  # Attempt to withdraw $150
except InsufficientFundsError as e:
    print(f"Exception occurred: {e}")
finally:
    print(f"Balance after attempted withdrawal: ${account.balance}")

    


# In[ ]:




