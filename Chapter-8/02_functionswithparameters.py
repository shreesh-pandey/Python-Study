# Let's create a function that uses a placeholder (called parameters) to greet the user.

def greet(name):
    print(f"Hello, {name}!")

#  Function call

greet("Alice")  # Here, "Alice" is the argument.

# A function with parameters means that when the function is defined, it includes placeholders (called parameters) that allow values (arguments) to be passed into the function when it is called.

# Common Mistakes

# 1. Calling a function without providing all required parameters:
    
def say_hi(name):
    print("Hi", name)
    
    say_hi()  # ❌ TypeError: missing 1 required positional argument
    
    
# 2. Giving extra arguments than the function expects:
    
def say_hi(name):
    print("Hi", name)
    
    say_hi("Alice", "Bob")  # ❌ TypeError: too many arguments
    