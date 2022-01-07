user_input = input("Enter your name:")
# this is a string formatting expression
message = "Hello %s!" % user_input

# same as line above just newer syntax
message = f"Hello {user_input}"
print(message)