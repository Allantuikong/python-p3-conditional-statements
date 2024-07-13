#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
print(admin_login("admin", "12345"))


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif (40 <= temperature <= 65):
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"

    
print(hows_the_weather(39))


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
print(fizzbuzz(1.10))


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        # Handle division by zero
        if num2 == 0:
            print("Error division by zero!")
            return None
        return num1 / num2
    else:
        print("Invalid operation")
        return None

print(calculator("/", 15,3))