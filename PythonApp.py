from datetime import datetime

def say_hello():
    print("hello")

def print_date():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def add_numbers(a, b):
    return a + b

say_hello()
print_date()
print("Sum of 5 + 3 =", add_numbers(5, 3))
