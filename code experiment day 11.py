def greet():
    message = "hiya buddy"
    new_message = message.capitalize()
    print("YEAH!")
    return new_message # without return, None is the result

greeting = greet()
print(greeting)
